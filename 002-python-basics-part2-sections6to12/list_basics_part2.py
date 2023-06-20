
list_range = [0,9,8,4]

for i in list_range:
    print(i)

print(list(list_range))
print(list_range)

great_range = list(range(0, 100, 2))

print(great_range)

a = 'AAA'
b = 'BBB'

a, b = b, a

print(a)
print(b)

spam = ['software', 'testing', 'tech']

print(spam.index('testing'))

spam.insert(1, 'python')

print(spam)

spam.append('nim')

print(spam)

spam = ['python', 'nim', 'nim', 'python', 'julia']

spam.remove('python')

print(spam)

spam.sort()

print(spam)

spam = ['python', 'nim', 'nim', 'python', 1]

# spam.sort()

print(spam)

foo = ['list', 'My']

foo.sort()

print(foo)

foo.sort(key=str.lower)

print(foo)