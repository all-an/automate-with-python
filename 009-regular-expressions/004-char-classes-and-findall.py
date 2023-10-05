import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

message = """
'Is this a phone? 345-342-2341 and this 232-334-6666'
"""

print(phoneRegex.search(message)) # first match:  <re.Match object; span=(19, 31), match='345-342-2341'>

print(phoneRegex.findall(message)) # output: ['345-342-2341', '232-334-6666']

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

print(phoneRegex.findall(message)) # output: [('345', '342-2341'), ('232', '334-6666')]

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')

print(phoneRegex.findall(message)) # output: [('345-342-2341', '345', '342-2341'), ('232-334-6666', '232', '334-6666')]

my_string = "Allan6Allan"

digit_regex = re.compile(r'\d')

print(digit_regex.findall(my_string))

digit_regex = re.compile(r'(0|1|2|3|4|5|6)')

print(digit_regex.findall(my_string))

song = """
A partridge in a pear tree on each of the 12 days: 1 x 12 = 12
Two turtle doves on the last 11 days: 2 x 11 = 22
Three French hens on the last 10 days: 3 x 10 = 30
Four calling birds on the last 9 days: 4 x 9 = 36
Five gold rings on the last 8 days: 5 x 8 = 40
Six geese a-laying on the last 7 days: 6 x 7 = 42
Seven swans a-swimming on the last 6 days: 7 x 6 = 42
Eight maids a-milking on the last 5 days: 8 x 5 = 40
Nine ladies dancing on the last 4 days: 9 x 4 = 36
Ten lords a-leaping on the last 3 days = 10 x 3 = 30
11 pipers piping on the last 2 days = 11 x 2 = 22
12 drummers drumming on the last day = 12 x 1 = 12
"""

xmas_regex = re.compile(r'\d+\s\w+') # \d+ = one or more, \s for space or a true space, \w+ one word characters or more

print(xmas_regex.findall(song))

vowel_regex = re.compile(r'[aeiouAEIOU]') 

print(vowel_regex.findall(song))

print('-----------------------------------------------------------------------------------------')

char_regex = re.compile(r'[a-fA-F]') 

print(char_regex.findall(song))

print('-----------------------------------------------------------------------------------------')

char_regex = re.compile(r'[^aeiouAEIOU]') # ^ is the equivalent to not

print(char_regex.findall(song))

"""
output:
['\n', ' ', 'p', 'r', 't', 'r', 'd', 'g', ' ', 'n', ' ', ' ', 'p', 'r', ' ', 't', 'r', ' ', 'n', ' ', 'c', 'h', ' ', 'f', ' ', 't', 'h', ' ', '1', '2', ' ', 'd', 'y', 's', ':', ' ', '1', ' ', 'x', ' ', '1', '2', ' ', '=', ' ', '1', '2', '\n', 'T', 'w', ' ', 't', 'r', 't', 'l', ' ', 'd', 'v', 's', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '1', '1', ' ', 'd', 'y', 's', ':', ' ', '2', ' ', 'x', ' ', '1', '1', ' ', '=', ' ', '2', '2', '\n', 'T', 'h', 'r', ' ', 'F', 'r', 'n', 'c', 'h', ' ', 'h', 'n', 's', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '1', '0', ' ', 'd', 'y', 's', ':', ' ', '3', ' ', 'x', ' ', '1', '0', ' ', '=', ' ', '3', '0', '\n', 'F', 'r', ' ', 'c', 'l', 'l', 'n', 'g', ' ', 'b', 'r', 'd', 's', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '9', ' ', 'd', 'y', 's', ':', ' ', '4', ' ', 'x', ' ', '9', ' ', '=', ' ', '3', '6', '\n', 'F', 'v', ' ', 'g', 'l', 'd', ' ', 'r', 'n', 'g', 's', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '8', ' ', 'd', 'y', 's', ':', ' ', '5', ' ', 'x', ' ', '8', ' ', '=', ' ', '4', '0', '\n', 'S', 'x', ' ', 'g', 's', ' ', '-', 'l', 'y', 'n', 'g', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '7', ' ', 'd', 'y', 's', ':', ' ', '6', ' ', 'x', ' ', '7', ' ', '=', ' ', '4', '2', '\n', 'S', 'v', 'n', ' ', 's', 'w', 'n', 's', ' ', '-', 's', 'w', 'm', 'm', 'n', 'g', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '6', ' ', 'd', 'y', 's', ':', ' ', '7', ' ', 'x', ' ', '6', ' ', '=', ' ', '4', '2', '\n', 'g', 'h', 't', ' ', 'm', 'd', 's', ' ', '-', 'm', 'l', 'k', 'n', 'g', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '5', ' ', 'd', 'y', 's', ':', ' ', '8', ' ', 'x', ' ', '5', ' ', '=', ' ', '4', '0', '\n', 'N', 'n', ' ', 'l', 'd', 's', ' ', 'd', 'n', 'c', 'n', 'g', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '4', ' ', 'd', 'y', 's', ':', ' ', '9', ' ', 'x', ' ', '4', ' ', '=', ' ', '3', '6', '\n', 'T', 'n', ' ', 'l', 'r', 'd', 's', ' ', '-', 'l', 'p', 'n', 'g', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '3', ' ', 'd', 'y', 's', ' ', '=', ' ', '1', '0', ' ', 'x', ' ', '3', ' ', '=', ' ', '3', '0', '\n', '1', '1', ' ', 'p', 'p', 'r', 's', ' ', 'p', 'p', 'n', 'g', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', '2', ' ', 'd', 'y', 's', ' ', '=', ' ', '1', '1', ' ', 'x', ' ', '2', ' ', '=', ' ', '2', '2', '\n', '1', '2', ' ', 'd', 'r', 'm', 'm', 'r', 's', ' ', 'd', 'r', 'm', 'm', 'n', 'g', ' ', 'n', ' ', 't', 'h', ' ', 'l', 's', 't', ' ', 'd', 'y', ' ', '=', ' ', '1', '2', ' ', 'x', ' ', '1', ' ', '=', ' ', '1', '2', '\n']
"""

print('-----------------------------------------------------------------------------------------')

char_regex = re.compile(r'[^aeiouAEIOU]') # ^ is the equivalent to not

print(char_regex.findall(song))