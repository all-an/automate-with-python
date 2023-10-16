import os

os.chdir('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dry_run_files')

""" for filename in os.listdir():
    if filename.endswith('.rxt'):
        print(filename) """

for filename in os.listdir():
    if filename.endswith('.txt'):
        os.unlink(filename)

print(os.getcwd())