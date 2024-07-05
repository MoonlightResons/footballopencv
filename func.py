import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def create_image_for_2drots(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1100

    if len(your_name) == 1:
        font_size_name = 400
    elif len(your_name) == 2:
        font_size_name = 400
    elif len(your_name) == 3:
        font_size_name = 400
    elif len(your_name) == 4:
        font_size_name = 400
    elif len(your_name) == 5:
        font_size_name = 400
    elif len(your_name) == 7:
        font_size_name = 380
    elif len(your_name) == 8:
        font_size_name = 360
    elif len(your_name) == 9:
        font_size_name = 340
    elif len(your_name) == 10:
        font_size_name = 320
    else:
        #если кол-во символов = 6
        font_size_name = 400

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2000

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 0, 0), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 0, 0), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_broke_boys(path, font_path, font_path2, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1300

    if len(your_name) == 1:
        font_size_name = 400
    elif len(your_name) == 2:
        font_size_name = 400
    elif len(your_name) == 3:
        font_size_name = 400
    elif len(your_name) == 4:
        font_size_name = 400
    elif len(your_name) == 5:
        font_size_name = 400
    elif len(your_name) == 7:
        font_size_name = 380
    elif len(your_name) == 8:
        font_size_name = 330
    elif len(your_name) == 9:
        font_size_name = 300
    elif len(your_name) == 10:
        font_size_name = 280
    else:
        #если кол-во символов = 6
        font_size_name = 400

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2000

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path2, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 6, 15), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 6, 15), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_fc_bus(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1400

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2000

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_fight_nights(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1400

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 300
    elif len(your_name) == 8:
        font_size_name = 350
    elif len(your_name) == 9:
        font_size_name = 260
    elif len(your_name) == 10:
        font_size_name = 250
    else:
        #если кол-во символов = 6
        font_size_name = 380

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2000

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 101, 30), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 101, 30), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_goats(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1400

    if len(your_name) == 1:
        font_size_name = 400
    elif len(your_name) == 2:
        font_size_name = 400
    elif len(your_name) == 3:
        font_size_name = 400
    elif len(your_name) == 4:
        font_size_name = 400
    elif len(your_name) == 5:
        font_size_name = 400
    elif len(your_name) == 7:
        font_size_name = 400
    elif len(your_name) == 8:
        font_size_name = 400
    elif len(your_name) == 9:
        font_size_name = 380
    elif len(your_name) == 10:
        font_size_name = 350
    else:
        #если кол-во символов = 6
        font_size_name = 400

    x_name = (image.width) // 2
    y_name = 1100

    x_number = (image.width) // 2
    y_number = 2400

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 0, 0), stroke_width=20, stroke_fill='white', anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 0, 0), stroke_width=25, stroke_fill='white', anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_lotus(path, font_path, font_path2, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1300

    if len(your_name) == 1:
        font_size_name = 400
    elif len(your_name) == 2:
        font_size_name = 400
    elif len(your_name) == 3:
        font_size_name = 400
    elif len(your_name) == 4:
        font_size_name = 400
    elif len(your_name) == 5:
        font_size_name = 400
    elif len(your_name) == 7:
        font_size_name = 400
    elif len(your_name) == 8:
        font_size_name = 350
    elif len(your_name) == 9:
        font_size_name = 330
    elif len(your_name) == 10:
        font_size_name = 300
    else:
        #если кол-во символов = 6
        font_size_name = 400

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2300

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path2, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 0, 0), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 0, 0), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_amkal(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1700

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2050

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 44, 151), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 44, 151), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_d_media(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1400

    if len(your_name) == 1:
        font_size_name = 400
    elif len(your_name) == 2:
        font_size_name = 400
    elif len(your_name) == 3:
        font_size_name = 400
    elif len(your_name) == 4:
        font_size_name = 400
    elif len(your_name) == 5:
        font_size_name = 400
    elif len(your_name) == 7:
        font_size_name = 380
    elif len(your_name) == 8:
        font_size_name = 360
    elif len(your_name) == 9:
        font_size_name = 340
    elif len(your_name) == 10:
        font_size_name = 320
    else:
        #если кол-во символов = 6
        font_size_name = 400

    x_name = (image.width) // 2
    y_name = 1100

    x_number = (image.width) // 2
    y_number = 2000

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 0, 0), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 0, 0), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_rockets(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1500

    if len(your_name) == 1:
        font_size_name = 420
    elif len(your_name) == 2:
        font_size_name = 420
    elif len(your_name) == 3:
        font_size_name = 420
    elif len(your_name) == 4:
        font_size_name = 420
    elif len(your_name) == 5:
        font_size_name = 420
    elif len(your_name) == 7:
        font_size_name = 400
    elif len(your_name) == 8:
        font_size_name = 350
    elif len(your_name) == 9:
        font_size_name = 330
    elif len(your_name) == 10:
        font_size_name = 300
    else:
        #если кол-во символов = 6
        font_size_name = 420

    x_name = (image.width) // 2
    y_name = 1100

    x_number = (image.width) // 2
    y_number = 2100

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_horses(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1800

    if len(your_name) == 1:
        font_size_name = 400
    elif len(your_name) == 2:
        font_size_name = 400
    elif len(your_name) == 3:
        font_size_name = 400
    elif len(your_name) == 4:
        font_size_name = 400
    elif len(your_name) == 5:
        font_size_name = 400
    elif len(your_name) == 7:
        font_size_name = 400
    elif len(your_name) == 8:
        font_size_name = 400
    elif len(your_name) == 9:
        font_size_name = 400
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 400

    x_name = (image.width) // 2
    y_name = 1100

    x_number = (image.width) // 2
    y_number = 2100

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)



def create_image_for_match_tv(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1800

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2050

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_narodnaya(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1700

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 850

    x_number = (image.width) // 2
    y_number = 1850

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_rodina(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1600

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 950

    x_number = (image.width) // 2
    y_number = 1950

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_roma(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1600

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2150

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_cka(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1400

    if len(your_name) == 1:
        font_size_name = 350
    elif len(your_name) == 2:
        font_size_name = 350
    elif len(your_name) == 3:
        font_size_name = 350
    elif len(your_name) == 4:
        font_size_name = 350
    elif len(your_name) == 5:
        font_size_name = 350
    elif len(your_name) == 7:
        font_size_name = 300
    elif len(your_name) == 8:
        font_size_name = 270
    elif len(your_name) == 9:
        font_size_name = 250
    elif len(your_name) == 10:
        font_size_name = 220
    else:
        #если кол-во символов = 6
        font_size_name = 350

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 1950

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(255, 255, 255), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 255, 255), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)



def create_image_for_tandem(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1700

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 1000

    x_number = (image.width) // 2
    y_number = 1950

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 59, 119), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 59, 119), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_titan(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1600

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2150

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 0, 0), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 0, 0), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_fk_10(path, font_path, font_path2, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1200

    if len(your_name) == 1:
        font_size_name = 400
    elif len(your_name) == 2:
        font_size_name = 400
    elif len(your_name) == 3:
        font_size_name = 400
    elif len(your_name) == 4:
        font_size_name = 400
    elif len(your_name) == 5:
        font_size_name = 400
    elif len(your_name) == 7:
        font_size_name = 300
    elif len(your_name) == 8:
        font_size_name = 280
    elif len(your_name) == 9:
        font_size_name = 220
    elif len(your_name) == 10:
        font_size_name = 200
    else:
        #если кол-во символов = 6
        font_size_name = 380

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2050

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path2, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 0, 0), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(255, 138, 237), stroke_width=130, stroke_fill='black', anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_piter(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1700

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 450
    elif len(your_name) == 8:
        font_size_name = 450
    elif len(your_name) == 9:
        font_size_name = 430
    elif len(your_name) == 10:
        font_size_name = 400
    else:
        #если кол-во символов = 6
        font_size_name = 450

    x_name = (image.width) // 2
    y_name = 1000

    x_number = (image.width) // 2
    y_number = 2050

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 59, 119), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 59, 119), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)


