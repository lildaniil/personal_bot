from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

from utils.db_api import commands
from utils.stat.set_stats import set_stat_data


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    # add user into db 
    if await commands.select_user(message.from_user.id) == None:
        print("New user")
        await commands.add_user(
            id = message.from_user.id,
            first_name = message.from_user.first_name,
            last_name = message.from_user.last_name,
            username = message.from_user.username,
            language_code = message.from_user.language_code,
            is_bot = message.from_user.is_bot,
            is_premium = message.from_user.is_premium,
            added_to_attachment_menu = message.from_user.added_to_attachment_menu,
            can_join_groups = message.from_user.can_join_groups,
            can_read_all_group_messages = message.from_user.can_read_all_group_messages,
            supports_inline_queries = message.from_user.supports_inline_queries
            )

        await set_stat_data(
            user_id=message.from_user.id,
            action='start',
            action_data='new user'
            )
    else: await set_stat_data(
            user_id=message.from_user.id,
            action='start'
            )


    await message.answer(f"Привет, {message.from_user.full_name}!\nЭто персональный ассистент, по совместительству бот.\nТы можешь запросить CV /cv , контакты /contact или просто порешать глупые тестики")


@dp.message_handler(text='/cv')
async def cv_require(message: types.Message):

    # collecting stats
    await set_stat_data(
            user_id=message.from_user.id,
            action='cv_require'
            )

    await message.answer(f"Секунду..")
    await message.bot.send_document(message.from_id, open('data/files/resume.pdf', 'rb'))


@dp.message_handler(text='/contact')
async def contact_require(message: types.Message):

    # collecting stats
    await set_stat_data(
            user_id=message.from_user.id,
            action='contact_require'
            )

    await message.answer(f"Контакты: \n")
    await message.answer(f"""
<a href="https://www.linkedin.com/in/daniil-agalakov/">работа</a>
<a href="https://www.t.me/lildaniil">чат</a>
<a href="https://www.instagram.com/daniilthecreator/">картинки</a>
    """)
