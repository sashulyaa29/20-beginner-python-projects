def replace_word():
    str = "привет ребята, я томи, и привет привет привет привет"
    word_to_replace = input("Введите слово, которое нужно заменить: ")
    word_replacement = input("На что заменить слово: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()