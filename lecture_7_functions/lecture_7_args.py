def multiply(first, second, *args):
    """Multiplies two numbers"""
    print(args)
    print(type(args))

    res = first * second
    for arg in args:
        # res = res * arg
        res *= arg

    return res


print(multiply(3, 4))
print(multiply(3, multiply(4, 5)))
print(multiply(3, 4, 5))
print(multiply(3, 4, 5, 6, 7))
print(multiply(3, 4, *range(1, 100)))

print(range(1, 100))
print(*range(1, 100))
