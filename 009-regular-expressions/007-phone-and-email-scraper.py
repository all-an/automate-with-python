import re, pyperclip

# regex for phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(       
((\d\d\d)|(\(\d\d\d))?    # area code (optional)
(\s|-)                     # first separator, space or dash
\d\d\d                        
-                          # separator
\d\d\d\d                   # last 4 digits
(((ext(\.)?\s)|x)           # extension word-part (optional)
(\d{2,5}))?                  # extension number-part (optional)
)    
''', re.VERBOSE)

# regex for the email part

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# get the text from clipboard

# just copy the text in the file 007-txt-email-and-phones
text = pyperclip.paste()

#print(text)

matchPhone = phoneRegex.findall(text)
matchEmail = emailRegex.findall(text)


allPhoneNumbers = []
for phoneNumber in matchPhone:
    allPhoneNumbers.append(phoneNumber[0])

    
print(allPhoneNumbers)
print(matchEmail)

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(matchEmail)

print(results)

pyperclip.copy(results)

