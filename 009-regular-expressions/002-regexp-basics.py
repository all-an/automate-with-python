import re

message = 'Is this a phone? 345-342-2341 and this 232-334-6666'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumberRegex.search(message)

print(matchObject.group())

listMatch = phoneNumberRegex.findall(message)

print(listMatch)