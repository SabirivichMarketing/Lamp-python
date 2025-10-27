import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('1231788061:AAE-czpea-vvG6tDnUA9EILwxB97OreONmM')
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'mysql'),
    'user': os.getenv('DB_USER', 'botuser'),
    'password': os.getenv('DB_PASSWORD', 'botpassword'),
    'database': os.getenv('DB_NAME', 'telegram_bot')
}