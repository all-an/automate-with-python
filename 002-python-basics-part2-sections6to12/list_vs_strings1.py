import copy

def eggs(cheese):
    cheese.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

my_cheese = copy.deepcopy(spam)
my_cheese[1] = 42
print(spam)
print(my_cheese)

fruits = ['apple',
          'orange',
          'banana']

print(fruits)


# ignore identation
print('Four score and seven' + \
      ' years ago')

