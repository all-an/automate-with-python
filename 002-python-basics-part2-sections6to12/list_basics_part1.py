
my_string = 'Hello Python'

print(list(my_string))

hello_list = list(my_string)

print(my_string[0])
print(my_string[1:3])
print(my_string[-2])

print('Hell' in my_string)

print('Test' in my_string)

for char in my_string:
    print(char)

# my_string[0] = '3'

new_string = my_string[0:6] + 'Nim'

print(new_string)

print(tuple('python'))

spam = [0,1,2]
cheese = spam
cheese[1] = 'hello'

print(spam)

spam = (0,1,2)
cheese = spam
# cheese[1] = 'hello'

spam = (1,2)

print(cheese)