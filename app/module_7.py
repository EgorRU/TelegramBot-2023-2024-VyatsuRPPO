from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from other import update_BD


router_module_7 = Router()


"""удалить потом
"""
@router_module_7.callback_query(F.data == '7 модуль')
async def module_1(callback: CallbackQuery):
    await callback.answer("В разработке", show_alert=True)
    await callback.answer()
    

keyboard_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Анализ данных', callback_data='7.1 модуль')],
    [InlineKeyboardButton(text='UI/UX-дизайн', callback_data='7.2 модуль')],
    [InlineKeyboardButton(text='Основы веб-разработки', callback_data='7.3 модуль')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры')]
    ])


@router_module_7.callback_query(F.data == '7 модуль')
async def module_7_main(callback: CallbackQuery):
    await update_BD(callback, "7 модуль")
    await callback.message.edit_text("Модуль 7", reply_markup=keyboard_main)
    await callback.answer()
    

keyboard7_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7.1'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7.1')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами7.1')],
    [InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=640129')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


keyboard7_2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7.2'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7.2')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами7.2')],
    [InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=640457')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


keyboard7_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лекции', callback_data='Лекции7.3'),
    InlineKeyboardButton(text='Материал лаб. работ', callback_data='Материал лаб. работ7.3')],
    [InlineKeyboardButton(text='Файл со всеми материалами', callback_data='Файл со всеми материалами7.3')],
    [InlineKeyboardButton(text='Тестирование', url='https://e.vyatsu.ru/mod/quiz/view.php?id=640589')],
    [InlineKeyboardButton(text='Выбор модуля', callback_data='Цифровые кафедры'),
    InlineKeyboardButton(text='Меню', callback_data='Меню')]
    ])


@router_module_7.callback_query(F.data == '7.1 модуль')
async def module_7_1(callback: CallbackQuery):
    await update_BD(callback, "Анализ данных")
    await callback.message.edit_text("Модуль 7.1", reply_markup=keyboard7_1)
    await callback.answer()
    

@router_module_7.callback_query(F.data == '7.2 модуль')
async def module_7_2(callback: CallbackQuery):
    await update_BD(callback, "UI/UX-дизайн")
    await callback.message.edit_text("Модуль 7.2", reply_markup=keyboard7_2)
    await callback.answer()
    

@router_module_7.callback_query(F.data == '7.3 модуль')
async def module_7_3(callback: CallbackQuery):
    await update_BD(callback, "Основы веб-разработки")
    await callback.message.edit_text("Модуль 7.3", reply_markup=keyboard7_3)
    await callback.answer()


@router_module_7.callback_query(F.data == 'Файл со всеми материалами7.1')
async def file_7_1(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами7.1")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7qGT_aAc_NfW_g1C8Yk2oBp83M8r_AALkOAACunMBSGJ7rFhHgvQ7MAQ")
        await callback.message.answer("Модуль 7.1", reply_markup=keyboard7_1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Файл со всеми материалами7.2')
async def file_7_2(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами7.2")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7pGT_Z_XukXUlXRIGB6h2_3B60dSqAALiOAACunMBSIUYm9Mr_Ur-MAQ")
        await callback.message.answer("Модуль 7.2", reply_markup=keyboard7_2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Файл со всеми материалами7.3')
async def file_7_3(callback: CallbackQuery):
    await update_BD(callback, "Файл со всеми материалами7.3")
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7pmT_Z_o6Sz9D_hMG00C5WfnmnHJzAALjOAACunMBSMAEELVVBdWCMAQ")
        await callback.message.answer("Модуль 7.3", reply_markup=keyboard7_3)
        await callback.answer()


keyboard_lecture1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/ZHpMUlr5pyA'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 71_1')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/KWlWJkSMByQ'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 71_2')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/G7IuOrpNZiw'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 71_3')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/A-SG4-r6igA'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 71_4')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/-5Q5duCKYIQ'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 71_5')],
    [InlineKeyboardButton(text='Назад', callback_data='7.1 модуль')]
    ])


keyboard_lecture2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/QvkIIGe3kso'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 72_1')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/G5_gGq4Ohu8'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 72_2')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/B5pUrmvyY8M'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 72_3')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/-TYHnF5DX0M'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 72_4')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/qlrMLGx276s'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 72_5')],
    [InlineKeyboardButton(text='Назад', callback_data='7.2 модуль')]
    ])


keyboard_lecture3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Видео 1', url='https://youtu.be/iT7DX8ZQcgM'),
    InlineKeyboardButton(text='Материал 1', callback_data='Материал 73_1')],
    [InlineKeyboardButton(text='Видео 2', url='https://youtu.be/D0M1T3ao1DA'),
    InlineKeyboardButton(text='Материал 2', callback_data='Материал 73_2')],
    [InlineKeyboardButton(text='Видео 3', url='https://youtu.be/4PZMPD8AKBE'),
    InlineKeyboardButton(text='Материал 3', callback_data='Материал 73_3')],
    [InlineKeyboardButton(text='Видео 4', url='https://youtu.be/sNWlPgMB-DY'),
    InlineKeyboardButton(text='Материал 4', callback_data='Материал 73_4')],
    [InlineKeyboardButton(text='Видео 5', url='https://youtu.be/GtGvdIM7Aqk'),
    InlineKeyboardButton(text='Материал 5', callback_data='Материал 73_5')],
    [InlineKeyboardButton(text='Назад', callback_data='7.3 модуль')]
    ])


