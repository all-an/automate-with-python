import re

namesRegex = re.compile(r'Agent \w+')

message = 'Agent Scully works with Agent Mulder'

print(namesRegex.findall(message))
#output ['Agent Scully', 'Agent Mulder']

print(namesRegex.sub('Agent Smith', message)) #output Agent Smith works with Agent Smith

print(message) # not modified

namesRegex = re.compile(r'Agent (\w)\w*') # * means zero or more

print(namesRegex.findall(message))
#output ['S', 'M']

print(namesRegex.sub(r'Agent \1****', message)) # \1 means group 1 (\w)
#output Agent S**** works with Agent M****

# verbose mode:

verbose_regex = re.compile(r'''
\d\d\d   # area code
-        # first dash
\d\d\d   # first three digits
-        # second dash
\d\d\d\d # last four digits                                              
''', re.VERBOSE)

message = """
'Is this a phone? 345-342-2341 and this 232-334-6666'
"""

match = verbose_regex.findall(message)
print(match)

verbose_regex = re.compile(r'''
(\d\d\d-)|   # area code
(\(\d\d\d)   # first three digits
-            # second dash
\d\d\d\d     # last four digits 
\sx\d{2,4}   # extension like x1234                                                                     
''', re.I | re.DOTALL | re.VERBOSE)

message = """
'Is this a phone? 345-342-2341 and this 232-334-6666'
"""

match = verbose_regex.findall(message)
print(match)