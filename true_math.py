
import math

def divide2_x_y():

    x = int(input('Введите число x:'))
    y = int(input('Введите число y:'))


    if y != 0:
        print(x / y)

    else:
        print(math.inf)

result1 = divide2_x_y()