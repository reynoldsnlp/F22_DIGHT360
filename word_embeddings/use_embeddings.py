from gensim.models import Word2Vec
import gensim.downloader
import pandas as pd

# Load your own
model = Word2Vec.load("word2vec.model")
print(model.wv['computer'])
print(model.wv.most_similar('computer', topn=10))

# ...or download pretrained models
# Show all available models in gensim-data
print(list(gensim.downloader.info()['models'].keys()))
# ['fasttext-wiki-news-subwords-300',
#  'conceptnet-numberbatch-17-06-300',
#  'word2vec-ruscorpora-300',
#  'word2vec-google-news-300',
#  'glove-wiki-gigaword-50',
#  'glove-wiki-gigaword-100',
#  'glove-wiki-gigaword-200',
#  'glove-wiki-gigaword-300',
#  'glove-twitter-25',
#  'glove-twitter-50',
#  'glove-twitter-100',
#  'glove-twitter-200',
#  '__testing_word2vec-matrix-synopsis']

# Download the "glove-twitter-200" embeddings
print('Loading large word vector model...')
glove_vectors = gensim.downloader.load('glove-twitter-200')

# Use the downloaded vectors as usual:
glove_vectors.most_similar('twitter')
# [('facebook', 0.948005199432373),
#  ('tweet', 0.9403423070907593),
#  ('fb', 0.9342358708381653),
#  ('instagram', 0.9104824066162109),
#  ('chat', 0.8964964747428894),
#  ('hashtag', 0.8885937333106995),
#  ('tweets', 0.8878158330917358),
#  ('tl', 0.8778461217880249),
#  ('link', 0.8778210878372192),
#  ('internet', 0.8753897547721863)]


# Analogies


def pp(obj):
    """Pretty print."""
    print(pd.DataFrame(obj))


def analogy(worda, wordb, wordc):
    result = glove_vectors.most_similar(negative=[worda],
                                        positive=[wordb, wordc])
    return result[0][0]


countries = ['australia', 'canada', 'germany', 'ireland', 'italy']
foods = [analogy('us', 'hamburger', country) for country in countries]
pp(zip(countries, foods))
