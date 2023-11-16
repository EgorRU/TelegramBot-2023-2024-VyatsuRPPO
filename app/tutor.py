from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_tutor = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сводная таблица', url='https://docs.google.com/spreadsheets/d/1QAD5LnGSAaSBU8Q4EO8dRPqeoeQkKD2VmoaWrjJDiUk/edit')],
        [InlineKeyboardButton(text='Таблица с корпоративными почтами', url='https://docs.google.com/spreadsheets/d/15ywquVtsVj19oq8UoUuaHhPAY8um0XHg/edit')],
        [InlineKeyboardButton(text='Ссылка на ассесмент(НЕ IT)', url='https://testing.assessment.unionepro.ru/courses/6537ebcee4d75719e8c430d4')],
        [InlineKeyboardButton(text='Ссылка на ассесмент(IT)', url='https://testing.assessment.unionepro.ru/courses/6537ed18e4d75719e8c430da')],
        [InlineKeyboardButton(text='Меню', callback_data='Меню')]
        ])


@router_tutor.callback_query(F.data == 'Клавиатура тьютора')
async def keyboard_tutor(callback: CallbackQuery):
    await update_BD(callback, "Клавиатура тьютора")
    await callback.message.edit_text("Клавиатура тьютора", reply_markup=keyboard)
    await callback.answer()