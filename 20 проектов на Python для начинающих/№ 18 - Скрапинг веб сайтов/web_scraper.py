# ===============================================================
#                     Инструкция по запуску
# ===============================================================
# Скрипт скачивает HTML-страницу по URL и ищет все заголовки <h1>,
# выводя их текст в консоль с номерами.
#
# 1. Создать виртуальное окружение:
#    python -m venv my_env
#
#    • Windows:     my_env\Scripts\activate
#    • Linux/macOS: source my_env/bin/activate
#
# 2. Установить зависимости:
#    pip install -r requirements.txt
#    (requests, beautifulsoup4)
#
# 3. Запустить скрипт:
#    python web_scraper.py
# ===============================================================

import requests
from bs4 import BeautifulSoup

url = "http://example.com"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    headers = soup.find_all("h1")

    for i, header in enumerate(headers, 1):
        print(str(i) + ". " + header.text.strip())
else:
    print("Не удалось получить страницу")