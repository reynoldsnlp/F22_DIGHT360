"""An ELIZA-like chatbot."""

import re

import spacy

nlp = spacy.load('en_core_web_sm')


def process_input(input_str):
    doc = nlp(input_str)
    eat_toks = []                                          # EX A
    for token in doc:                                      # EX A
        if token.lemma_ in {'eat', 'binge'}:               # EX A
            eat_toks.append(token)                         # EX A
    if re.search('happy', input_str, flags=re.IGNORECASE):
        return "I'm glad to hear it. What makes you happy?"
    elif input_str.lower() in {'quit', 'exit', 'q', 'stop'}:
        return  # equivalent to `return None`
    elif eat_toks:                                         # EX A
        return f"Talk more about {eat_toks[0].lemma_}ing." # EX A
    elif toks := [t for t in doc if t.lemma_ in {'eat', 'binge'}]:  # EX B using the walrus operator and a list comprehension
        return f"Talk more about {toks[0].lemma_}ing."              # EX B
    else:
        return "Tell me more about that."


client = input('ELIZA: Is something troubling you?\n> ')
while True:
    eliza = process_input(client)
    if eliza is None:
        print('Goodbye!')
        break
    else:
        client = input(f'ELIZA: {eliza}\n> ')
