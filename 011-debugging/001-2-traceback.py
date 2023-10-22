import traceback, os

import datetime

e = datetime.datetime.now()

try:
    raise Exception('Allan error message')
except:
    errorFile = open('error-log.txt', 'a')
    errorFile.write("\n--------------------------------Current date and time = %s" % e)
    errorFile.write('\n' + traceback.format_exc())
    errorFile.close()
    print('Error message was printed to error-log.txt file')

print(os.getcwd())