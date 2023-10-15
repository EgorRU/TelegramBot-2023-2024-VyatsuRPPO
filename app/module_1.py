from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_1 = Router()


"""удалить потом
"""
@router_module_1.callback_query(F.data == '1 модуль')
async def module_1(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    await callback.answer()


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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-P2T_damrDjh6J3kKqJL8Hdii0KR-AALNOQACunMBSAMv4wvs7V9eMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-QmT_da5O7rhs7QpDXY4zks7Nc6-9AALPOQACunMBSAcoRr_YHjT0MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-QWT_da57eET6bjd7LkptSWkVShmHAALOOQACunMBSMd-9aDk3hSJMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-RWT_dd0muZ1f-MZjQCScWat2nbwMAALQOQACunMBSPscLo2Xt19GMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-RmT_dd2HLuCbA1sVH29IOhTL-9PcAALROQACunMBSOqV__RK0e3KMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-SWT_deFRl-ohyvyrTP5P9g31b_0GAALSOQACunMBSM-SFQNZX1NcMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-SmT_deHPjAGmBMK5FhofelBc3e-dAALTOQACunMBSBWKEuvOHOQcMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-TWT_diBf4z3jyw0xDewVlMsLOIByAALUOQACunMBSL0yDDP7OAW9MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-TmT_diDtyin1TE1p6zUOrP4Cm4ntAALVOQACunMBSHZcs4fsFMRmMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-UWT_diWJZ6yEZhIjJJK6mcOaP40gAALWOQACunMBSHzEBATdGCmbMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-UmT_diXm0r2Waju3uqceT3IOznmcAALXOQACunMBSAzdoUlv1sRuMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-VmT_dlqLzkbBc3wMN9XS7d-PepKjAALZOQACunMBSDbCo_mptEm0MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-VWT_dlqWn7z3cUmTlNn_-GlqMO0OAALYOQACunMBSFtNZBNq6YmzMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-WmT_dl9MLdZD_2kepAR4NwABr-Q6JgAC2zkAArpzAUgqz1bI5AT8rTAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-WWT_dl-v_IN2CMBq6y-pBxq5VBS_AALaOQACunMBSLi7LhMemcQHMAQ")
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
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-XmT_dmRWdmQi5KjrJm8yG6RC8V-gAALdOQACunMBSLRpn4ptMHoTMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-XWT_dmQVKm-dtA9gtk2clTFLNm0WAALcOQACunMBSJ1ZVVTYmkwkMAQ")
        await callback.message.answer("Раздел лабораторных работ 1 модуля", reply_markup=keyboard_labs)
        await callback.answer()