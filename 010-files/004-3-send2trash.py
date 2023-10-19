import send2trash, os

if os.path.isfile(os.path.join('C:\\Users\\Public\\code\\automate-with-python\\010-files\\', 'important-file.txt')):
    send2trash.send2trash('C:\\Users\\Public\\code\\automate-with-python\\010-files\\important-file.txt')