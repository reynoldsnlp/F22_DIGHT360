# Sentiment analysis

Sentiment analysis aims to tell us whether a text is generally positive or
negative. The output is generally a "polarity" score (usually between -1 and
1), where a positive number reflects a positive text, and a negative score
reflects a negative text.

I will introduce two different libraries that can do sentiment analysis for us.
To install them, run the following commands in your command line:

```bash
$ python3 -m pip install --user vaderSentiment
$ python3 -m pip install --user textblob
```

## VADER

One of the first widely used sentiment analyzers was called LIWC (pronounced
`Luke`), so when researchers came up with a better way, of course they had to
name it VADER (Valence Aware Dictionary and sEntiment Reasoner). It is based on
[vocabulary
lists](https://github.com/cjhutto/vaderSentiment/blob/master/vaderSentiment/vader_lexicon.txt)
that are labeled as positive and negative. The output of the algorithm actually
gives 4 scores: `neg`, `neu`, `pos`, `compound`. An explanation of these scores
is [here](https://github.com/cjhutto/vaderSentiment#about-the-scoring), but
usually you only need to use the `compound` score. If you want to convert the
score to a category, a compound score below -0.05 is considered negative, and a
compound score above 0.05 is considered positive.

## Text Blob

TextBlob is also based on [vocabulary
lists](https://github.com/sloria/TextBlob/blob/dev/textblob/en/en-sentiment.xml).
It might even be the VADER algorithm under the hood, but their documentation is
not very helpful.

## How to use them

```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

sentences = [
    'Devin is smart, handsome, and funny.',  # positive sentence example
    'Devin is smart, handsome, and funny!',  # punctuation emphasis handled correctly (sentiment intensity adjusted)
    'Devin is very smart, handsome, and funny.',  # booster words handled correctly (sentiment intensity adjusted)
    'Devin is VERY SMART, handsome, and FUNNY.',  # emphasis for ALLCAPS handled
    'Devin is VERY SMART, handsome, and FUNNY!!!',  # combination of signals - Devin appropriately adjusts intensity
    'Devin is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!',  # booster words & punctuation make this close to ceiling for score
    'The book was good.',  # positive sentence
    'The book was kind of good.',  # qualified positive sentence is handled correctly (intensity adjusted)
    'The plot was good, but the characters are uncompelling and the dialog is not great.',  # mixed negation sentence
    'A really bad, horrible book.',  # negative sentence with booster words
    "At least it isn't a horrible book.",  # negated negative sentence with contraction
    ':) and :D',  # emoticons handled
    '😡 ☹️  😞 😖',  # emoji not handled
    '',  # an empty string is correctly handled
    'Today sux',  # negative slang handled
    'Today sux!',  # negative slang with punctuation emphasis handled
    'Today SUX!',  # negative slang with capitalization emphasis
    "Today kinda sux! But I'll get by, lol",  # mixed sentiment example with slang and constrastive conjunction 'but'
    'This is awful.',
    'My date was really memorable!',
    'What a terrible show! Do not waste your money!',
    'I can\'t wait to get started on my new project.',
    'Python is the BEST!!!!!!!',
    'It was meh.',
    'I never want to do that again!',
    'This is not the terrible, awful, useless waste of time that people say it is!',
]

# VADER approach
sentiment_analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(f'{sentence:<60}', end='')
    ps = sentiment_analyzer.polarity_scores(sentence)  # ps is dictionary of the four scores
    for name, score in sorted(ps.items()):
        print(f'\t{name}: {score:> .3}', end='  ')
    print()
print('\n\n')


# TextBlob approach
# https://textblob.readthedocs.io/en/dev/api_reference.html#module-textblob.en.sentiments
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print(testimonial.sentiment)
# Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
print(testimonial.sentiment.polarity)
# 0.39166666666666666
joined_sentences = '\n'.join(sentences)  # textblob automatically separates sentences
blob = TextBlob(joined_sentences)
print('Sentiment of all sentences together:', blob.sentiment)
# Sentiment of all sentences together: Sentiment(polarity=0.13295708198051948, subjectivity=0.7949945887445887)
print(blob.tags)  # POS tags
# [('Devin', 'NNP'), ('is', 'VBZ'), ('smart', 'JJ'), ('handsome', 'JJ'), ...]
print(blob.noun_phrases)
# ['devin', 'devin', 'devin', 'devin', 'very smart', 'funny', 'devin', ...]
for sentence in blob.sentences:
    print(sentence, sentence.sentiment)
# Devin is smart, handsome, and funny. Sentiment(polarity=0.32142857142857145, subjectivity=0.8809523809523809)
# Devin is smart, handsome, and funny! Sentiment(polarity=0.3422619047619048, subjectivity=0.8809523809523809)
# ...
```
