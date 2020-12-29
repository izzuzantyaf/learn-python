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

# Data type in Python
# 1. Number
# 2. String
# 3. Boolean
# 4. List
# 5. Tuple
# 6. Set
# 7. Dictionary


# 1. Number : Integer, Float, Complex
print('1. Number')
# Integer
a = 10
print(a, 'is type of', type(a))

# Float
b = 10.6
print(b, 'is type of', type(b))

# Complex
c = 1+5j
print(c, 'is comlplex number ?', isinstance(c, complex))
# end of Number data type

print('\n')

# 2. String
print('2. String')
string = "This is a string"

# 2.1 Accessing string
# print the entire string
print('string =', string)
# print specific character in string
print('string[2] = ', string[2])  # print string at index 2
print('string[-1] = ', string[-1])  # print the last char in string
# print specific character in range
print('string[:4] = ', string[: 4])  # 0<=index<4 (print from index 0 until 3)
# 5<=index<7 (print from index 5 until 6)
print('string[5:7] = ', string[5: 7])
# 11<=index<=end (print from index 0 until end of string)
print('string[11:] = ', string[11:])
print('string[-3:] = ', string[-3:])  # print 3 char in string from the last

# 2.2 String behaviour
# the string itself is mutable (the value is changeable), but its elements is immutable
string = "Hello world"  # this will work properly
# string[2] = 'a'  # this will produce an error # UNCOMMENT THIS LINE TO SEE THE ERROR
# end of String data type

print('\n')

# 3. Boolean
print('3. Boolean')
t = True
f = False
print(t)
print(f)
# end of Boolean data type

print('\n')

# 4. List
# List can contains various data type
print('4. List')
x = [5, 10, 15, 50, 90, -26, 35, 40]
# 4.1 Accessing List
print('x[5] = ', x[5])
print('x[-1] = ', x[-1])
print('x[3:5] = ', x[3:5])
print('x[:5] = ', x[:5])
print('x[-3:] = ', x[-3:])
print('x[1:7:2] = ', x[1:7:2])
# end of List data type

print('\n')

# 5. Tuple
# Tuple is non-changeable List
print('5. Tuple')
y = (5, 10, 15, 50, 90, -26, 35, 40)
print(y)
# y[0] = 1  # this will produce an error # UNCOMMENT THIS LINE TO SEE THE ERROR
# end of Tuple data type

print('\n')

# 6. Set
# Set is a group of unique items
print('6. Set')
s = {1, 1, 1, 5, 8, 0, 3, 6, 8, 2}
print(s)
# Set cannot be accessed by index
# print(s[0])  # this will produce an error # UNCOMMENT THIS LINE TO SEE THE ERROR
# end of Set data type

print('\n')

# 7. Dictionary
# Dictionary is group of pairs of key-value
print('7. Dictionary')
# name, home is called key. Izzu, earth is called value
d = {'name': 'Izzu', 'home': 'earth'}
print(d)
# 7.1 Accessing Dictionary
# Dict can be accessed by its key
# Dict cannot accessed by index
print(d['name'], ' is live on ', d['home'])
# end of Dictionary data type
