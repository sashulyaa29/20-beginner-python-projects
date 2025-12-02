def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Високосный год")
            else:
                print("Не високосный год")
        else:
            print("Високосный год")
    else:
        print("Не високосный год")

# Пример
is_leap_year(2000) # високосный

# Ниже, другие примеры (закомментированы)
# is_leap_year(1900)  # не високосный
# is_leap_year(2020)  # високосный
# is_leap_year(2021)  # не високосный
# is_leap_year(2052)  # високосный