@router_module_7.callback_query(F.data == 'Лекции7.1')
async def lect_7_1(callback: CallbackQuery):
    await update_BD(callback, "Лекции7.1")
    await callback.message.edit_text("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Лекции7.2')
async def lect_7_2(callback: CallbackQuery):
    await update_BD(callback, "Лекции7.2")
    await callback.message.edit_text("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Лекции7.3')
async def lect_7_3(callback: CallbackQuery):
    await update_BD(callback, "Лекции7.3")
    await callback.message.edit_text("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
    await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 71_1')
async def material_71_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7qmT_aDge8Bp75ikcxJIgpMR45stUAALlOAACunMBSPZUxXeydyBcMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7rGT_aDsWPqDDjI0EuiFqtVcSeyBdAALmOAACunMBSIOx_I4DSLzJMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 71_2')
async def material_71_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7rmT_aF1hPpJb_jblqj0ntZeVOYxhAALoOAACunMBSHqj7uH24TpiMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 71_3')
async def material_71_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7sGT_aHZYeF-2PI7JtzSn8JKWZfUbAALpOAACunMBSBivARjftYiOMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 71_4')
async def material_71_4(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7smT_aIzfezNDWr29nTwj76XF9FNFAALqOAACunMBSMOXhNjhFH0bMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 71_5')
async def material_71_5(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7tGT_aKkeHtnK-liNAWBZ-cLAM15eAALsOAACunMBSDPyOFn1E7vHMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7tmT_aKxbVwq3mxodrDHfn_yaPySJAALtOAACunMBSAn0HVi8IF_sMAQ")
        await callback.message.answer("Раздел лекций 7.1 модуля", reply_markup=keyboard_lecture1)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 72_1')
async def material_72_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7uGT_aNU-keUtZZoAAQVU1-v0h99GyQAC8DgAArpzAUhKxnfB7TVXvzAE")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7umT_aNgbUe32wDJij5R_h8SNg7inAALyOAACunMBSKuM4gxOsSx7MAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 72_2')
async def material_72_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7vGT_aPkJ9SXqY45fHyrTdYlMZo_LAAL0OAACunMBSMIK0_YTYSfKMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7vmT_aPwZhVURx1xpejxqFjfhE4OWAAL1OAACunMBSOxEhvY2LNTVMAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 72_3')
async def material_72_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7wGT_aRkpvk8jHvGFZk3LavwVteqdAAL2OAACunMBSLB-vCWoDOhKMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7wmT_aRvAV6JrIxhUedkwxkZtAk1jAAL3OAACunMBSGszw1FrXVJ7MAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 72_4')
async def material_72_4(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7xGT_aTcVkp9VDKobnquxST-s8HsiAAL4OAACunMBSF4EM84iDqvIMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7xmT_aT2o7rBbyFBI7H7BcO4WeMDjAAL5OAACunMBSFGN65oGdQIAATAE")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 72_5')
async def material_72_5(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7yGT_aVqc5pA54k9mkhKTOpe5_c7lAAL7OAACunMBSMAo5Hej95_QMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7ymT_aV9CNV6FlPOXYnJTekaGiZdIAAL8OAACunMBSJ1atb7QQ8fTMAQ")
        await callback.message.answer("Раздел лекций 7.2 модуля", reply_markup=keyboard_lecture2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_1')
async def material_73_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7zGT_aYElitGkBSUYKZ_hu7WgVnrEAAL_OAACunMBSMyb31wKptf7MAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Материал 73_2')
async def material_73_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ7zmT_aaIlLSVnVL_z53raBCyDsPGRAAIHOQACunMBSGWOYHcehOgLMAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_3')
async def material_73_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ70GT_aamd4RFl8hr0ws9KYptEPSb0AAIJOQACunMBSJGDr_CDWOw1MAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_4')
async def material_73_4(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ70mT_aasjiHiRGub75U_AD0RqhLceAAIKOQACunMBSIGvml-vWkE-MAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Материал 73_5')
async def material_73_5(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ71GT_abDDPGvmQBDf9-g4fy46FaRyAAILOQACunMBSG51cq0YkNc_MAQ")
        await callback.message.answer("Раздел лекций 7.3 модуля", reply_markup=keyboard_lecture3)
        await callback.answer()
        

keyboard_labs1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 71_1')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 71_2')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 71_3')],
    [InlineKeyboardButton(text='Назад', callback_data='7.1 модуль')]
    ])


keyboard_labs2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 72_1')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 72_2')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 72_3')],
    [InlineKeyboardButton(text='Назад', callback_data='7.2 модуль')]
    ])


keyboard_labs3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Лабораторная работа 1', callback_data='Лабораторная работа 73_1')],
    [InlineKeyboardButton(text='Лабораторная работа 2', callback_data='Лабораторная работа 73_2')],
    [InlineKeyboardButton(text='Лабораторная работа 3', callback_data='Лабораторная работа 73_3')],
    [InlineKeyboardButton(text='Назад', callback_data='7.3 модуль')]
    ])


@router_module_7.callback_query(F.data == 'Материал лаб. работ7.1')
async def lect_71(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ7.1")
    await callback.message.edit_text("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Материал лаб. работ7.2')
async def lect_72(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ7.2")
    await callback.message.edit_text("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
    await callback.answer()
    

@router_module_7.callback_query(F.data == 'Материал лаб. работ7.3')
async def lect_73(callback: CallbackQuery):
    await update_BD(callback, "Материал лаб. работ7.3")
    await callback.message.edit_text("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
    await callback.answer()
    
   
@router_module_7.callback_query(F.data == 'Лабораторная работа 71_1')
async def lab_71_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8KmT_aqDy0qhVaaF-1RDqVbG9ewlaAAIWOQACunMBSK3rqiDLmlreMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8LGT_aqN2IogUDZDAT7g5AdUUbn91AAIXOQACunMBSD0-sZnRHgKFMAQ")
        await callback.message.answer("https://youtu.be/djuHlDYccCU")
        await callback.message.answer("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Лабораторная работа 71_2')
async def lab_71_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8LmT_aqmA55HJry00DKMdgXZLHIJlAAIZOQACunMBSFS_1ofN0YE6MAQ")
        await callback.message.answer("https://youtu.be/p_jBR4y351g")
        await callback.message.answer("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 71_3')
async def lab_71_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8MGT_aq8jLITo_ElDv8uQwbuEiT0fAAIaOQACunMBSNVJDLVv-wNSMAQ")
        await callback.message.answer("https://youtu.be/ut2GMNxxpC4")
        await callback.message.answer("Раздел лабораторных работ 7.1 модуля", reply_markup=keyboard_labs1)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 72_1')
async def lab_72_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8MmT_avjJEkyubu9mV4qeC5LjumyVAAIbOQACunMBSAJFuYzog54WMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8NGT_avtHx-zPHSxnvRzpDZkjhkfWAAIcOQACunMBSPfcIg62rVbHMAQ")
        await callback.message.answer("https://youtu.be/mzZMdc-jLqQ")
        await callback.message.answer("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Лабораторная работа 72_2')
async def lab_72_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8NmT_av0OvOpHfD2QZbjvpc3PPMVSAAIdOQACunMBSCyqibrND45zMAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8OGT_awABdVP1igPO4TkuOGr9iYZe8gACHjkAArpzAUiXDmOWp7iwjTAE")
        await callback.message.answer("https://youtu.be/mOYpukKC-Uc")
        await callback.message.answer("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 72_3')
async def lab_72_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8OmT_axFTwK1dTXY8lbKrFaXorXoRAAIfOQACunMBSLTtSEFY9AH1MAQ")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8PGT_axQM-IELuBqsXl-eu744EQ7wAAIgOQACunMBSHJf8egMFnXFMAQ")
        await callback.message.answer("https://youtu.be/Q14Rc_QsEUE")
        await callback.message.answer("Раздел лабораторных работ 7.2 модуля", reply_markup=keyboard_labs2)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 73_1')
async def lab_73_1(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8PmT_a1g9mnBovmON2rpXI31hPW3eAAIhOQACunMBSHKhDCy7vQTKMAQ")
        await callback.message.answer("https://youtu.be/afUQcFZOYfY")
        await callback.message.answer("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
        await callback.answer()


@router_module_7.callback_query(F.data == 'Лабораторная работа 73_2')
async def lab_73_2(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8QGT_a1rFQAKKjEtxSvWH2ZuYgOHdAAIiOQACunMBSHO4kK2fDnD1MAQ")
        await callback.message.answer("https://youtu.be/T-Kvj3ibRjM")
        await callback.message.answer("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
        await callback.answer()
        

@router_module_7.callback_query(F.data == 'Лабораторная работа 73_3')
async def lab_73_3(callback: CallbackQuery):
    try:
        await callback.message.delete()
    except:
        pass
    finally:
        await callback.message.answer("Подождите, файл загружается")
        await callback.message.answer_document(document="BQACAgIAAxkBAAJ8QmT_a1wQyf92n9VLbN-q0JuK6lt3AAIjOQACunMBSDNj9r_Ac-zOMAQ")
        await callback.message.answer("https://youtu.be/hY7QRLHvl0Q")
        await callback.message.answer("Раздел лабораторных работ 7.3 модуля", reply_markup=keyboard_labs3)
        await callback.answer()