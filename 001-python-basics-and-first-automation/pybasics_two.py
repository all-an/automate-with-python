
print(bool(""))

print(bool(42))

spam = 0

while spam < 5:
    print("hello spam")
    spam = spam + 1

name = ''

while name != 'allan':
    print('Please type your name: ')
    name = input()

print('Thank you!')
    
spam_two = 0
while spam_two < 5:
    spam_two = spam_two + 1
    if spam_two == 3:
        continue
    print('spam is ' + str(spam_two))
