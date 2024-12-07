import requests

reg = requests.get('https://github.com')
if reg.status_code == 200:
    print(f'Есть сертификат SSL')
print('Кодировка сайта', reg.encoding)

####
# импортируем форк PIL
from PIL import Image

pic = "picture.jpeg"
with Image.open(pic) as im:
    print("Параметры изображения", im.format, im.size, im.mode)
    # открыть изображение
    im.show()
    # поворот изображения
    converted_img = im.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.show()

