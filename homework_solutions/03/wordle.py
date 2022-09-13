"""Very basic clone of the popular online game Wordle."""


def check_the_guess(target_word, guessed_word):
    """Check how well a guess matches the target.

    Parameters
    ----------
    target_word : str
        The word that the user is trying to guess
    guessed_word : str
        The word that was given by the user
    """
    feedback = ''
    i = 0
    # for i in range(len(guessed_word)):  # replace `letter` below with guessed_word[i]
    # for i, letter in enumerate(guessed_word)):
    for letter in guessed_word:
        if target_word[i] == guessed_word[i]:
            feedback += letter.upper()
        elif letter in target_word:
            feedback += letter + '*'
        else:
            feedback += letter
        i += 1
    return feedback


target_word = 'pilot'
while True:
    guessed_word = input('Guess a five-letter word: ')
    feedback = check_the_guess(target_word, guessed_word)
    if feedback.isupper():
        print(f'Congratulations! The word was {feedback}.')
        break
    print(feedback)
