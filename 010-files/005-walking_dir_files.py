import os

dir_to_walk = os.walk('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_to_walk')

for folder_name, subfolders, filenames in dir_to_walk:
    print("FOLDER: " + folder_name)
    print("SUBFOLDERS: " + str(subfolders))
    print("FILENAMES: " + str(filenames))
    print("---------------------------------------------------")