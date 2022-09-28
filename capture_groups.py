import re


data = 'Age: 43, Phone number: 888-666-4444.'
digits = re.findall(r'\d+', data)
print(digits)

age = re.findall(r'Age: \d+', data)
print(age)

age = re.findall(r'Age: (\d+)', data)
print(age)

# Using capture group to exclude a specific match from a more general match
# Match everything but dog
matches = re.findall(r'dog|(\w+)', 'hog log dog')
print(matches)
