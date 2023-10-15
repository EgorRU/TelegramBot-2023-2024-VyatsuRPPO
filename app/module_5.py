from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_5 = Router()


"""удалить потом
"""
@router_module_5.callback_query(F.data == '5 модуль')
async def module_1(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    await callback.answer()
    

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции5'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ5')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами5')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_5.callback_query(F.data == '5 модуль')
async def module_5(callback: CallbackQuery):
    await update_BD(callback, "5 модуль")
    await callback.message.edit_text("Модуль 5", reply_markup=keyboard)
    await callback.answer()


@router_module_5.callback_query(F.data == 'Файл со всеми материалами5')
async def file_5(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами5")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8x2T_bfnwp8Yozcps9Xl5a7VbKNcxAAJHOQACunMBSNz4YU8nFJ_dMAQ")
        await callback.message.answer("Модуль 5", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/DI2OyecP8dA'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 51')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/JIslvRvDj0A'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 52')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/JIslvRvDj0A'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 53')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/iL1LuiwUeQA'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 54')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/-SoKsuCA4Lk'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 55')],
    [InlineKeyboardButton(text='Назад', callback_data='5 модуль')]
    ])


@router_module_5.callback_query(F.data == 'Лекции5')
async def lect_5(callback: CallbackQuery):
    await update_BD(callback, "Лекции5")
    await callback.message.edit_text("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_5.callback_query(F.data == 'Материал 51')
async def material_51(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8yWT_bfsH--Mn1BOKDi7dmfnBmTWrAAJIOQACunMBSNO2h7_BSsR5MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8y2T_bfzdPEb5y6HELHcRuAleNeWgAAJJOQACunMBSLNmquftqs63MAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_5.callback_query(F.data == 'Материал 52')
async def material_52(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8zWT_biUqDCDMjfX5zq1vAcU4KAa7AAJMOQACunMBSBlSi9lzHxxGMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8z2T_binB_Nthq6Stg3ATRJrQeUXoAAJNOQACunMBSPA82mA7QbvBMAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Материал 53')
async def material_53(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ80WT_bkpXkBNVwhnG2XsofVkERjEIAAJOOQACunMBSMgCGRSirT6hMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ802T_bk02MJZ40WLHgXN_02IgfUKUAAJPOQACunMBSI-BllGo1nBjMAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Материал 54')
async def material_54(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ812T_bm9r97bnDeyh5FOOMsRJeOcUAAJROQACunMBSK1GyNDf_2K1MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ81WT_bm3Y7WDnHbcL6jhdaHA711qKAAJQOQACunMBSGlE9_qtJDFLMAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Материал 55')
async def material_55(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ82WT_bnXZnD9jbLm6f9wkGVw0u7blAAJSOQACunMBSBGai7s34UIlMAQ")
        await callback.message.answer("Раздел лекций 5 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 51')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 52')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 53')],
    [InlineKeyboardButton(text='Назад', callback_data='5 модуль')]
    ])


@router_module_5.callback_query(F.data == 'Материал лаб. работ5')
async def lect_5(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ5")
    await callback.message.edit_text("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_5.callback_query(F.data == 'Лабораторная работа 51')
async def lab_51(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ822T_bp8EVtKg_ARnxMufg-rmWTsqAAJTOQACunMBSHM7EWvgKEMXMAQ")
        await callback.message.answer("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_5.callback_query(F.data == 'Лабораторная работа 52')
async def lab_52(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ83WT_bqFxeBJovmvHYK1ZSVzi1PWjAAJUOQACunMBSFBaCG3kWDIHMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ832T_bqfEOesorLE9qyH5VQlg_uBGAAJVOQACunMBSK8XdgN5jgABUTAE")
        await callback.message.answer("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_5.callback_query(F.data == 'Лабораторная работа 53')
async def lab_53(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ84WT_bqliwThHesvxR16a7cWqWncKAAJWOQACunMBSHYkmiqCQVnsMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ842T_bq6AVxqs7enrHGFwz2POs5e_AAJXOQACunMBSDTWMNfMupMLMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ85WT_brF45WoPm1muRydcOL2xrcnsAAJYOQACunMBSDdZV-Rt1Sr0MAQ")
        await callback.message.answer("Раздел лабораторных работ 5 модуля", reply_markup=keyboard_labs)
        await callback.answer()