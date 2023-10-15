from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_3 = Router()


"""удалить потом
"""
@router_module_3.callback_query(F.data == '3 модуль')
async def module_1(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    await callback.answer()
    

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции3'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ3')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами3')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_3.callback_query(F.data == '3 модуль')
async def module_3(callback: CallbackQuery):
    await update_BD(callback, "3 модуль")
    await callback.message.edit_text("Модуль 3", reply_markup=keyboard)
    await callback.answer()


@router_module_3.callback_query(F.data == 'Файл со всеми материалами3')
async def file_3(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами3")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9imT_cSOeJP1yJ7HXS9jBFCSuTE0MAAKOOQACunMBSAqqZub0buWzMAQ")
        await callback.message.answer("Модуль 3", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/DqaFNejpA1c'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 31')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/ViBLgHyxsHI'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 32')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/-WNZte7Rgn4'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 33')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/bdt9ffXfn3c'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 34')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/VvSVLJovQR8'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 35')],
    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
    ])


@router_module_3.callback_query(F.data == 'Лекции3')
async def lect_3(callback: CallbackQuery):
    await update_BD(callback, "Лекции3")
    await callback.message.edit_text("Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_3.callback_query(F.data == 'Материал 31')
async def material_31(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9jGT_cSb8xvOaOU9CiiQ2Fpeyhx3AAAKPOQACunMBSAawgjr-erpYMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9jmT_cSd6KOzRSuDt-ZLRWfKGQLj0AAKQOQACunMBSCcHtKomFXLqMAQ")
        await callback.message.answer("Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_3.callback_query(F.data == 'Материал 32')
async def material_32(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9kGT_cUWKp9H-DlDJiNrfoof820a1AAKSOQACunMBSOcx5wp4u3gpMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9kmT_cUioLkP84VxFJY7kqZ6rxIVXAAKTOQACunMBSC3gsWCdxNCAMAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Материал 33')
async def material_33(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9lmT_cWV8-PEo-FVM8_2bRaM9AfWtAAKWOQACunMBSO-XOsJiKq55MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9lGT_cWEwJnM7AfK6AtdE2hJdDDruAAKVOQACunMBSLHLLlM4-jf0MAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Материал 34')
async def material_34(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9mmT_cb9M4tEe3ScPgs__xqnirQZQAAKdOQACunMBSC4_A5gO9zg0MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9mGT_cbyGT9jcT8YuwCgqMjtJgcXMAAKcOQACunMBSJWjfteJ_kXLMAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Материал 35')
async def material_35(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9nmT_cd9HnnLETt7RRRCWpKDECyjoAAKgOQACunMBSOGH4DOXwQ8LMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9nGT_cdup28S69W8JCOF99SzhH3J_AAKeOQACunMBSOPX4eXGl4fZMAQ")
        await callback.message.answer( "Раздел лекций 3 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 31')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 32')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 33')],
    [InlineKeyboardButton(text='Назад', callback_data='3 модуль')]
    ])


@router_module_3.callback_query(F.data == 'Материал лаб. работ3')
async def lect_3(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ3")
    await callback.message.edit_text("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_3.callback_query(F.data == 'Лабораторная работа 31')
async def lab_31(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9oGT_cgABztpoAfGPonocDeOM4hJI-AACoTkAArpzAUgnI8-y-CHWtDAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9oWT_cgECOQ3Px1BHDeCfykrAMw_PAAKiOQACunMBSLnnVwnItPWwMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9pGT_cgcGkAuqL7gi4JzLGO3jbbofAAKjOQACunMBSDvAnZY7JWL-MAQ")
        await callback.message.answer("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_3.callback_query(F.data == 'Лабораторная работа 32')
async def lab_32(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9pmT_ciio91QUj_hNn5bokBhrSNWVAAKlOQACunMBSKCL9vwZil1WMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9qGT_cit9k7wOIBCmCtEx4olsf-EzAAKmOQACunMBSARjSl0ltIG8MAQ")
        await callback.message.answer("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_3.callback_query(F.data == 'Лабораторная работа 33')
async def lab_33(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9qmT_ckW2pDEQj0OzUYekWRO66AFvAAKnOQACunMBSKk2wLX9q-ILMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9rGT_ckhLO7TGB7yBvhXCVEhAYC3sAAKoOQACunMBSFSMxXpWlTPkMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9rmT_ck6O8yeujy5cYVPh718nkWPpAAKqOQACunMBSFjwswABzs92oDAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9r2T_ck6-792KoleSaAeVppmB7mwjAAKrOQACunMBSDqTVScLmQN0MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9smT_clQ_GZD02DXHWg5nAi_VbnohAAKsOQACunMBSJ-4U2dZcIIyMAQ")
        await callback.message.answer("Раздел лабораторных работ 3 модуля", reply_markup=keyboard_labs)
        await callback.answer()