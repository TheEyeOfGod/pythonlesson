a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
b = []

for i in a:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            b.append(f"'{int(i):02}'")
        else:
            b.append(f"'{i[0]}{int(i[1:]):02}'")
    else:
        b.append(i)

print(b)
print(' '.join(b))




