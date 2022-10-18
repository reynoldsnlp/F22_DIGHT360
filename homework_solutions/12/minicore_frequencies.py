from collections import Counter
from glob import glob
import re

from spacy.lang.en import English

nlp = English()
# Create a Tokenizer with the default settings for English
# including punctuation rules and exceptions
tokenizer = nlp.tokenizer


def preprocess(in_file) -> str:
    """Remove headers from corpus file. Returns lines that begin
    with <h> or <p>.

    Parameters
    ----------

    in_file : TextIOWrapper
        The file object wrapping a corpus document
    """
    out_str = ''
    for line in in_file:
        if re.match(r'<[hp]>', line):
            out_str += re.sub(r'<[hp]>', '', line)
    return out_str


def get_genre(name) -> str:
    """Extract genre (subcorpus) from filename. The subcorpus is
    the first abbreviation after `1+`.

    Parameters
    ----------

    name : str
        The filename of the corpus document
    """
    return name.split('+')[1]


freqdists = {'IN': Counter(),
             'IP': Counter(),
             'LY': Counter(),
             'NA': Counter(),
             'OP': Counter(),
             'SP': Counter(),
             }

for fname in glob('../Mini-CORE/*.txt'):
    genre = get_genre(fname)
    with open(fname) as f:
        text = preprocess(f)
    doc = tokenizer(text)
    freqdists[genre].update(token.text for token in doc)

for genre, freqdist in freqdists.items():
    with open(f'{genre}.tsv', 'w') as f:
        for tok, freq in freqdist.most_common():
            print(tok, freq, sep='\t', file=f)
