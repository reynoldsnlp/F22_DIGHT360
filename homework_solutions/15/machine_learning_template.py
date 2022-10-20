"""Template for assignment 13. (machine-learning)."""

from collections import Counter
from glob import glob
import re
# from string import punctuation as punct  # string of common punctuation chars
import sys

import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
from sklearn import model_selection
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import accuracy_score
import spacy
from tqdm import tqdm  # progress bar

# import model classes
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

MC_DIR = '../Mini-CORE/'
nlp = spacy.load('en_core_web_sm')  # or another model, if you prefer


def clean(in_file):
    """Remove headers from corpus file."""
    out_str = ''
    for line in in_file:
        if re.match(r'<[hp]>', line):
            out_str += re.sub(r'<[hp]>', '', line)
    return out_str


def subcorpus(name):
    """Extract subcorpus from filename.

    name -- filename

    The subcorpus is the first abbreviation after `1+`.
    """
    return name.split('+')[1]


def pro1_tr(tokens):
    """Compute 1st person pronoun-token ratio for input Text.

    tokens -- list of strings
    """
    regex = r'(?:i|me|my|mine)$'
    pro1_count = len([i for i in tokens if re.match(regex, i, re.I)])
    return pro1_count / len(tokens)


def pro2_tr(tokens):
    """Compute 2nd person pronoun-token ratio for input Text.

    tokens -- list of strings
    """
    regex = r'(?:ye|you(?:rs?)?)$'
    pro2_count = len([i for i in tokens if re.match(regex, i, re.I)])
    return pro2_count / len(tokens)


def pro3_tr(tokens):
    """Compute 3rd person pronoun-token ratio for input Text.

    tokens -- list of strings
    """
    regex = r'(?:he|him|his|she|hers?|its?|they|them|theirs?)$'
    pro3_count = len([i for i in tokens if re.match(regex, i, re.I)])
    return pro3_count / len(tokens)


def q_count(in_str):
    """Compute proportion of letters that are q."""
    return in_str.count('q') / len(in_str)


# TODO add feature names HERE
feat_names = ['1st-pro', '2nd-pro', '3rd-pro', 'q_count',
              'genre']

print('Extracting features...', file=sys.stderr)
genre_counter = Counter()
with open('mc_features.csv', 'w') as out_file:
    print(*feat_names, sep=',', file=out_file)
    for f in tqdm(glob(MC_DIR + '*.txt')):
        genre = subcorpus(f)
        genre_counter.update([genre])
        if genre_counter[genre] > 10:  # TODO comment out this line
            continue  # move on without finishing the loop  # TODO comment out
        with open(f) as the_file:
            raw_text = clean(the_file)
        # preprocess
        doc = nlp(raw_text)
        tokens = [tok.text for tok in doc]
        # TODO call functions HERE
        print(pro1_tr(tokens), pro2_tr(tokens), pro3_tr(tokens),
              q_count(raw_text), genre, sep=',', file=out_file)

###############################################################################
# Do not change anything below this line! The assignment is simply to try to
# design useful features for the task by writing functions to extract those
# features. Simply write new functions and add a label to feat_names and call
# the function in the `print` function above that writes to out_file. MAKE SURE
# TO KEEP the order the same between feat_names and the print function, ALWAYS
# KEEPING `genre` AS THE LAST ITEM!!
###############################################################################

# Load dataset
# make pandas DataFrame (something like a spreadsheet; 2-dimensional table)
with open('mc_features.csv') as mc_file:
    dataset = pandas.read_csv(mc_file, keep_default_na=False, na_values=['_'])  # avoid 'NA' category being interpreted as missing data  # noqa
print(type(dataset), file=sys.stderr)

# Summarize the data
print('"Shape" of dataset:', dataset.shape,
      f'({dataset.shape[0]} instances of {dataset.shape[1]} attributes)',
      end='\n\n', file=sys.stderr)
