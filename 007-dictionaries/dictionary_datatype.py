
my_kingdom = {
    'name': 'Kingdom of Touvnia',
    'language': 'English',
    'king': 'King Jon',
    1: 'some value'
}

print(my_kingdom['king'])

print('This kingdom: ' + my_kingdom['name'] + ' is great.')

print(my_kingdom[1])

print([1,2,3] == [3,2,1]) # order matters for lists

print({'first':1, 'second':2, 'third':3} == {'third':3, 'first':1, 'second':2}) # orders do not matters in dictionaries

# print(my_kingdom['allan']) # error

print('language' in my_kingdom)

print(list(my_kingdom.keys()))
print(list(my_kingdom.values()))

print(my_kingdom.keys())

for k in my_kingdom.keys():
    print(k)

print(my_kingdom.items())

for i in my_kingdom.items():
    print(i)

if 'language' in my_kingdom:
    print(my_kingdom['language'])

print(my_kingdom.get('language', 'Portuguese')) # 'Portuguese' is the default

print(my_kingdom.get('color', 'black'))

if 'color' not in my_kingdom:
    my_kingdom['color'] = 'Black'

print(my_kingdom['color'])

my_kingdom.setdefault('color', 'Blue')

print(my_kingdom)

my_kingdom['color'] = 'Blue'

print(my_kingdom)

