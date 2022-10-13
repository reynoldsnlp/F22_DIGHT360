"""
You can use the normal spacy pipeline ("en-core-web-sm") to do tokenization,
but will take more compute time to load all of the NLP models. If all you need
is a tokenizer, the following code is an example of how to do that.
"""
from collections import Counter
from pprint import pprint  # pretty print

from spacy.lang.en import English

nlp = English()
# Create a Tokenizer with the default settings for English
# including punctuation rules and exceptions
tokenizer = nlp.tokenizer
doc = tokenizer('This is a sentence, Mr. Bean. So is this!. And a sentence is '
                'a lot more than some people think. And that\'s saying '
                'something! Why, Mr. Bilbo said so himself!')

c = Counter(t.text for t in doc)
pprint(c.most_common(20))

