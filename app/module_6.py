from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_6 = Router()


"""удалить потом
"""
@router_module_6.callback_query(F.data == '6 модуль')
async def module_1(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    await callback.answer()
    

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции6'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ6')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами6')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_6.callback_query(F.data == '6 модуль')
async def module_6(callback: CallbackQuery):
    await update_BD(callback, "6 модуль")
    await callback.message.edit_text("Модуль 6", reply_markup=keyboard)
    await callback.answer()


@router_module_6.callback_query(F.data == 'Файл со всеми материалами6')
async def file_6(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами6")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8wGT_bamZSaEQ9FSf8DHUxcEpKcaPAAJFOQACunMBSPMoDvkwpdkoMAQ")
        await callback.message.answer("Модуль 6", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/dfIqseL0jVU'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 61')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/GQNOQ15gqyo'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 62')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/IZK7Xga7Rl8'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 63')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/MJY3-_OxvrM'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 64')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/TgKv1trj8Cc'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 65')],
    [InlineKeyboardButton(text='Назад', callback_data='6 модуль')]
    ])


@router_module_6.callback_query(F.data == 'Лекции6')
async def lect_6(callback: CallbackQuery):
    await update_BD(callback, "Лекции6")
    await callback.message.edit_text("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_6.callback_query(F.data == 'Материал 61')
async def material_61(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8bmT_bBwmtD-oEq_lr2vrYM_ytZRRAAIoOQACunMBSF9RgHIp3jhcMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8cGT_bB39cJzk2T8ModrhHT1Bg0Y9AAIpOQACunMBSE4O8rPD2Qw-MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8cmT_bCN4EIleLys0bFAxbyuU1gtlAAIqOQACunMBSFeqyIGF2N7XMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_6.callback_query(F.data == 'Материал 62')
async def material_62(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8dGT_bEODS-xQW-uaPhqhUt9uqLq2AAIrOQACunMBSMMJs-cmGzmCMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8dmT_bEkaNqBAlwQZjoWaKPF1noiEAAIuOQACunMBSKfLFGcBvTRkMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8eGT_bEtLe7c4NIurfv7hOOGkSSFBAAIvOQACunMBSJAFO4J7Vw2sMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Материал 63')
async def material_63(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8emT_bGyezDIdHb3F-qQZAAEui8H7egACMjkAArpzAUgtCDUsdqwz-zAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8fGT_bG-yLdJQPEvXuuayuSjbU5DEAAIzOQACunMBSDaLvaG_-dbJMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Материал 64')
async def material_64(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8fmT_bIyYn85eTsClCjdQ2u8dnDlhAAI1OQACunMBSGlNFS8dCYfJMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8gGT_bI5a4l5H8louXIg-T_yjiyJzAAI2OQACunMBSEX2LirNiL2lMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Материал 65')
async def material_65(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8gmT_bLcQp4wYimsCp6rzv8Yyt34pAAI4OQACunMBSAdyOkv4fQP2MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8hGT_bLo0mhbGre9o_qIfMR4GrPT9AAI5OQACunMBSAYtxGxTnnmBMAQ")
        await callback.message.answer("Раздел лекций 6 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 61')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 62')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 63')],
    [InlineKeyboardButton(text='Назад', callback_data='6 модуль')]
    ])


@router_module_6.callback_query(F.data == 'Материал лаб. работ6')
async def lect_6(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ6")
    await callback.message.edit_text("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_6.callback_query(F.data == 'Лабораторная работа 61')
async def lab_61(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8hmT_bNvpPQFdi0yk6PcJakAhEnbMAAI6OQACunMBSEb90DLM4KpCMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8iGT_bNwKNknuWeBowkNIzANDUg6VAAI7OQACunMBSPRDQ741M3zyMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8imT_bN52S8l5855iPRgCMYnxGiXkAAI8OQACunMBSEhpj4DNzAO0MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8jGT_bOK8dHFCaAaGqAcW7PQygDllAAI9OQACunMBSH2SGN8Ca-GoMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8jmT_bOY9_djREhf_aA5YVJi5VRo0AAI-OQACunMBSBDh-kHcLemfMAQ")
        await callback.message.answer("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_6.callback_query(F.data == 'Лабораторная работа 62')
async def lab_62(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8kGT_bRSgqlVUw6g9dazApAABL17AUQACPzkAArpzAUig-u_rFdp1-DAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8kmT_bRcPqFgYjANscfxvbOvpjUI2AAJAOQACunMBSGDvfaQbZ3fpMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8lGT_bRjGq5F2ILcXB7HHI9EJ8tEVAAJBOQACunMBSDjI6KDeV5RQMAQ")
        await callback.message.answer("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_6.callback_query(F.data == 'Лабораторная работа 63')
async def lab_63(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8lmT_bT0jHweQBb0v_RzTmcH1sGaCAAJDOQACunMBSK3s1ryr9cdhMAQ")
        await callback.message.answer("Раздел лабораторных работ 6 модуля", reply_markup=keyboard_labs)
        await callback.answer()