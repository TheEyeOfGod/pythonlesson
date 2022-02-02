lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

nlst = [lst[num] for num in range(1, len(lst)) if lst[num] > lst[num - 1]]
print(nlst)