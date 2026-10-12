empty_set = set()
print(type(empty_set))

my_set = {1, 2, 3, 4, 4, 4, 4, 5}
print(my_set)

letters = set("pythooooooooon")
print(letters)

set_1 = {'A', 'B', 'C', 'D'}
set_2 = {'D', 'B', 'C', 'A'}
print(set_1 == set_2)

print(len(set_1))
print('A' in set_1)
print('E' in set_1)
print('E' not in set_1)

for item in set_1:
    print(item)

set_1.remove('A')
print(set_1)
set_1.discard('A')
print(set_1)
set_1.add('E')
print(set_1)
