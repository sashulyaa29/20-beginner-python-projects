def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")
def div(a, b):
    if b == 0:
        print("Ошибка: Ноль в делителе? Так нельзя!\n")
    else:
        if a % b == 0:
            # Если делится нацело, то получаем целое число
            answer = a // b
        else:
            # Если не делится нацело, то получаем дробь
            answer = a / b
        print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. Сложение")
    print("B. Вычитание")
    print("C. Умножение")
    print("D. Деление")
    print("E. Выход")

    choice = input("Введите ваш выбор: ")

    if choice == "a" or choice == "A":
        print("Сложение")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Вычитание")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Умножение")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Деление")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Программа завершена")
        quit()