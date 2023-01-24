from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЭто персональный ассистент, по совместительству бот.\nТы можешь запросить CV /cv , контакты /contact или просто порешать глупые тестики")


@dp.message_handler(text='/cv')
async def bot_start(message: types.Message):
    await message.answer(f"Секунду..")
    await message.bot.send_document(message.from_id, open('data/files/resume.pdf', 'rb'))


@dp.message_handler(text='/contact')
async def bot_start(message: types.Message):
    await message.answer(f"Контакты: \n")
    await message.answer(f"""
<a href="https://www.linkedin.com/in/daniil-agalakov/">Работа</a>
<a href="https://www.t.me/lildaniil">Написать</a>
<a href="https://www.instagram.com/daniilthecreator/">Картинки</a>
    """)
