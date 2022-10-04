"""Core concepts quiz

STEP 1: Complete the quiz WITHOUT USING ANY RESOURCES.
STEP 2: Go back and revise your answers using any resource EXCEPT other humans.

Add a comment to the end of every line of code to explain what it is doing. Be
VERY detailed in your explanations. (It's okay if the lines are too long for
PEP8.)

Where you see comments beginning with TODO, add/change the code to complete
the feature described in the comment. Then delete TODO the comment."""

# TODO add an import statement to import the `variance` function from the
# `statistics` module, giving the function the alias `var`.
# TODO import the `Counter` class from the `collections` module.
# Make sure the modules are in alphabetical order when you are done.
import re

print('The variance of [1, 2, 3] is', var([1, 2, 3]))

# this is not all English stop words, just enough to process this quotation
stop_words = {'and', 'be', 'because', 'can', 'for', 'his', 'if', 'is', 'its',
              'more', 'of', 'or', 'than', 'the', 'they', 'to'}

mandela = """No one is born hating another person because of the color of his
skin , or his background , or his religion . People must learn to hate , and
if they can learn to hate , they can be taught to love , for love comes more
naturally to the human heart than its opposite ."""
output1 = '\n' in mandela
print('Is there a newline in mandela?', output1)
mandela = mandela.replace('\n', ' ')
mandela2 = mandela.split()
mandela2a = ' '.join(mandela2)
print('Are these the same value?', mandela == mandela2a)
print('Are these the same thing?', mandela is mandela2a)


def func1(a1):
    """Add docstring here."""
    # TODO Edit the docstring above to reflect the purpose of this function.
    # TODO Write a new function below this function that does the exact same
    # thing using only one list comprehension or one for loop. Test them to
    # be sure they function exactly the same.
    a2 = [q1 for q1 in a1 if q1 not in {',', '.', '?'}]
    a3 = [q1 for q1 in a2 if q1 not in stop_words]
    a4 = [q1.lower() for q1 in a3]
    return a4


mandela3 = func1(mandela2)
mandela4 = mandela3.count('love')
mandela5 = re.sub(r'\b(\w)is\b', r'\1er', mandela)
mandela6 = re.sub(r' ([,.])', r'\1', mandela5)
mandela7 = Counter(mandela2)
print('Top 5:', mandela7.most_common(5))

# TODO Write a regular expression below that will find words with the prefix
# ‘un’ or ‘in’ AND the suffix ‘able/ible’ (you may use pythex.org or
# regex101.com to test your expression). In the following text your regular
# expression should only match inimitable, untouchable and incomprehensible
# (but NOT unable):

x1 = """The inimitable Rogartis was unable to untie the untouchable unicorn
from the unicycle in the stable with incomprehensible magical powers."""
target_words = ['inimitable', 'untouchable', 'incomprehensible']
if all([w in x1 for w in target_words]):
    print('No typos in target_words!')
un_able_words = re.findall(r'YOUR REGEX HERE', x1)  # TODO write regex
print('Is the regex working? (should be True)', un_able_words == target_words)
print('Are these the same? (should be False)', un_able_words is target_words)

# TODO Many of the variables used in this module are not helpful. Rename all of
# the variables that have a number in them to better reflect the values stored
# in them. I recommend using Find/Replace, or your IDE's refactoring tools to
# avoid changing a name in one place, but not another. Make sure the script
# runs without errors after you change the names.
