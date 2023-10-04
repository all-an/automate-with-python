import re

batRegex = re.compile(r'Bat(wo)?man') # (thisgroup)? can appear 1 or zero times

match = batRegex.findall('The Adventures of Batman and Batwoman')

print(match)

match = batRegex.search('The Adventures of Batwoman')

print(match.group())

message = 'Is this a phone? 345-342-2341 and this 232-334-6666'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumberRegex.search(message)

print(matchObject.group())

message = 'Is this a phone? 345--2341 and this 232-334-'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumberRegex.search(message)

print(matchObject == None)

message = 'Is this a phone? 345--2341 and this 232-334-'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d(-\d\d\d\d)?')

matchObject = phoneNumberRegex.search(message)

print(matchObject.group()) # returns 232-334 because this part is optional ?: (-\d\d\d\d)?

# re.compile(r'dinner\?') # in this case we look for the word dinner including the ?

batRegex = re.compile(r'Bat(wo)*man') # * means wo can appear zero or many times

match = batRegex.search('The Adventures of Batman and Batwoman')

print(match)

match = batRegex.search('The Adventures of Batwoman')

print(match)

match = batRegex.search('The Adventures of Batwowowowowowoman')

print(match)

batRegex = re.compile(r'Bat(wo)+man') # + means wo can appear zero or many times

match = batRegex.search('The Adventures of Batman and Batman')

print(match) # output None

my_regex = re.compile(r'\+\*\?') # searching for the signs after the \

my_match = my_regex.search('I learn about +*? syntax')

print(my_match)

my_regex = re.compile(r'(\+\*\?)+') # searching for the signs after the \

my_match = my_regex.search('I learn about +*?+*?+*?+*?+*? syntax')

print(my_match.group())

ha_regex = re.compile(r'(Ha){3}') # looking for Ha 3 times

ha_match = ha_regex.search('He said HaHaHa')

print(ha_match)

message = 'phone numbers:    345-342-2341,232-334-6666,334-6444'

phoneNumberRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}') # ? optional group zero or 1 times, and 3 phone numbers {3}

matchObject = phoneNumberRegex.search(message)

print(matchObject)

ha_regex = re.compile(r'(Ha){3,8}') # looking for Ha 3 to 8 times

ha_match = ha_regex.search('He said HaHaHa')

print(ha_match)

ha_match = ha_regex.search('He said HaHaHaHaHaHa')

print(ha_match)

digitRegex = re.compile(r'(\d){3,5}') # any digit from 3 to 5 times
match = digitRegex.search('1234576564') 
print(match) #greedy will match the maximum

digitRegex = re.compile(r'(\d){3,5}?') # any digit from 3 to 5 times nongreedy
match = digitRegex.search('1234576564') 
print(match) # nongreedy will match the minimum
