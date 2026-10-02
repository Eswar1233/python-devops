"""
This is a multi line comment
"""


a = 42
print(a)


b = 42.34
print(b)

c = True

d = "string"
d = 'string'
d = """"this is multi-line string"""

# Today's weather is nice
d = "Today's weather is nice"
f = 'Today\'s weather i great'
print(d)
print(f)

test_list = ["hello", "world", "python"]

print(test_list)

test_tuple = ("hello", "world", "python")
print(test_tuple)

test_dict = {'a': 1, 'b': 2}
print(test_dict)

test_set = {'a', 'b', 'c', 'd'}
print(test_set)


# type() function --> prints the dataype of the variable
print(type(test_dict))
print(type(print))


a = 42
b = 45.32
c = a + b
print(c)

d = a - b
print(d)

e = a * b
print(e)

print(d, type(d))

h = a // b
print(h)


i = a % b
print(i)

a = "42"
b = "43"
print(a + " " + b)

# power
a = 10
print(a**2)

a = 10
b = 30
res = a > b
res_1 = a < b
res_2 = a != b
print(res, res_1, res_2)

# Logical operators
# AND, NOT, OR 
a = True
b = False
