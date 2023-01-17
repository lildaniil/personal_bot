from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

from aiogram.contrib.middlewares import i18n

_ = i18n.gettext


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = (_("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку"))
    
    await message.answer("\n".join(text))
