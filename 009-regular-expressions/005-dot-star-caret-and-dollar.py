import re

beginsWithHelloRegex = re.compile(r'^Hello') # ^ without [ means Hello appearing at start of string

match = beginsWithHelloRegex.search('Hello world!')

print(match)

endsWithWorldRegex = re.compile(r'world$') # $ means ends with world word

match = endsWithWorldRegex.search('hello world')

print(match)

match = endsWithWorldRegex.search('hello world planet')

print(match) # will print None

allHelloREgex = re.compile(r'^Hello$') # all string must be the world Hello

match = allHelloREgex.search('Hello')

print(match)

match = allHelloREgex.search('Hello1') # output None

print(match)

allDigitsREgex = re.compile(r'^\d+$') # all string must be the digits

match = allDigitsREgex.search('123987959')

print(match)

match = allDigitsREgex.search('1239879-HELLO-59')

print(match)

anythingDotWordRegex = re.compile(r'.at') # dot means any character followed by at

match = anythingDotWordRegex.findall('manat cow avat alkj uat')

print(match) # output ['nat', 'vat', 'uat']

anythingDotWordRegex = re.compile(r'.{1,2}at') # dot means any character followed by at {1,2} range

match = anythingDotWordRegex.findall('manat cow avat alkj uat')

print(match) # output ['anat', 'avat', ' uat']