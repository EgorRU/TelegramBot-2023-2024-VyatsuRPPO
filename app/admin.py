from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3
from other import update_BD
from config import ADMIN_API,  TOKEN_WORK_BOT


router_admin = Router()
bot = Bot(token=TOKEN_WORK_BOT)


@router_admin.message(F.text == '/info')
async def info(message: Message):
    if message.from_user.id == ADMIN_API:
        await message.answer(
            "Курс-хаб: https://e.vyatsu.ru/course/view.php?id=29027",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 2: https://drive.google.com/drive/folders/1lOybjbCFDXdQjDB2rw2HZFl6kpUVycuc",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 3: https://drive.google.com/drive/folders/1FHNdVC5VlmmIQCxxAnHmftTkFvSDwYQ1",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 4: https://drive.google.com/drive/folders/1jKZ5cMgJGQcLsC2Q5lpfUzViVF--6hsI",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 5: https://drive.google.com/drive/folders/1ag4Vn-A7ijx_EyLTKMztl1kSOWH7xyqd",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 6: https://drive.google.com/drive/folders/1cRElanzq1K1NIBCHfXFRvRdhFlNGzmra",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 7.1: https://drive.google.com/drive/folders/1eEqgYfOa_JG_TNPln_Bolp002jxEh582",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 7.2: https://drive.google.com/drive/folders/1-UX4uQNZU40WIUIZgN8E2P0Lwz9EzCVZ",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 7.3: https://drive.google.com/drive/folders/1sAbnRzJdAY8dCx-yJTgvO-JHs5k4Jaeg",
            disable_web_page_preview=True,
        )
        await message.answer(
            "Гугл диск 8: https://drive.google.com/drive/folders/1sseDW4dGC8r8ZZ8Osu4V3O70aEC0CcCC",
            disable_web_page_preview=True,
        )
    else:
        await message.answer("Недостаточно прав")


@router_admin.message(F.text.startswith("/add"))
async def add(message: Message):
    if message.from_user.id == ADMIN_API:
        id_user = int(message.text.split()[1])
        base = sqlite3.connect("database.db")
        cur = base.cursor()
        id_user_from_db = cur.execute(f"SELECT id FROM registration_data WHERE id={id_user}").fetchone()
        if id_user_from_db != None:
            cur.execute("UPDATE registration_data SET active==? WHERE id=?",("2", id_user))
            base.commit()
            await message.answer("Успешно")
        else:
            await message.answer("Такого пользователя нет")
    else:
        await message.answer("Недостаточно прав")
        

@router_admin.message(F.text.startswith("/remove"))
async def remove(message: Message):
    if message.from_user.id == ADMIN_API:
        id_user = int(message.text.split()[1])
        base = sqlite3.connect("database.db")
        cur = base.cursor()
        id_user_from_db = cur.execute(f"SELECT id FROM registration_data WHERE id={id_user}").fetchone()
        if id_user_from_db != None:
            cur.execute("UPDATE registration_data SET active==? WHERE id=?",("1", id_user))
            base.commit()
            await message.answer("Успешно")
        else:
            await message.answer("Такого пользователя нет")
    else:
        await message.answer("Недостаточно прав")
        

@router_admin.message(F.text.startswith("/message"))
async def remove(message: Message):
    if message.from_user.id == ADMIN_API:
        message_text = message.text[8:]
        base = sqlite3.connect("database.db")
        cur = base.cursor()
        user_from_db = cur.execute(f"SELECT id FROM registration_data").fetchall()
        for val in user_from_db:
            id_user = int(val[0])
            try:
                await bot.send_message(id_user, message_text)
            except:
                cur.execute("UPDATE registration_data SET active==? WHERE id=?",("0", id_user))
                base.commit()
        await message.answer("Рассылка прошла успешно")
    else:
        await message.answer("Недостаточно прав")
        
    
@router_admin.message(F.document)
async def get_document(message: Message):
    if message.from_user.id == ADMIN_API:
        await message.answer(message.document.file_id)