def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False #not area code
    if text[3] != '-':
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first three digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # no three digits
    else: 
        return True

print(isPhoneNumber('123-444-0093'))

print(isPhoneNumber('hello'))

#foundNumber = False

def findPhoneNumber(sentence):
    foundNumber = False
    for i in range(len(sentence)):
        partition = sentence[i:i+12]
        if isPhoneNumber(partition):
            print('Phone number found: ' + partition)
            foundNumber = True
    if not foundNumber:
        print('Could not find any phone number')


findPhoneNumber('Is this a phone number, 322-234-2341')
findPhoneNumber('Not number here')