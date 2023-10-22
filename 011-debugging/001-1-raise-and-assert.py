# the raise and assert statements

# raise Exception('Allan error message')


"""
function that creates a box:

********
*      *
*      *
********

"""
def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('First parameter symbol must be len 1')
    if (width < 2) or (height < 2):
        raise Exception('Width and height must be greater than or equal 2')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

box_print('*', 8, 4)
box_print('#', 1, 40)
box_print('*#', 80, 40)
