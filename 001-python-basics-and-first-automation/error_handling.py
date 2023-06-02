
def div42by(divisor):
    try:
        print(42 / divisor)
    except ZeroDivisionError:
        print('Error you try to divide by zero')

div42by(0)

print('How much are the mangos')


howMuch = input()


try:
    if int(howMuch) >= 4:
        print('That is expensive')
    else:
        print('That is cheap')
except ValueError:
    print('Please type only numbers')

