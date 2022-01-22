a = 15 * 3
b = 15 / 3
c = 15 // 2
d = 15 ** 2

print(a) # целое число
print(b) # число с точкой
print(c) # целое число
print(d) # целое число

# выполняем проверку типа объекта

# способ 1
print(type(a) == int)
print(type(b) == float)
print(type(c) == int)
print(type(d) == int)

# способ 2
print(isinstance(a, int))
print(isinstance(b, float))
print(isinstance(c, int))
print(isinstance(d, int))
