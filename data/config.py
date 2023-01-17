from environs import Env
from pathlib import Path

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

# Main
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

# DB
PGUSER=env.str("PGUSER")
PGPASSWORD=env.str("PGPASSWORD")
DATABASE=env.str("DATABASE")

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'

# Locales
I18N_DOMAIN='testbot'
BASE_DIR=Path(__file__).parent.parent
LOCALES_DIR=BASE_DIR/'utils/locales'