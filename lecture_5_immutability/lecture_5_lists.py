my_list = ["Python", "Java", "C++", "Kotlin", "JS"]
print(my_list)
print(id(my_list))

print(", ".join(my_list))
my_list.append("Swift")
my_list.append("Rust")
my_list.append("Dart")
print(my_list)
print(id(my_list))

my_list.extend(["C", "Haskell", "Perl"])
print(my_list)
print(id(my_list))

my_list.remove("Perl")
print(my_list)
print(id(my_list))
del my_list[1]
print(my_list)

for item in my_list:
    print(item)

print(my_list)

for symbol in "Python":
    print(symbol)

for i in range(10):
    print(i)

for i in range(5):
    print(str(i) + ' ' + my_list.pop())

print(my_list)
print(my_list.pop(0))
print(my_list)
print(my_list.pop(1))
print(my_list)

a = 100
b = 100
c = a
print(id(a))
print(id(b))
print(id(c))
a += 100
print(id(a))
print(id(b))
print(id(c))

that_list = my_list
print(id(my_list))
print(id(that_list))
print(my_list)
print(that_list)

my_list.append("Python")
print(id(my_list))
print(id(that_list))
print(my_list)
print(that_list)

letters_list = list("Python")
print(letters_list)
print(len(letters_list))
