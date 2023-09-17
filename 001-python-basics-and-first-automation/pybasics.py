
print('Hello world')
print('What is your name?')
myName = input()
print("It's good to meet you " + myName)
print("The length of your name is: " + str(len(myName)))
print("What is your age? ")
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

def hello(name):
    print('Hello ' + name)
    print('Goodbye ' + name)
    print('Name ' + name + ' has ' + str(len(name)) + ' letters in it.')

hello('Alice')
hello('Bob')

def plusNumber(myNumber, plusNumber):
    print('my number: ' + str(myNumber) + ' plus number: '  + str(plusNumber) + ', equals: ' + str(myNumber + plusNumber))

plusNumber(4, 5)

spam = print()

print(type(spam))

print('Hello ', end='')
print('World')

print('Hello ')
print('World')

print('cat', 'dog')

