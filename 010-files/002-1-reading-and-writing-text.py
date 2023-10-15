hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext.txt')

print(hi_file.read())

def open_file():
    global hi_file
    hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext.txt')

#hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext.txt')
open_file()
print(hi_file.read()) # cannot read two times

# hi_file.close()

#hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext.txt')
open_file()
content = hi_file.read()

print(content)
#hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext.txt')
open_file()
print(hi_file.read())


print('----------read lines ----------------')
open_file()
#hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext.txt')

print(hi_file.readlines()) # output ['hello world\n', 'how are you']

hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext2.txt', 'w')
hi_file.write('Hello Allan!')

hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\002-plaintext.txt', 'w')
hi_file.write('Hello Allan!') # if file do not exists, is created

hi_file = open('bacon.txt', 'a')
hi_file.write('bacon is not a vegetable\n')
hi_file.write('bacon is delicious')
hi_file.close()

import os

print(os.getcwd())