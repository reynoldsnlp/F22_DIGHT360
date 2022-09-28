"""One possible solution to assignment 5."""


def all_lines_from(filename):
    with open(filename) as f:
        return f.readlines()


def filter_lines_from(filename, filter):
    with open(filename) as f:
        # return [line for line in f if filter in line]  # list comprehension
        output_list = []
        for line in f:
            if filter in line:
                output_list.append(line)
    return output_list


def append_lines_to(filename, lines):
    with open(filename, 'a') as f:
        for line in lines:
            # print(line, file=f)
            f.write(line + '\n')


def overwrite_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            # print(line, file=f)
            f.write(line + '\n')


# 1.)
for line in all_lines_from('example.txt'):
    print(line, end='')  # customizing the end avoids extra newlines

# 2.)
for line in filter_lines_from('jokes.txt', 'Dracula'):
    print(line, end='')

# 3.)
my_jokes = ['A Parent  Q: When does a joke turn into a dad joke?  A: When it becomes apparent.',
            'Squak!!   Q: What’s orange and sounds like a parrot?  A: A carrot.'
            ]
append_lines_to('jokes.txt', my_jokes)

# 4.)
overwrite_file('myjoke_1.txt', my_jokes[:1])
overwrite_file('myjoke_2.txt', my_jokes[1:])
