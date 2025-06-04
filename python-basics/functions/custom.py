def greet():
    print("Hello")


greet()


def hello(name):
    print("Hello", name)


hello('Rushi')


def sum(a, b=10):
    return a + b


print(sum(4, 10))

print(sum(a=4, b=10))

print(sum(a=4))

# Multiple Arguemnts


def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply(1, 2, 3, 4, 5, 6))
