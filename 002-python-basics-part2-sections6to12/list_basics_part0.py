
spam = ['software', 'testing']

def p(myVar):
    print(myVar)

print(spam[0])

for item in spam:
    print(item)

foo = [['python', 'c'], 'sql']

print(foo[0][1])
print(foo[-1])
print(foo[-2])

bar = ['the', 'elephant', 'is', 'afraid']
print(bar[1:3])
print(bar[1:])

bar[2] = 'was'

print(bar)

bar[1:3] = ['cat', 'is']

print(bar)

spam = ['cat', 'bat', 'rat', 'elephant', 'dog']

print(spam[:2])

print(spam)
del spam[2]
print(spam)

p(len('Hello'))
p(len([1,2,3]))

p([1,2] * 5)

spam = ['cat', 'bat', 'rat', 'elephant', 'dog']

p('cat' in spam)