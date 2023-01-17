from asyncpg import UniqueViolationError

from utils.db_api.schema.user import User
from utils.db_api.schema.stat import Statistic
from utils.db_api.db_gino import db


# 
# USER COMMANDS
# 

async def add_user(
    id:int,
    first_name:str, 
    last_name:str, 
    username:str,
    language_code:str,
    is_bot:str,
    is_premium:bool,
    added_to_attachment_menu:bool,
    can_join_groups:bool,
    can_read_all_group_messages:bool,
    supports_inline_queries:bool
    ):
    
    try:
        user = User(
            id=id, 
            first_name=first_name, 
            last_name=last_name, 
            username=username,
            language_code=language_code,
            is_bot = is_bot,
            is_premium=is_premium,
            added_to_attachment_menu=added_to_attachment_menu,
            can_join_groups=can_join_groups,
            can_read_all_group_messages=can_read_all_group_messages,
            supports_inline_queries=supports_inline_queries
            )

        await user.create()

    except UniqueViolationError:
        pass


async def select_all_users():

    users = await User.query.gino.all()
    return users


async def select_user(id:int):
    
    user = await User.query.where(User.id == id).gino.first()

    return user


async def count_users():

    total = await db.func.count(User.id).gino.scalar()


async def update_user_email(id, username):
    
    user = await User.get(id)

    await user.update(username=username).apply()



# 
# STATISTIC COMMANDS
# 


async def add_stat(
    # id:int,
    user_id:int,
    action:str,
    action_data:str = None
    ):

    try:
        stat = Statistic(
            user_id=user_id,
            action=action,
            action_data=action_data
        )

        await stat.create()

    except UniqueViolationError:
        pass