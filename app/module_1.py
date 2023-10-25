from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_1 = Router()


keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции1'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ1')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами1')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


@router_module_1.callback_query(F.data == '1 модуль')
async def module_1(callback: CallbackQuery):
    await update_BD(callback, "1 модуль")
    await callback.message.edit_text("Модуль 1", reply_markup=keyboard)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Файл со всеми материалами1')
async def file_1(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами1")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDjWU49Sfrh_t4vYDALvjJ1q1tbhuNAAILNgAC0uHISUrrTCQAASPrqjAE")
        await callback.message.answer("Модуль 1", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/FK-sqG2mrlk'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 11')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/1fJ3LFlWY3I'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 12')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/eJRZwVaix9s'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 13')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/GP0jUYaZBHs'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 14')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/cQ7_4Lg99sw'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 15')],
    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
    ])


@router_module_1.callback_query(F.data == 'Лекции1')
async def lect_1(callback: CallbackQuery):
    await update_BD(callback, "Лекции1")
    await callback.message.edit_text("Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_1.callback_query(F.data == 'Материал 11')
async def material_11(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDV2U486U9LY0OC9tRhuw9_WGuaHLfAALpNQAC0uHISTodvCmB4oBkMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDWWU4863nOAN9GA7l8Q4HtDeuYa5tAALqNQAC0uHISR8UY6HlBOgBMAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_1.callback_query(F.data == 'Материал 12')
async def material_12(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDW2U48-Qkxk1hxzlHyV62wi7IIq0SAALuNQAC0uHISRz_sn91pp0QMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDXWU48-y8PmlumGPQjJHBJuC-qphKAALwNQAC0uHISb1V-C9U-PSyMAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 13')
async def material_13(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDX2U49AHjMYzNlSxYKe240M6pussgAALxNQAC0uHISaejb7Dg6JOkMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDYWU49AWXVrVbCLbwytEfIctDFd2HAALyNQAC0uHISQGZTTJQvlLbMAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 14')
async def material_14(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDY2U49B_moh8WxSEWyR9fh1x42iHsAAL0NQAC0uHISS_Q51qTxl0uMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDZWU49CIokHcXAAGDFpXniQk28unefQAC9jUAAtLhyEkqT_b_5cWP9jAE")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Материал 15')
async def material_15(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDZ2U49HRsM5X-Rq_BRh-NwRdTbp2nAAL-NQAC0uHISd1HiHnDmj02MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDaWU49HiebWLMrQXYHjfY5D21VXNVAAL_NQAC0uHISTo0AdS5FSTaMAQ")
        await callback.message.answer( "Раздел лекций 1 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 11')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 12')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 13')],
    [InlineKeyboardButton(text='Назад', callback_data='1 модуль')]
    ])


@router_module_1.callback_query(F.data == 'Материал лаб. работ1')
async def lect_1(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ1")
    await callback.message.edit_text("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_1.callback_query(F.data == 'Лабораторная работа 11')
async def lab_11(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDgWU49Ku-ftBA3e6IZLn3k7IBcr_5AAIDNgAC0uHISfKyShJGzSmxMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDg2U49K5pOd8aURzgihXWIAN5KAMeAAIENgAC0uHISaiSqqNCNsdgMAQ")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_1.callback_query(F.data == 'Лабораторная работа 12')
async def lab_12(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDhWU49M0T0SUOjS83jlM9-oHYtqylAAIFNgAC0uHISTIF2xK6UyxpMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDh2U49M-xmiTkEB1sdfPo4Rhm26_9AAIGNgAC0uHIScr07v5cja2oMAQ")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_1.callback_query(F.data == 'Лабораторная работа 13')
async def lab_13(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDiWU49P7tiV1seQ3iEpo5k7N0SmaZAAIINgAC0uHISQHYfJqFtpg8MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAIDi2U49QEe_o78RUMkJ7hB5YfkBQABwAACCTYAAtLhyElCTFEZIQO81TAE")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()