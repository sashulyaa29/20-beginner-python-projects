import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["камень", "ножницы", "бумага"]
    user_input = input("Выберите камень, ножницы, бумага или выход: ")
    computer_input = random.choice(options)
    
    if user_input == "выход":
        print("\nИгра завершена")
        print("Вы набрали " + str(user_points) + " очков, а компьютер набрал " + str(computer_points))
        exit = True
        continue

    if user_input == "камень":
        if computer_input == "камень":
            print("\nВаш выбор: камень")
            print("Выбор компьютера: камень")
            print("Ничья!")
        elif computer_input == "бумага":
            print("\nВаш выбор: камень")
            print("Выбор компьютера: бумага")
            print("Компьютер выиграл")
            computer_points += 1
        elif computer_input == "ножницы":
            print("\nВаш выбор: камень")
            print("Выбор компьютера: ножницы")
            print("Вы выиграли!")
            user_points += 1

    elif user_input == "бумага":
        if computer_input == "камень":
            print("\nВаш выбор: бумага")
            print("Выбор компьютера: камень")
            print("Вы выиграли!")
            user_points += 1
        elif computer_input == "бумага":
            print("\nВаш выбор: бумага")
            print("Выбор компьютера: бумага")
            print("Ничья!")
        elif computer_input == "ножницы":
            print("\nВаш выбор: бумага")
            print("Выбор компьютера: ножницы")
            print("Компьютер выиграл")
            computer_points += 1

    elif user_input == "ножницы":
        if computer_input == "камень":
            print("\nВаш выбор: ножницы")
            print("Выбор компьютера: камень")
            print("Компьютер выиграл!")
            computer_points += 1
        elif computer_input == "бумага":
            print("\nВаш выбор: ножницы")
            print("Выбор компьютера: бумага")
            print("Вы выиграли!")
            user_points += 1
        elif computer_input == "ножницы":
            print("\nВаш выбор: ножницы")
            print("Выбор компьютера: ножницы")
            print("Ничья!")

    elif user_input != "камень" or user_input != "бумага" or user_input != "ножницы":
        print("\nНеверный ввод")