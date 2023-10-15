from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_4 = Router()


"""удалить потом
"""
@router_module_4.callback_query(F.data == '4 модуль')
async def module_1(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    await callback.answer()
    

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции4'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ4')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами4')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_4.callback_query(F.data == '4 модуль')
async def module_4(callback: CallbackQuery):
    await update_BD(callback, "4 модуль")
    await callback.message.edit_text("Модуль 4", reply_markup=keyboard)
    await callback.answer()


@router_module_4.callback_query(F.data == 'Файл со всеми материалами4')
async def file_4(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами4")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9DWT_b0CKRsEEaNOrHqcqmGfyvTC9AAJdOQACunMBSKWDOQ9SJgABgjAE")
        await callback.message.answer("Модуль 4", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/MMkW9IKBqjo'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 41')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/aIJWHeepO7s'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 42')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/pEvhS_YPjaI'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 43')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/hW4CFDfKSNA'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 44')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/lt7QdWC-Wfw'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 45')],
    [InlineKeyboardButton(text='Назад', callback_data='4 модуль')]
    ])


@router_module_4.callback_query(F.data == 'Лекции4')
async def lect_4(callback: CallbackQuery):
    await update_BD(callback, "Лекции4")
    await callback.message.edit_text("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_4.callback_query(F.data == 'Материал 41')
async def material_41(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9D2T_b0QKOF4RehBZ4qv1Xq7szpLAAAJeOQACunMBSGrCSGVTnYUDMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9EWT_b0Z7b1EJl41_v_oeS7YgXEMCAAJhOQACunMBSFdMOk1w7aTDMAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_4.callback_query(F.data == 'Материал 42')
async def material_42(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9E2T_b2WwO0-ZBrtwMcsfMYJJveSTAAJkOQACunMBSEpgXJuZLJBoMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9FWT_b2kv0l7ICRelQ8_QNbjEFkYmAAJlOQACunMBSOEP9UKwbZO0MAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Материал 43')
async def material_43(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9F2T_b4JMQB-T79-JgQTGS2Aw0s5XAAJmOQACunMBSKih58gFO7G3MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9GWT_b4SyjqLEQm1E9BwSrD-VBWBZAAJnOQACunMBSElVXZyO7V9KMAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Материал 44')
async def material_44(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9G2T_b5_QhFtJUPYisErYDiyq2TmuAAJoOQACunMBSEYCOCKMNutUMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9HWT_b6MEu3ZEtUx4XJfW3jmk87TlAAJpOQACunMBSBiugMTvXPA_MAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Материал 45')
async def material_45(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9H2T_b8AjYodCvbCn1dT2GGjCfwqXAAJqOQACunMBSO9Fs9JZn9b2MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9IWT_b8Nhlcwvz_fPDcywPP5m5X6iAAJrOQACunMBSNSEBvkbrRBvMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9I2T_b8eD5-dviXR54xUNLjzvkpJIAAJsOQACunMBSDj3apLGFQI9MAQ")
        await callback.message.answer("Раздел лекций 4 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 41')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 42')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 43')],
    [InlineKeyboardButton(text='Назад', callback_data='4 модуль')]
    ])


@router_module_4.callback_query(F.data == 'Материал лаб. работ4')
async def lect_4(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ4")
    await callback.message.edit_text("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_4.callback_query(F.data == 'Лабораторная работа 41')
async def lab_41(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9ZWT_cH3wnVbaDSbtX48MzSOhEfRdAAJzOQACunMBSGHLkCMl5Qo5MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9Z2T_cIAm5nka2uf0DshdOE_C9bTCAAJ1OQACunMBSO1WrkbjuU2BMAQ")
        await callback.message.answer("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_4.callback_query(F.data == 'Лабораторная работа 42')
async def lab_42(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9aWT_cJnH_SPLCxFbTIIy13MOtBYhAAJ3OQACunMBSAoTGpw5zPruMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9a2T_cJvpVKVvD4xkDk6vJSHSB7AlAAJ4OQACunMBSDbW3IdjdUCCMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9bWT_cKC__6dO2cSnqLQb_eEGetXRAAJ7OQACunMBSGPI2NflJ3kUMAQ")
        await callback.message.answer("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_4.callback_query(F.data == 'Лабораторная работа 43')
async def lab_43(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9b2T_cLuaAnIleAoM_xTPxqH3CkJmAAKDOQACunMBSMKP5pjQ0tVvMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9cWT_cL7JFMoOOKpoXDIEd6HGi3htAAKEOQACunMBSBX1N15bMOfEMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9c2T_cMFb1PAdTSLrrzPinYnreTLlAAKGOQACunMBSG6ofDj6t4hpMAQ")
        await callback.message.answer("Раздел лабораторных работ 4 модуля", reply_markup=keyboard_labs)
        await callback.answer()