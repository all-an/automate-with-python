
print(list("hi allan"))

name = "Allan"

print(name[0])

print(name[1:3])

print(name[-2])

print('all' in name)
print('All' in name)

for letter in name:
    print(letter)

name = "I live in Europe"

# name[1] = 'x' # name is immutable

print(name)

name = 'Zophie a cat'

new_name = name[0:7] + 'the' + name[8:12]

print(name)
print(new_name)
print(name[8])

spam = 42
cheese = spam ## pass by value , so is a different 42
spam = 100

print(cheese)
print(spam)

my_list = [0,1,2,3,4,5]

cheese = my_list # pass by reference so changing a value change another , referencing the same list
cheese[0] = 42
print(cheese)
print(my_list)

def eggs(some_parameter):
    some_parameter.append('Hello')

spam = [1,2,3]

eggs(spam) # change spam outside scope because of the passing by reference

print(spam)

import copy

my_spam = ['x', 'y', 'z']

my_eggs = copy.deepcopy(my_spam)

my_spam.append("Hellow")

print(my_eggs)
print(my_spam)

my_fruits = ['apples',
             'oranges',
             'bananas']

print('Just testing the line continuation ' + \
      ' in python.' )