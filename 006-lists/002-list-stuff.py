for i in range(4):
    print(i)

print("-----------------------------")

for i in [0,8,38,"hello"]:
    print(i)

print(list(range(42)))

print(list(list(range(0, 14, 4))))

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

for i in range(len(myList2)):
    print('item in index: ' + str(i) + ' is ' + myList2[i])

word1, word2, word3, word4 = myList2

print(word1)

str = myList2[0]
 
globals()[str] = myList2[3]
print(myList2[0])

a = 'AAA'
b = 'BBB'

a , b = b , a

print(b)

spam = 41

print(spam)

spam += 1

print(spam)