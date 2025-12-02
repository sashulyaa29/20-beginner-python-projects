# ===============================================================
#                     Инструкция по запуску
# ===============================================================
# 1. Создать виртуальное окружение:
#    python -m venv my_env
#
#    • Windows:     my_env\Scripts\activate
#    • Linux/macOS: source my_env/bin/activate
#
# 2. Установить зависимости:
#    pip install -r requirements.txt
#    (должны быть qrcode и pillow)
#
# 3. Запустить скрипт:
#    python qr_code_generator.py
#
# 4. Ввести URL для генерации QR-кода.
# ===============================================================

import qrcode

def generate_qrcode(text):
   qr = qrcode.QRCode(
      version = 1,
      error_correction = qrcode.constants.ERROR_CORRECT_L,
      box_size = 10,
      border = 4,
   )

qr.add_data(text)
qr.make(fit = True)

img = qr.make_image(fill_color = "black", back_color = "white")
img.save("qr_код.png")

print("QR-код успешно сгенерирован и сохранен.")
    
url = input("Введите URL для QR-кода: ")
generate_qrcode(url)