print('"head" of data:\n', dataset.head(20), end='\n\n', file=sys.stderr)
print('Description of data:\n:', dataset.describe(), end='\n\n',
      file=sys.stderr)
print('Class distribution:\n', dataset.groupby('genre').size(), end='\n\n',
      file=sys.stderr)

# Visualize the data
print('Drawing boxplot...', file=sys.stderr)
grid_size = 0
while grid_size ** 2 < len(dataset):
    grid_size += 1
dataset.plot(kind='box', subplots=True, layout=(grid_size, grid_size),
             sharex=False, sharey=False)
fig = plt.gcf()  # get current figure
fig.savefig('boxplots.png')

# histograms
print('Drawing histograms...', file=sys.stderr)
dataset.hist()
fig = plt.gcf()
fig.savefig('histograms.png')

# scatter plot matrix
print('Drawing scatterplot matrix...', file=sys.stderr)
scatter_matrix(dataset)
fig = plt.gcf()
fig.savefig('scatter_matrix.png')

print('Splitting training/development set and validation set...',
      file=sys.stderr)
# Split-out validation dataset
array = dataset.values  # two-dimensional numpy array
# https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html#advanced-indexing  # noqa: E501
feats = array[:, :-1]  # `:` copies all rows, `:-1` slices all but last column
labels = array[:, -1]  # `:` copies all rows, `-1` selects only last column
print('\tfull original data ([:5]) and their respective labels:',
      file=sys.stderr)
print(feats[:5], labels[:5], sep='\n\n', end='\n\n\n', file=sys.stderr)
seed = 42  # used to make the same 'pseudo-random' choices in each run
split = model_selection.train_test_split(feats, labels,
                                         test_size=0.2,
                                         random_state=seed)
feats_train, feats_validation, labels_train, labels_validation = split
# print('\ttraining data:\n', feats_train[:5],
#       '\ttraining labels:\n', labels_train[:5],
#       '\tvalidation data:\n', feats_validation[:5],
#       '\tvalidation labels:\n', labels_validation[:5], sep='\n\n')


print('Initializing models...', file=sys.stderr)
models = [('LR', LogisticRegression(solver='lbfgs', multi_class='auto')),
          ('LDA', LinearDiscriminantAnalysis()),
          ('KNN', KNeighborsClassifier()),
          ('CART', DecisionTreeClassifier()),
          ('NB', GaussianNB()),
          ('SVM', SVC(gamma='scale'))]
print('Training and testing each model using 10-fold cross-validation...',
      file=sys.stderr)
# evaluate each model in turn
results = []  # track results for boxplot
for name, model in models:
    # https://chrisjmccormick.files.wordpress.com/2013/07/10_fold_cv.png
    kfold = model_selection.KFold(n_splits=10, shuffle=True,
                                  random_state=seed)
    cv_results = model_selection.cross_val_score(model, feats_train,
                                                 labels_train, cv=kfold,
                                                 scoring='accuracy')
    results.append(cv_results)
    msg = f'{name}: {cv_results.mean()} ({cv_results.std()})'
    print(msg, file=sys.stderr)

print('\n\nDrawing algorithm comparison boxplots...', file=sys.stderr)
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels([name for name, model in models])
fig = plt.gcf()
fig.savefig('compare_algorithms.png')

# One could use the following template to perform final evaluation
# Make predictions on validation dataset
# best_model = KNeighborsClassifier()
# best_model.fit(feats_train, labels_train)
# predictions = best_model.predict(feats_validation)
# print('Accuracy:', accuracy_score(labels_validation, predictions),
#       file=sys.stderr)
# print('Confusion matrix:', file=sys.stderr)
# print('labels:', feat_names, file=sys.stderr)
# print(confusion_matrix(labels_validation, predictions, labels=feat_names),
#       file=sys.stderr)
# print('\n\nClassification report:', file=sys.stderr)
# print(classification_report(labels_validation, predictions), file=sys.stderr)
