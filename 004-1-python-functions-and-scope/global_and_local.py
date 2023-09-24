spam = 42

def eggs():
    spam = "hello 42"
    return spam

print(spam)
print(eggs())

def spam():
    eggs = 99
    bacon()
    print("spam eggs = " + str(eggs))

def bacon():
    ham = 101
    eggs = 0
    print("bacon eggs = " + str(eggs))
    print("bacon ham = " + str(ham))

spam()