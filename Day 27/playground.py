def add(*args):
    sum = 0
    for item in args:
        sum += item
    return sum


print(add(1, 2, 3, 45))
