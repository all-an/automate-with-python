import os, shutil

dir_to_walk = os.walk('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_to_walk')

for folder_name, subfolders, filenames in dir_to_walk:
    print("FOLDER: " + folder_name)
    print("SUBFOLDERS: " + str(subfolders))
    print("FILENAMES: " + str(filenames))
    print("---------------------------------------------------")
    for sub_folder in subfolders:
        if 'fish' in sub_folder:
            shutil.rmtree(folder_name + '\\' + sub_folder)

        for file in filenames:
            if file.endswith('.py'):
                shutil.copy(os.join(folder_name, file), os.join(folder_name, file + '.backup'))
                # os.unlink(folder_name + '\\' + file)
            