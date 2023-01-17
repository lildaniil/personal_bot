from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from gino import Gino

from data import config
# from utils.db_api.db_gino import db

from middlewares.language import I18nMiddleware
from data.config import LOCALES_DIR, I18N_DOMAIN


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR, default="en")

# i18n = dp.middleware.applications
# _ = i18n.gettext
# __ = i18n.lazy_gettext
 