import re

message = 'Is this a phone? 345-342-2341 and this 232-334-6666'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumberRegex.search(message)

print(matchObject.group())

listMatch = phoneNumberRegex.findall(message)

print(listMatch)


#same thing
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')

matchObject = phoneNumberRegex.search(message)

print(matchObject.group())

print(matchObject.group(1)) # output 345

print(matchObject.group(2)) # output 342

phoneNumberRegex = re.compile(r'\(\d\d\d\) (\d\d\d)-(\d\d\d\d)') # search litteraly for ( when \(

message = 'Is this a phone? (345) 342-2341 and this 232-334-6666'

matchObject = phoneNumberRegex.search(message)

print(matchObject.group())
print(matchObject.group(1)) # output 342

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')

message = 'Superman vs Batman on the Batmobile'
listMatch = batRegex.findall(message)

print(listMatch)

