# ===============================================================
#                     Инструкция по запуску
# ===============================================================
# Скрипт использует Pillow (PIL) для изменения размера изображения.
# Он показывает текущий размер, запрашивает новую ширину и высоту,
# сохраняет изображение с новыми размерами и выводит результат.
#
# 1. Создать виртуальное окружение:
#    python -m venv my_env
#
#    • Windows:     my_env\Scripts\activate
#    • Linux/macOS: source my_env/bin/activate
#
# 2. Установить зависимости:
#    pip install -r requirements.txt
#    (pillow)
#
# 3. Запустить скрипт:
#    python image_resizer.py
# ===============================================================

from PIL import Image

def resize_image(width, height):
   image = Image.open("images/my_picture.jpg")

   resized_image = image.resize((width, height))
   resized_image.save("my_picture_resized_" + str(width) + "x" + str(height) + ".jpeg")

   print("\nНовый размер изображения: " + str(resized_image.size) + "\n")

image = Image.open("images/my_picture.jpg")
print("Текущий размер изображения: " + str(image.size) + "\n")

width = int(input("Введите ширину: "))
height = int(input("Введите длину: "))

resize_image(width, height)