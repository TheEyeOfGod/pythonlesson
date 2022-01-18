duration = int(input("Введите количество секунд: "))

second = duration % 60
minute = duration // 60 % 60
day = duration // 3600 // 24
hour = duration // 3600 - day * 24

print("дни: ", day, " часы: ", hour, " минуты: ",
      minute, " секунды: ", second, sep=" ")

