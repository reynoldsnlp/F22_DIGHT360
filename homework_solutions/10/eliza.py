"""An ELIZA-like chatbot."""

import re


def process_input(input_str):
    if re.search('happy', input_str, flags=re.IGNORECASE):
        return "I'm glad to hear it. What makes you happy?"
    elif input_str.lower() in {'quit', 'exit', 'q', 'stop'}:
        return  # equivalent to `return None`
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
