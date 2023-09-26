spam = ['cat', 'bat', 'rat', 'elephant']

print(spam)

print(spam[0])

print(spam[0][1])

myList1 = ['one', ['two', 'three'], 'four']

print(myList1[1][0])

print(spam[-1])
print(spam[-2])

print(spam[1:3])

spam2 = [10, 20, 30]

spam2[1] = "hello"

print(spam2)

spam2[1:3] = ['cat', 'dog', 'mouse']

print(spam2)

import requests

from random_word import *
r = RandomWords()

# Return a single random word
r.get_random_word()
""" # Return list of Random words
r.get_random_words()
# Return Word of the day
r.word_of_the_day() """

myList2 = []

for i in range(1,5):
    myList2.append(r.get_random_word())
    print(r.get_random_word())

print(myList2)

print(myList2[:2])
print(myList2[1:])
      
del myList2[2]
print(myList2)

print(myList2[0] in myList2)
print('allan' in myList2)
print('allan' not in myList2)

#print(WORDS)
