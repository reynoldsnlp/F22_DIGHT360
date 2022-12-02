# Visualizations with `matplotlib.pyplot`

All of the following code will only work in a gui environment. In other words,
if you are connected to a remote machine through the terminal (pythonanywhere,
kaggle, Google Colab, ssh, etc.), that machine has no way to open a new window
to show you the generated image. However, you can save image files by using the
following idiom instead of `plt.show()`:

```python
>>> fig = plt.gcf()  # get current figure
>>> fig.savefig('filename.png')
>>> plt.clf()  # clear plot (only necessary if you need to make more images)
```

The following code is adapted from this website:
https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py

## drawing simple line

```python
import matplotlib.pyplot as plt  # $ python3 -m pip install --user matplotlib
seq = [1, 2, 3, 4, 5, 6]
plt.plot(seq)  # x is assumed to be range(len(seq)), y is seq
plt.ylabel('some numbers')
plt.show()
```

## drawing parabolic line

```python
import matplotlib.pyplot as plt
seq2 = [i ** 2 for i in seq]
plt.plot(seq, seq2)  # seq is x, seq2 is y
plt.show()
```


`PRACTICE A`

Write a new list `myseq` and try generating plots. Change the numbers to higher
and lower values. Use more or fewer numbers. Play around until you are
comfortable drawing line graphs.


## Plotting points using custom marking shape/line/color

For all marker formatting options, see
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

```python
import matplotlib.pyplot as plt
plt.plot(seq, seq2, 'ro')  # r = red; o = circle
plt.axis([0, 10, 0, 100])  # Usually automatic axis lengths are best; this is just an example of how to change it if needed.
plt.show()
```


`PRACTICE B`

Use different combinations of marker formatting on the website shown above.
Draw lines and dots of different colors and shapes. Tinker.


## Drawing multiple series using various shapes/colors


You can `plot` multiples series all at once...

```python
import matplotlib.pyplot as plt
seq3 = [i ** 3 for i in seq]
plt.plot(seq, seq, 'r--', seq, seq2, 'bs', seq, seq3, 'g^')
plt.show()
```

...or one at a time, before calling `plt.show()`... (I think this is more
readable)

```python
import matplotlib.pyplot as plt
seq = [1, 2, 3, 4, 5, 6]
seq2 = [i ** 2 for i in seq]
seq3 = [i ** 3 for i in seq]
plt.plot(seq, seq, 'r--')
plt.plot(seq, seq2, 'bs')
plt.plot(seq, seq3, 'g^')
plt.show()
```



`PRACTICE C`

To plot points, we need one sequence of all the x values and one sequence of
all the y values. Let's practice wrangling data to the format we need. The
built-in `zip` function and splat syntax are our friends. Remember that using
the splat syntax (`*`) with `zip` is the inverse of `zip`.

```python
print(seq)
# [1, 2, 3, 4, 5, 6]
print(seq2)
# [1, 4, 9, 16, 25, 36]
zipped = list(zip(seq, seq2))
print(zipped)
# [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
unzipped = list(zip(*zipped))
print(unzipped)
# [(1, 2, 3, 4, 5, 6), (1, 4, 9, 16, 25, 36)]
```

Finish the following script by using `zip` on `c.most_common()` to plot the
frequencies of the words in this quotation.


```python
from collections import Counter
vote = 'Not voting is not a protest . It is a surrender .'.split()
print(vote)
# ['Not', 'voting', 'is', 'not', 'a', 'protest', '.', 'It', 'is', 'a', 'surrender', '.']
c = Counter(vote)  # dictionary
print(c)
# Counter({'is': 2, 'a': 2, '.': 2, 'Not': 1, 'voting': 1, 'not': 1, 'protest': 1, 'It': 1, 'surrender': 1})
print(c.most_common())
# [('is', 2), ('a', 2), ('.', 2), ('Not', 1), ('voting', 1), ('not', 1), ('protest', 1), ('It', 1), ('surrender', 1)]
...
```

You can use `plt.xticks(fontsize=10, rotation='vertical')

## drawing barplot, scatterplot, and boxplots

```python
import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.bar(names, values)
plt.show()

plt.scatter(names, values)
plt.show()

plt.plot(names, values)
plt.show()

plt.boxplot([1, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 11])
plt.show()

plt.boxplot([[1, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 11],
             [1, 1, 1, 1, 1, 2, 2, 2, 4, 7, 8, 9, 13]])
plt.show()
```


## drawing a histogram

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate a normal distribution
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)  # x is a list of random numbers in a normal distribution

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
print(n)
print(bins)
print(patches)

# add some text
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```
