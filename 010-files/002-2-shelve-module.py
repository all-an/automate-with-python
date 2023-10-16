import shelve

shelf_file  = shelve.open('mydata')

shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']

shelf_file.close()

shelf_file  = shelve.open('mydata')
print(shelf_file['cats'])

print(list(shelf_file.keys())) # output ['cats']
print(list(shelf_file.values())) # output [['Zophie', 'Pooka', 'Simon']]

shelf_file.close()