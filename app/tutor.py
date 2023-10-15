from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_tutor = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Сводная таблица', url='https://docs.google.com/spreadsheets/d/1VoLwNVuGzpxd3Pd67T77tj_VNnaGHfY5pm2ABtd0eHA/edit')],
        [InlineKeyboardButton(text='Распред. тьюторов по группам', callback_data='Распред. тьюторов по группам')],
        [InlineKeyboardButton(text='Меню', callback_data='Меню')]
        ])


@router_tutor.callback_query(F.data == 'Клавиатура тьютора')
async def keyboard_tutor(callback: CallbackQuery):
    await update_BD(callback, "Клавиатура тьютора")
    await callback.message.edit_text("Клавиатура тьютора", reply_markup=keyboard)
    await callback.answer()
    

@router_tutor.callback_query(F.data == 'Распред. тьюторов по группам')
async def group_tutor(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Распред. тьюторов по группам:\n")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7TGT_Y1WugSMKbjzHVATrwN05BZGmAALBOAACunMBSMFL6_9rHsYWMAQ")
        await callback.message.answer("Клавиатура тьютора", reply_markup=keyboard)
        await callback.answer()