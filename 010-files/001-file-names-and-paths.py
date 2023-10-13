
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

print(os.path.abspath('..\\..\\spam.png')) # C:\Users\Public\code\spam.png  # remove folders automate-with-python\\010-files

print(os.path.isabs('..\\..\\spam.png')) # False
print(os.path.isabs('C:\\Users\\Public\\code')) # True

print(os.path.relpath('C:\\folder1\\folder2\\folder3\\spam.png', 'C:\\folder1')) # output folder2\folder3\spam.png

print(os.path.dirname('C:\\folder1\\folder2\\folder3\\spam.png'))
print(os.path.basename('C:\\folder1\\folder2\\folder3\\spam.png'))

print(os.path.exists('C:\\Users\\Public\\code\\'))
print(os.path.exists('C:\\folder1\\folder2\\folder3\\'))
print(os.path.exists('C:\\windows\\system32\\calc.exe'))

print(os.path.isdir('C:\\windows\\system32\\calc.exe'))
print(os.path.isfile('C:\\windows\\system32\\calc.exe'))

print(os.path.getsize('C:\\windows\\system32\\calc.exe'))

print(os.listdir('C:\\Users\\Public\\code'))

totalSize = 0
for filename in os.listdir('C:\\windows\\system32\\'):
    if not os.path.isfile(os.path.join('C:\\windows\\system32\\', filename)):
        #print(os.path.isfile(os.path.join('C:\\windows\\system32\\', filename)))
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\windows\\system32\\', filename))
    #print(os.path.isfile(os.path.join('C:\\windows\\system32\\', filename)))

print(totalSize)

os.makedirs('C:\\Users\\Public\\code\\TEST1\\TEST2')