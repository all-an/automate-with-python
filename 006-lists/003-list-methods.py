from random_word import *

r = RandomWords()
r.get_random_word()

myList2 = []

for i in range(1,5):
    myList2.append(r.get_random_word())
    #print(r.get_random_word())

print(myList2)

print(myList2[3])

print(myList2.index(myList2[3]))

print('-----------------------------------')

for i in myList2[0]:
    print(i)

print('-----------------------------------')

myList2.append(r.get_random_word())

print(myList2)

myList2.insert(1, r.get_random_word())

print(myList2)

del myList2[0]

print(myList2)

myNums = [43, 34, 0.9, -43, -4]

myNums.sort()

print(myNums)

spam = ['I', 'J', 'b', 'a']

spam.sort()

print(spam)

spam.sort(key=str.lower)

print(spam)