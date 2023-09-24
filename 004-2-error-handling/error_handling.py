def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divid by zero')

print(div42by(0))
print(div42by(1))

# value error

print('How many cats do you have (enter a digit number) ?')
num_cats = input()
try:
    if int(num_cats) > 4:
        print("That's a lot of cats")
    else:
        print('That is not that many cats')
except ValueError:
    print('Non digit numbers are not allowed. Please enter a digit number')