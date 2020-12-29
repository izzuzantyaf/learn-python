import os
"""
Written by Izzu Zantya Fawwas
Website : izzuzantyaf.space
Email : izzuzantyaf@gmail.com
Github : https://github.com/izzuzantyaf
Instagram : https://instagram.com/izzuzantyaf
Twitter : https://twitter.com/izzuzantyaf
Facebook : https://facebook.com/izzuzantyaf
"""

os.system('cls')

# 1. Output
# print a value on console
print('Hello world!')
print(3)
print(True)
print([1, 2, 3])
print((1, 2, 3))
print({1, 2, 3})
print({'first_name': 'Guido', 'last_name': 'Rossum'})

print('\n')

# print variable value
name = 'Guido'
print('Hello, my name is', name)
print('Hi {}'.format(name))
print('Hola, %s' % name)
age = 40
print('My first name is %s and I am %s' % (name, age))

# non string data type will be automaticallly converted to string
list = [1, 2, 3]
print('This is my list %s' % list)

print('\n')

"""
Other argument specifiers
%s - String
%d - Integers
%f - Decimal number
%.<digit>f - Decimal number with specified digit after point
%x/%X - Integer in hexadecimal (lowecase/UPPERCASE)
"""
print('My string is %s' % 'Hello world')
print('My integer is %d' % 45)
print('My float is %f' % 45)
print('My float is %.3f' % 45)
print('%x %X' % (45, 45))

print('\n')

# 2. Input
# store a value from user's input
name = input('Input your name : ')
# it could be a number
age = int(input('Input your age : '))
# it could be a float
PGA = float(input('Input your PGA : '))
print('Your name is %s you are %d y.o and your PGA is %.2f' % (name, age, PGA))

print('\n')

# you can print a mathematic expression
print(eval('2+3'))
# or could it be from user's input
print(eval(input('Write a math expression : ')))
# you can store it in variable too
my_math_expression = input('Write another math expression : ')
print(eval(my_math_expression))