def create_image_for_egrisi(path, font_path, image_name, your_name, your_number):
    img = cv2.imread(path)
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)

    font_size_number = 1600

    if len(your_name) == 1:
        font_size_name = 450
    elif len(your_name) == 2:
        font_size_name = 450
    elif len(your_name) == 3:
        font_size_name = 450
    elif len(your_name) == 4:
        font_size_name = 450
    elif len(your_name) == 5:
        font_size_name = 450
    elif len(your_name) == 7:
        font_size_name = 380
    elif len(your_name) == 8:
        font_size_name = 350
    elif len(your_name) == 9:
        font_size_name = 300
    elif len(your_name) == 10:
        font_size_name = 250
    else:
        #если кол-во символов = 6
        font_size_name = 420

    x_name = (image.width) // 2
    y_name = 1050

    x_number = (image.width) // 2
    y_number = 2150

    font1 = ImageFont.truetype(font_path, font_size_name)
    font2 = ImageFont.truetype(font_path, font_size_number)

    # Рисование текста на изображении
    draw.text((x_name, y_name), your_name, font=font1, fill=(0, 0, 0), anchor="mm")
    draw.text((x_number, y_number), str(your_number), font=font2, fill=(0, 0, 0), anchor='mm')

    # Преобразование изображения обратно в формат OpenCV
    new_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Сохранение нового изображения
    cv2.imwrite(image_name, new_img)