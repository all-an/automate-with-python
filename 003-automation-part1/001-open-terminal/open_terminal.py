import os
from os.path import exists

os.system("echo 'hello world'")

# 003-automation-part1/001-open-terminal/

os.system("python 003-automation-part1/001-open-terminal/open_terminal2.py")

file_exists = exists("003-automation-part1/001-open-terminal/cli")

print(file_exists)

if not file_exists:
    print("try build nim again")
    os.system("nim c -r --verbosity:0 003-automation-part1/001-open-terminal/cli.nim test1 test2")

os.system("003-automation-part1/001-open-terminal/cli test1 test2")

#os.system("ls -l")