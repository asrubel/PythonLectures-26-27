empty_dict = dict()
print(type(empty_dict))

my_dict = {'518': 5, '519': 15, '516': 20}
print(my_dict)
print(my_dict['518'])
my_dict['518'] = my_dict['518'] + 1
print(my_dict)

print("Keys only ---------------------")
for key in my_dict:
    print(key)

print(my_dict.keys())
for key in my_dict.keys():
    print(key)

print("Values only -------------------")
for value in my_dict.values():
    print(value)

print("Items only --------------------")
print(my_dict.items())
for pair in my_dict.items():
    print(pair)

for key, value in my_dict.items():
    print(key, " -> ", value)

new_dict = {1: "number", 3.2: "float", "str": "string",
            (): "tuple", (1, 2, 3): "tuple"}
print(new_dict)

print(hash((1, 2, 3, "str", 4.5)))
