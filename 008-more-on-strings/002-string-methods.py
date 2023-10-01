
spam = "hello world"
spam.upper()

print(spam)

spam = spam.upper()

print(spam)

print(spam.lower())

print(spam) # strings are immutable

answer = input()
answer = answer.lower()
print(answer)

print(answer.islower())
print(answer.isupper())

print('HELLO'.isupper())

print('is hello alpha: ' + str('hello'.isalpha()))

print('is hello123 alpha: ' + str('hello123'.isalpha()))

print('is hello123 alnum: ' + str('hello123'.isalnum()))

print('is 123 isdecimal: ' + str('123'.isdecimal()))

print("is 'hello world'[5] space: " + str('hello world'[5].isspace()))

print("is 'My Title' a title: " + str('My Title'.istitle()))

print("is 'My Title' a title: " + str('My Title'.startswith('M')))

print("is 'My Title' a title: " + str('My Title'.startswith('My')))

print(','.join(['cats','bats','rats'])) # output> cats,bats,rats

print('\n\n'.join(['cats','bats','rats']))

print('My name is Allan'.split())

print('Hello'.rjust(20)) 

print('Hello'.rjust(20, '*')) 

print('Hello'.ljust(20, '-'))

print('Hello'.center(50, '*'))

print('    HelloX'.strip())

word = 'SpamSpamAllanSpamHelloSpamSpam'.strip('ampS') 

print(word) # output AllanSpamHello

spam = 'hello there'

spam = spam.replace('e', '123')

print(spam) # output h123llo th123r123
