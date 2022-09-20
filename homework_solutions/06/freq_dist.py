# from collections import Counter
import re


def get_freq_dist(text, normalize=True):
    """Make a frequency distribution from the given text.

    Parameters
    ==========
    text : str
        Text from which to generate the frequency dictionary
    normalize : bool
        Whether to normalize the text (lowercase and apostrophes)
    """
    if normalize:
        text = text.lower().replace('’', "'")
    tokens = re.findall(r"n't|\w+(?!'t)|[^\s]+", text)
    # return Counter(tokens)  # This object can do it all for us!
    freq_dict = {}
    for token in tokens:
        if token not in freq_dict:
            freq_dict[token] = 1
        else:
            freq_dict[token] += 1  # same as freq_dict[token] = freq_dict[token] + 1
        # or...
        # try:
        #     freq_dict[token] += 1
        # except KeyError:
        #     freq_dict[token] = 1
    return freq_dict


toy_text = '''Fuzzy Wuzzy was a bear,
Fuzzy Wuzzy had no hair,
Fuzzy Wuzzy wasn’t really fuzzy,
Was he?'''

print(get_freq_dist(toy_text))

with open('nlp.txt') as f:
    freq_dict = get_freq_dist(f.read())
    print(freq_dict)

print(len(freq_dict), 'types.')
print(sum(freq_dict.values()), 'tokens.')
print(list(freq_dict.values()).count(1), 'hapaxes.')
