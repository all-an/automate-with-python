import shutil

shutil.copy('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_tobe_copied\\spam.txt', 'C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_to_copy\\renamed_spam.txt')

shutil.copytree('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_tobe_copied', 'C:\\Users\\Public\\code\\automate-with-python\\010-files\\backup_dir_to_copy')

shutil.move('C:\\Users\\Public\\code\\automate-with-python\\010-files\\dir_tobe_copied\\spam.txt', 'C:\\Users\\Public\\code\\automate-with-python\\010-files\\backup_dir_to_copy\\backup_spam.txt')

