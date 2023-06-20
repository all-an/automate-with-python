
my_cat = {'size': 'fat', 'color': 'gray', 'hungry': True}
my_cat2 = {'color': 'gray', 'hungry': True,'size': 'fat'}

print(my_cat['hungry'])

if my_cat['hungry']:
    print('Give food')

print(my_cat == my_cat2) # True

message = 'My cat has ' + my_cat['color'] + ' fur.'

print(message)

print('size' in my_cat) # True
print('size' not in my_cat) # False
print('fat' in my_cat) # False because in compare keys
print('fat' in my_cat.values()) # True because in compare values now

print(my_cat.values())
print(my_cat.keys())

print(list(my_cat.values()))
print(list(my_cat.keys()))
