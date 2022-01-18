for i in range(1, 101):
    first_digit = i // 10
    second_digit = i % 10
    if first_digit == 1:
        print(i, 'процентов')
    elif first_digit == 1 and second_digit == 1:
        print(i, 'процентов')
    elif 2 <= second_digit <= 4:
        print(i, 'процента')
    elif second_digit == 1:
        print(i, 'процент')
    else:
        print(i, 'процентов')