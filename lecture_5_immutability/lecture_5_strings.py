# My comment

print('Python 3.11')
print("Python 3.10")

print('Python "3.11"')
print("Python '3.10'")

print('Python \'3.10\'')
print("Python \"3.11\"")

# TODO - Implement this later

my_num = 100
print(id(my_num))
print(type(my_num))
my_num += 10
print(id(my_num))
print(my_num.bit_count())

my_str = "Python, version '3.12'"
print(my_str)
print(id(my_str))
print(type(my_str))
new_str = my_str.replace('2', '3')
print(new_str)
print(id(new_str))

print(my_str.lower())
print(my_str.upper())
print(my_str.capitalize())
print(my_str.title())
print(my_str.swapcase())

redundant_str = "   fdgdfg  "
print(redundant_str)
print(redundant_str.lstrip())
print(redundant_str.rstrip())
print(redundant_str.strip())

some_str = "pythonyth"
print(some_str.find('th'))
print(some_str.find('th'), 5)
print(some_str.index('y'))
print(some_str.count('y'))
print(some_str.count('yth'))

user_input = input("Please enter a string: ")
print(user_input)
print(user_input.split())
