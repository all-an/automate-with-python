
fictional_filepath = 'c:\\spam\\eggs.png'

print(fictional_filepath) # c:\spam\eggs.png

print('\\') # \

print(r'c:\spam\eggs.png')

print('\\'.join(['folder1', 'folder2', 'filename.png']))

import os

print('-------------------------------with os module ----------------------------------')

print(os.path.join('folder1', 'folder2', 'filename.png'))

print(os.sep)

print(os.getcwd()) # current working

os.chdir('C:\\') # change working dir to C:\

print(os.getcwd()) # current working

print(os.path.abspath('spam.png')) # C:\spam.png

os.chdir('C:\\Users\\Public\\code\\automate-with-python\\010-files')

print(os.path.abspath('..\\..\\spam.png')) # C:\Users\Public\code\spam.png

print(os.path.isabs('..\\..\\spam.png')) # False
print(os.path.isabs('C:\\Users\\Public\\code')) # True