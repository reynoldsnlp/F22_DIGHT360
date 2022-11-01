import pandas
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold


with open('mc_features.csv') as mc_file:
    dataset = pandas.read_csv(mc_file, keep_default_na=False, na_values=['_'])  # avoid 'NA' category being interpreted as missing data  # noqa

array = dataset.values
feats = array[:, :-1]
labels = array[:, -1]

# Feature ranking with Recursive Feature Elimination and Cross-Validated
# selection of the best number of features.
ETC = ExtraTreesClassifier(n_estimators=10)
skf = StratifiedKFold(10, shuffle=True, random_state=42)
selector = RFECV(ETC, step=1, cv=skf)
selector = selector.fit(feats, labels)
# In the following line, remember that iterating over a pandas DataFrame gives
# you just the column names, i.e. the names of the features
evaluations = zip(dataset, selector.support_, selector.ranking_)
print('Recursive feature evaluation on cross-validation (RFECV):')
print('Name', 'Support', 'Rank', sep='\t')
for name, support, rank in sorted(evaluations, key=lambda x: x[-1],
                                  reverse=True):
    print(name, support, rank, sep='\t')
