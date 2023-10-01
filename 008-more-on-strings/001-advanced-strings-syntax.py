print("hello there\nHow are you\nI'm fine")

#print raw string

print(r'That\'s carol\'s cat')


print("""
    I am the knight
     and I will defeat
      the dragon.
      """)

spam = """
    I am the knight
     and I will defeat
      the dragon.
      """

print(len(spam))

print('dragon' in spam)

print(spam[1:15])
print(spam[-16])

name1 = " bob "
name2 = " alice "

print(" Does " + name2 + ' loves ' + name1 + ' ?')

print("Hello %s and %s" % (name1, name2))