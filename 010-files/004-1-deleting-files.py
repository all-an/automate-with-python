import os

print(os.getcwd())
print(os.path.isfile(os.path.join('C:\\Users\\Public\\code\\automate-with-python\\010-files\\', 'bacon.txt')))
print(os.path.isdir(os.path.join('C:\\Users\\Public\\code\\automate-with-python\\010-files\\', 'dir_tobe_copied')))

if not os.path.isdir(os.path.join('C:\\Users\\Public\\code\\automate-with-python\\010-files\\', 'dir_tobe_copied')):
    os.makedirs('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_tobe_copied')
    print('Dir created')

if not os.path.isfile(os.path.join('C:\\Users\\Public\\code\\automate-with-python\\010-files\\', 'bacon.txt')):
    hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\bacon.txt', 'w')
    hi_file.write('Hello Allan!') # if file do not exists, is created
    hi_file.close()
    print('File created')

    
os.unlink('bacon.txt') # delete file on getcwd() folder
print('File deleted')

os.rmdir('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_tobe_copied')
print('Dir deleted')

os.makedirs('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_tobe_copied')
print('Dir created')
hi_file = open('C:\\Users\\Public\\code\\automate-with-python\\010-files\\bacon.txt', 'w')
hi_file.write('Hello Allan!') # if file do not exists, is created
print('File created')

print(os.path.isfile(os.path.join('C:\\Users\\Public\\code\\automate-with-python\\010-files\\', 'bacon.txt')))

import shutil

if os.path.isdir(os.path.join('C:\\Users\\Public\\code\\automate-with-python\\010-files\\', 'dir_tree_todelete')):
    print('Dir tree deleting')
    shutil.rmtree('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_tree_todelete')