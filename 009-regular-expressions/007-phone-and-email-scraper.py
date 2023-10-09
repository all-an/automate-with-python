import re, pyperclip

# regex for phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
           
((\d\d\d)|(\(\d\d\d)))?    # area code (optional)
(\s|-)                     # first separator, space or dash
-                          # separator
\d\d\d\d                   # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part (optional)
(\d{2,5}))?                  # extension number-part (optional)
           
''', re.VERBOSE)

# TODO regex for the email part

emailRegex = re.compile(r'''


''', re.VERBOSE)