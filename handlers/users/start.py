from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, i18n

_ = i18n.gettext



@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(_('Привет, {full_name}!').format(full_name=message.from_user.full_name))
    print(message.from_user.language_code)
    print(message.from_user.locale)


@dp.message_handler(commands='lang')
async def cmd_lang(message: types.Message):
    await message.reply(_('Your current language: <i>{language}</i>').format(language=message.from_user.language_code))


@dp.message_handler(text='/cv')
async def bot_start(message: types.Message):
    await message.answer(("Запрос CV"))


@dp.message_handler(text='/contact')
async def bot_start(message: types.Message):
    await message.answer(("Контакты"))
