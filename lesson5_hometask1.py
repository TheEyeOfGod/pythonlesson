def number(num):
    for num in range(1, num + 1, 2):
        yield num

for i in number(56):
    print(i)