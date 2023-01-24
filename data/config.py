from environs import Env

env = Env()
env.read_env()

# Main settings
BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста

# DB
PGUSER=env.str("PGUSER")
PGPASSWORD=env.str("PGPASSWORD")
DATABASE=env.str("DATABASE")

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'