from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD
import sqlite3


router_client = Router()


@router_client.message(F.text == '/start')
async def start(message: Message):
    await update_BD(message, "/start")
    base = sqlite3.connect("database.db")
    cur = base.cursor()
    base.execute("CREATE TABLE IF NOT EXISTS registration_data(id PRIMARY KEY, fullname TEXT, username TEXT, time_register TEXT, last_time TEXT, last_action TEXT, count INTEGER, active TEXT)")
    base.commit()
    active = int(cur.execute(f"SELECT active FROM registration_data WHERE id={message.from_user.id}").fetchone()[0])
    base.close()
    if active == 2:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Клавиатура тьютора', callback_data='Клавиатура тьютора')],
        [InlineKeyboardButton(text='Ресурсы ВятГУ', callback_data='Ресурсы ВятГУ')],
        [InlineKeyboardButton(text='Цифровые кафедры', callback_data='Цифровые кафедры')],
        [InlineKeyboardButton(text='Помошь с ботом', callback_data='Помошь с ботом')]
        ])
        await message.answer("Основной раздел", reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ресурсы ВятГУ', callback_data='Ресурсы ВятГУ')],
        [InlineKeyboardButton(text='Цифровые кафедры', callback_data='Цифровые кафедры')],
        [InlineKeyboardButton(text='Помошь с ботом', callback_data='Помошь с ботом')]
        ])
        await message.answer("Основной раздел", reply_markup=keyboard)


@router_client.callback_query(F.data == 'Меню')
async def menu(callback: CallbackQuery):
    await update_BD(callback, "Меню")
    base = sqlite3.connect("database.db")
    cur = base.cursor()
    base.execute("CREATE TABLE IF NOT EXISTS registration_data(id PRIMARY KEY, fullname TEXT, username TEXT, time_register TEXT, last_time TEXT, last_action TEXT, count INTEGER, active TEXT)")
    base.commit()
    active = int( cur.execute(f"SELECT active FROM registration_data WHERE id={callback.from_user.id}").fetchone()[0])
    base.close()
    if active == 2:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Клавиатура тьютора', callback_data='Клавиатура тьютора')],
        [InlineKeyboardButton(text='Ресурсы ВятГУ', callback_data='Ресурсы ВятГУ')],
        [InlineKeyboardButton(text='Цифровые кафедры', callback_data='Цифровые кафедры')],
        [InlineKeyboardButton(text='Помощь с ботом', callback_data='Помощь с ботом')]
        ])
        await callback.message.edit_text("Основной раздел", reply_markup=keyboard)
    else:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ресурсы ВятГУ', callback_data='Ресурсы ВятГУ')],
        [InlineKeyboardButton(text='Цифровые кафедры', callback_data='Цифровые кафедры')],
        [InlineKeyboardButton(text='Помощь с ботом', callback_data='Помощь с ботом')]
        ])
        await callback.message.edit_text("Основной раздел", reply_markup=keyboard)
    await callback.answer()


@router_client.callback_query(F.data == 'Ресурсы ВятГУ')
async def source_vyatsu(callback: CallbackQuery):
    await update_BD(callback, "Ресурсы ВятГУ")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сайт ВятГУ', url='https://www.vyatsu.ru/'),
        InlineKeyboardButton(text='Личный кабинет', url='https://new.vyatsu.ru/account/')],
        [InlineKeyboardButton(text='Moodle', url='https://e.vyatsu.ru/'),
        InlineKeyboardButton(text='VK', url='https://vk.com/vyatsu')],
        [InlineKeyboardButton(text='Telegram', url='https://t.me/vyatsunews')],
        [InlineKeyboardButton(text='Меню', callback_data='Меню')]
        ])
    await callback.message.edit_text("Ресурсы ВятГУ", reply_markup=keyboard)
    await callback.answer()


@router_client.callback_query(F.data == 'Цифровые кафедры')
async def digital_departments(callback: CallbackQuery):
    await update_BD(callback, "Цифровые кафедры")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='1 модуль', callback_data='1 модуль'),
        InlineKeyboardButton(text='2 модуль', callback_data='2 модуль'),
        InlineKeyboardButton(text='3 модуль', callback_data='3 модуль'),
        InlineKeyboardButton(text='4 модуль', callback_data='4 модуль')],
        [InlineKeyboardButton(text='5 модуль', callback_data='5 модуль'),
        InlineKeyboardButton(text='6 модуль', callback_data='6 модуль'),
        InlineKeyboardButton(text='7 модуль', callback_data='7 модуль'),
        InlineKeyboardButton(text='8 модуль', callback_data='8 модуль')],
        [InlineKeyboardButton(text='Меню', callback_data='Меню')]
        ])
    await callback.message.edit_text("1 модуль - основы программирования на Python", reply_markup=keyboard)
    await callback.answer()


@router_client.message(F.text == '/help')
async def help(message: Message):
    await update_BD(message, "/help")
    await message.answer(
        "Основная информация:\n\nℹ️ Чтобы обновить клавиатуру, напишите /start\n\nℹ️ С помощью бота Вы всегда можете получить электронные версии материалов.\n\nℹ️ Вопросы по поводу ошибок писать сюда:\nTelegram: @advanced_default_user\nVk: vk.com/advanced_default_user",
        disable_web_page_preview=True)


@router_client.callback_query(F.data == 'Помощь с ботом')
async def help(callback: CallbackQuery):
    await update_BD(callback, "Помощь с ботом")
    await callback.message.edit_text(
        "Основная информация:\n\nℹ️ Чтобы обновить клавиатуру, напишите /start\n\nℹ️ С помощью бота Вы всегда можете получить электронные версии материалов.\n\nℹ️ Вопросы по поводу ошибок писать сюда:\nTelegram: @advanced_default_user\nVk: vk.com/advanced_default_user",
        disable_web_page_preview=True)
    await callback.answer()

