import os
import uuid

import telebot
from telebot import types

from func import create_image_for_2drots, create_image_for_broke_boys, create_image_for_fc_bus, \
    create_image_for_fight_nights, create_image_for_goats, create_image_for_lotus, create_image_for_amkal, \
    create_image_for_d_media, create_image_for_rockets, create_image_for_horses, create_image_for_match_tv, \
    create_image_for_narodnaya, create_image_for_rodina, create_image_for_roma, create_image_for_cka, \
    create_image_for_tandem, create_image_for_titan, create_image_for_fk_10, create_image_for_piter, \
    create_image_for_egrisi

bot = telebot.TeleBot("7233849242:AAH-R--7Ts8rPIIcTAhwiRe3ELhWQE8lX-g")
user_state = {}


def start_keyboard():
    start = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='HighQual', url='https://t.me/HighQuaI', callback_data='linked_start')
    start.add(button1)
    return start


def main():
    main_bord = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='🖼️Обои')
    main_bord.add(button1)
    return main_bord


def clubs():
    clubs_bord = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='2DROTS', callback_data='2drots')
    button2 = types.InlineKeyboardButton(text='BROKE BOYS', callback_data='broke_boys')
    button3 = types.InlineKeyboardButton(text='FC BUS', callback_data='fc_bus')
    button4 = types.InlineKeyboardButton(text='FIGHT NIGHTS', callback_data='fight_nights')
    button5 = types.InlineKeyboardButton(text='GOATS', callback_data='goats')
    button6 = types.InlineKeyboardButton(text='LOTUS', callback_data='lotus')
    button7 = types.InlineKeyboardButton(text='АМКАЛ', callback_data='amkal')
    button8 = types.InlineKeyboardButton(text='Д Медиа', callback_data='d_media')
    button9 = types.InlineKeyboardButton(text='Деньги Рокетов', callback_data='rockets')
    button10 = types.InlineKeyboardButton(text='Кони', callback_data='horses')
    button11 = types.InlineKeyboardButton(text='Матч ТВ', callback_data='match_tv')
    button12 = types.InlineKeyboardButton(text='Народная Команда', callback_data='narodnaya')
    button13 = types.InlineKeyboardButton(text='Родина Медиа', callback_data='rodina')
    button14 = types.InlineKeyboardButton(text='Рома', callback_data='roma')
    button15 = types.InlineKeyboardButton(text='CKA', callback_data='cka')
    button16 = types.InlineKeyboardButton(text='Тандем', callback_data='tandem')
    button17 = types.InlineKeyboardButton(text='Титан', callback_data='titan')
    button18 = types.InlineKeyboardButton(text='ФК 10', callback_data='fk_10')
    button19 = types.InlineKeyboardButton(text='Чисто Питер', callback_data='piter')
    button20 = types.InlineKeyboardButton(text='Эгриси', callback_data='egrisi')
    clubs_bord.add(button1, button2, button3, button4)
    clubs_bord.add(button5, button6, button7, button8)
    clubs_bord.add(button9, button10, button11, button12)
    clubs_bord.add(button13, button14, button15, button16)
    clubs_bord.add(button17, button18, button19, button20)
    return clubs_bord


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, 'Пустой', reply_markup=main())
    bot.send_message(message.chat.id, "Привет, дорогой подписчик! Чт бы разблокировать функционал бота, тебе потребуется подписка на наш канал 👇🏻", reply_markup=start_keyboard())


@bot.message_handler(func=lambda message: True)
def wallpapers_message_handler(message):
    user = bot.get_chat_member(-1001950300501, message.from_user.id)
    if user and user.status in ['creator', 'administrator', 'member']:
        if message.text == "🖼️Обои":
            bot.send_message(message.chat.id, "Выберите команду", reply_markup=clubs())
    else:
        bot.send_message(message.chat.id, "Для использования функционала подпишитесь на канал!!!", reply_markup=start_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def clubs_callback_handlers(call):
    if call.data == "2drots":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_2drots, call.data)
    elif call.data == 'broke_boys':
        print("broke_boys")
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_broke_boys, call.data)
    elif call.data == "fc_bus":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_fc_bus, call.data)
    elif call.data == "fight_nights":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_fight_nights, call.data)
    elif call.data == "goats":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_goats, call.data)
    elif call.data == 'lotus':
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_lotus, call.data)
    elif call.data == "amkal":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_amkal, call.data)
    elif call.data == "d_media":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_d_media, call.data)
    elif call.data == "rockets":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_rockets, call.data)
    elif call.data == "horses":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_horses, call.data)
    elif call.data == "match_tv":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_match_tv, call.data)
    elif call.data == "narodnaya":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_naradnaya, call.data)
    elif call.data == "rodina":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_rodina, call.data)
    elif call.data == "roma":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_roma, call.data)
    elif call.data == "cka":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_cka, call.data)
    elif call.data == "tandem":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_tandem, call.data)
    elif call.data == "titan":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_titan, call.data)
    elif call.data == "fk_10":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_fk_10, call.data)
    elif call.data == "piter":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_piter, call.data)
    elif call.data == "egrisi":
        bot.send_message(call.message.chat.id, 'Привет! Укажите фамилию/имя/ник, только на английском языке (лимит 10 символов):')
        bot.register_next_step_handler(call.message, name_asking_for_egrisi, call.data)


