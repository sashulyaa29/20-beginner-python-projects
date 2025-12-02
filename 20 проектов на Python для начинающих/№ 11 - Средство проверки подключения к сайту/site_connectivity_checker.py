# Пример для проверки: https://www.google.com

import urllib.request as urllib

def main(url):
    print("Проверка соединения")
    
    response = urllib.urlopen(url)

    print("Успешно подключено к", url)
    print("Код ответа сервера: ", response.getcode())

print("Это программа для проверки доступности сайта")
input_url = input("Введите URL сайта, который хотите проверить: ")

main(input_url)