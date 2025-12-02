import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
	password_length = int(input("Какой длины вы хотите пароль? "))
	random.shuffle(characters)
	password = []

	for x in range(password_length):
		password.append(random.choice(characters))

	random.shuffle(password)
	password = "".join(password)
	print("Ваш сгенерированный пароль:", password)

option = input("Хотите сгенерировать пароль? (Да/Нет): ")

if option == "Да":
	generate_password()
elif option == "Нет":
	print("Программа завершена")
	quit()
else:
	print("Неверный ввод, пожалуйста введите Да или Нет")
	quit()