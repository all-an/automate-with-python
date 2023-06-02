# gaussian sum

total = 0
for num in range(101):
    print('total: ' + str(total) + ' +  num: ' + str(num) + ' = ' + str(total + num))
    total = total + num
    
print(total)