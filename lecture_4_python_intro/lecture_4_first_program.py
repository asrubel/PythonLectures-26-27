print("Programming in Python")

# snake_case
# camelCase
my_str1 = "Python"
my_str2 = 'Python'
my_num = 12343454456788888888888888888888888888888888
my_float = 3.14
my_bool = True
some_none = None

print(my_num)
print(type(my_num))
print(id(my_num))

my_num = my_num + 1000
print(my_num)
print(type(my_num))
print(id(my_num))

print(some_none)
print(type(some_none))
print(id(some_none))

one_more_none = None
print(one_more_none)
print(type(one_more_none))
print(id(one_more_none))

another_str = "Python"
print(id(my_str1))
print(id(my_str2))
print(id(another_str))

my_str1 = my_str1 + " 3.12"
print(my_str1)
print(id(my_str1))
