from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_2 = Router()


"""удалить потом
"""
@router_module_2.callback_query(F.data == '2 модуль')
async def module_1(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    await callback.answer()
    

keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции2'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ2')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами2')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])



@router_module_2.callback_query(F.data == '2 модуль')
async def module_2(callback: CallbackQuery):
    await update_BD(callback, "2 модуль")
    await callback.message.edit_text("Модуль 2", reply_markup=keyboard)
    await callback.answer()


@router_module_2.callback_query(F.data == 'Файл со всеми материалами2')
async def file_2(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами2")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ97WT_dEYXjrgfOJAv9gUk7Izs7y9VAAK1OQACunMBSGTLOR4KLGMSMAQ")
        await callback.message.answer("Модуль 2", reply_markup=keyboard)
        await callback.answer()


keyboard_lecture = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/b2uPoHBWEhE'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 21')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/h7Z31Okj6tY?list=PLjQrQCcomcyN2UWgeg2IF7LnYwoUMPYXj'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 22')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/j_pq-0v1S1s?list=PLjQrQCcomcyN2UWgeg2IF7LnYwoUMPYXj'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 23')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/2GL8TERJ_zg?list=PLjQrQCcomcyN2UWgeg2IF7LnYwoUMPYXj'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 24')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/yughW7TL8gY'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 25')],
    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
    ])


@router_module_2.callback_query(F.data == 'Лекции2')
async def lect_2(callback: CallbackQuery):
    await update_BD(callback, "Лекции2")
    await callback.message.edit_text("Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
    await callback.answer()


@router_module_2.callback_query(F.data == 'Материал 21')
async def material_21(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ972T_dEgeuBkvP0Od_m4m4Ad16t-nAAK2OQACunMBSHwenbvl0UXLMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ98WT_dFqO2o8B9m_orEFxyogLwKMoAAK4OQACunMBSDqbsozRgt89MAQ")
        await callback.message.answer("Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


@router_module_2.callback_query(F.data == 'Материал 22')
async def material_22(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ99WT_dJ4H4wYk-3m32r-jbhBylxlIAAK-OQACunMBSIpAiaR8wZl3MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ982T_dJt_fSmoOgK7-ODgCDNorm2zAAK9OQACunMBSMM-TXFx0HzfMAQ")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Материал 23')
async def material_23(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ992T_dLIG-B0Yd4-ikTVVo9485KxAAAK_OQACunMBSIpzfJKmiRrfMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9-WT_dLWW4WRQThK-KYixL9nCRG_wAALAOQACunMBSCqtYctWz_7BMAQ")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Материал 24')
async def material_24(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9_GT_dNj9huVbjbyxm8Bx2ojBtiwjAALCOQACunMBSDfBl_rsrITgMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9-2T_dNhL79L9kwVxpzIdLLA1oPgQAALBOQACunMBSEOrGgg6TiMjMAQ")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Материал 25')
async def material_25(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ9_2T_dPCqg3A-u0Ii7F6bBp8LUlVnAALEOQACunMBSDJA-xSwai4hMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-AAFk_3TwFNPejy6SAAE7zSFvvwHnY8MAAsU5AAK6cwFIadvupNpokQUwBA")
        await callback.message.answer( "Раздел лекций 2 модуля", reply_markup=keyboard_lecture)
        await callback.answer()


keyboard_labs = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 21')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 22')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 23')],
    [InlineKeyboardButton(text='Назад', callback_data='2 модуль')]
    ])


@router_module_2.callback_query(F.data == 'Материал лаб. работ2')
async def lect_2(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ2")
    await callback.message.edit_text("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
    await callback.answer()
    
   
@router_module_2.callback_query(F.data == 'Лабораторная работа 21')
async def lab_21(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-A2T_dRkAAUbUdvdV8KXv8kTZmHm6BgACxjkAArpzAUjXYpZWyt-wAzAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-BGT_dRnnpkp8kPCP72Y2KJAgEQq5AALHOQACunMBSID3y5gOrQc2MAQ")
        await callback.message.answer("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
        await callback.answer()


@router_module_2.callback_query(F.data == 'Лабораторная работа 22')
async def lab_22(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-B2T_dRsPHncWwmMGN-ZXwa_F7xWDAALIOQACunMBSE3ao-pBwCkPMAQ")
        await callback.message.answer("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
        await callback.answer()
        

@router_module_2.callback_query(F.data == 'Лабораторная работа 23')
async def lab_23(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-CmT_dSYEV7iugb5oMLgjv6_6DmfnAALKOQACunMBSLRb2IQnxBdsMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ-CWT_dSYTFBPBAUJOD-cu-axkvvxqAALJOQACunMBSLVNVPrcsJbQMAQ")
        await callback.message.answer("Раздел лабораторных работ 2 модуля", reply_markup=keyboard_labs)
        await callback.answer()