def name_asking_for_2drots(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_2drots)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_2drots, club)


def name_asking_for_broke_boys(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_for_broke_boys)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_broke_boys, club)


def name_asking_for_fc_bus(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_for_fc_bus)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_fc_bus, club)


def name_asking_for_fight_nights(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_fight_nights)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_fight_nights, club)


def name_asking_for_goats(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_goats)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_goats, club)


def name_asking_for_lotus(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_lotus)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_lotus, club)


def name_asking_for_amkal(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_amkal)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_amkal, club)


def name_asking_for_d_media(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_d_media)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_d_media, club)


def name_asking_for_rockets(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_rockets)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_rockets, club)


def name_asking_for_horses(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_horses)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_horses, club)


def name_asking_for_match_tv(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_mathc_tv)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_match_tv, club)


def name_asking_for_naradnaya(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_naradnaya)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_naradnaya, club)


def name_asking_for_rodina(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_rodina)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_rodina, club)


def name_asking_for_roma(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_roma)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_roma, club)


def name_asking_for_cka(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_cka)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_cka, club)


def name_asking_for_tandem(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_tandem)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_tandem, club)


def name_asking_for_titan(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_titan)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_titan, club)


def name_asking_for_fk_10(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_fk_10)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_fk_10, club)


def name_asking_for_piter(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_piter)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_piter, club)


def name_asking_for_egrisi(message, club):
    if len(message.text) <= 10 and message.text.isascii():
        user_state[message.chat.id] = {'name': message.text, 'club': club}
        bot.send_message(message.chat.id, "Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_egrisi)
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите фамилию/имя/ник на английском языке (лимит 10 символов):")
        bot.register_next_step_handler(message, name_asking_for_egrisi, club)


def result_2drots(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'root/footbalopencv/images/{club}.jpg'
        image_name = f'root/footbalopencv/{club}_text_{unique_id}.jpg'
        font_path = f'root/footbalopencv/fonts/{club}.TTF'

        create_image_for_2drots(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_2drots)


def result_for_broke_boys(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'
        font_path2 = f'fonts/{club}_numbers.TTF'

        create_image_for_broke_boys(path, font_path, font_path2, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_for_broke_boys)


def result_for_fc_bus(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'root/footbalopencv/fonts/{club}.TTF'

        create_image_for_fc_bus(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_for_fc_bus)


def result_fight_nights(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'root/footbalopencv/fonts/{club}.TTF'

        create_image_for_fight_nights(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_fight_nights)


def result_goats(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'footbalopencv/fonts/{club}.TTF'


        create_image_for_goats(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_goats)


def result_lotus(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'
        font_path2 = f'fonts/{club}_numbers.TTF'
        print(club)

        create_image_for_lotus(path, font_path, font_path2, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_lotus)


def result_amkal(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_amkal(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_amkal)


def result_d_media(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_d_media(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_d_media)


def result_rockets(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_rockets(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_rockets)


def result_horses(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_horses(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_rockets)


def result_mathc_tv(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_match_tv(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_rockets)


def result_naradnaya(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_narodnaya(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_naradnaya)


def result_rodina(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_rodina(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_rodina)


def result_roma(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_roma(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_roma)


def result_cka(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_cka(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_cka)


def result_tandem(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_tandem(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_tandem)


def result_roma(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_roma(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_roma)


def result_titan(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_titan(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_titan)


def result_fk_10(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'
        font_path2 = f'fonts/{club}_numbers.TTF'

        create_image_for_fk_10(path, font_path, font_path2, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_fk_10)


def result_piter(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_piter(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_piter)


def result_egrisi(message):
    if message.text.isdigit() and 0 <= int(message.text) <= 99:
        user_state[message.chat.id]['number'] = int(message.text)

        your_name = user_state[message.chat.id]['name']
        your_number = user_state[message.chat.id]['number']
        club = user_state[message.chat.id]['club']

        unique_id = str(uuid.uuid4())
        path = f'images/{club}.jpg'
        image_name = f'{club}_text_{unique_id}.jpg'
        font_path = f'fonts/{club}.TTF'

        create_image_for_egrisi(path, font_path, image_name, your_name, your_number)

        with open(image_name, 'rb') as img:
            bot.send_photo(message.chat.id, img)

        # Удаление временного файла
        os.remove(image_name)

        # Очистка состояния пользователя
        del user_state[message.chat.id]
    else:
        bot.send_message(message.chat.id, "Неверный формат. Укажите номер от 0 до 99:")
        bot.register_next_step_handler(message, result_egrisi)

bot.polling()
