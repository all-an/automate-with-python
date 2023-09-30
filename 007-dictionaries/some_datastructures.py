import pprint

class Format:
    end = '\033[0m'
    underline = '\033[4m'

cat = {
    'name': 'Zophie',
    'age': 7,
    'color': 'gray'
}

allCats = []

allCats.append(cat)
allCats.append({
    'name': 'Pooka',
    'age': 5,
    'color': 'gray'
})

def myprint(something):
    pprint.pprint(something)

myprint(allCats)

the_board = {
    'low-L': ' ',
    'low-M': ' ',
    'low-R': ' ',
    'mid-M': '_',
    'mid-L': '_',
    'mid-R': '_',
    'top-L': '_',
    'top-M': '_',
    'top-R': '_',
}

myprint(the_board)

the_board['low-M'] = 'X'
the_board['mid-M'] = Format.underline + 'X' + Format.end

myprint(the_board)

def printBoard(board):
    print(Format.underline + '       ' + Format.end)
    print('|' + board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
    print('|' + board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '|')
    print(Format.underline + '|' + board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '|' + Format.end)

printBoard(the_board)



print()

print("\u0332".join('X'))

print(type(the_board))