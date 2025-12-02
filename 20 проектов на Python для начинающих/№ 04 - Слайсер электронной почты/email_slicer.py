def main():
    print("Добро пожаловать в слайсер электронной почты")
    print("")

    email_input = input("Введите ваш адрес электронной почты: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Имя пользователя: ", username)
    print("Домен: ", domain)
    print("Расширение: ", extension)

while True:
    main()