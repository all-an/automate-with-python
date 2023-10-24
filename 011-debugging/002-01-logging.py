import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
print(logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s'))

# factorial 4
print(1 * 2 * 3 * 4)

# factorial 7
print(1 * 2 * 3 * 4 * 5 * 6 * 7)

# disabling logging, all loggings down below will be disabled
#logging.disable(logging.CRITICAL)

logging.debug('start of program')
logging.info('start of program')
logging.warning('start of program')
logging.error('start of program')
logging.critical('start of program')
logging.debug('----------------START-------------------------')

def factorial(n):
    total = 1
    for i in range(n + 1):
        if i > 0:
            total *= i
            logging.debug('i is %s and total is %s' % (i, total))
    logging.debug('----------------END OF FACTORIAL-------------------------')
    return total

print(factorial(4))

print(factorial(5))

logging.debug('end of program')