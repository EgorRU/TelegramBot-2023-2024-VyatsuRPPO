from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_tutor = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сводная таблица', url='https://docs.google.com/spreadsheets/d/1QAD5LnGSAaSBU8Q4EO8dRPqeoeQkKD2VmoaWrjJDiUk/edit')],
        [InlineKeyboardButton(text='Меню', callback_data='Меню')]
        ])


@router_tutor.callback_query(F.data == 'Клавиатура тьютора')
async def keyboard_tutor(callback: CallbackQuery):
    await update_BD(callback, "Клавиатура тьютора")
    await callback.message.edit_text("Клавиатура тьютора", reply_markup=keyboard)
    await callback.answer()