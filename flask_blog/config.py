import os
from dotenv import load_dotenv

load_dotenv(r'C:\Users\petr\my_env\.env')
password = os.getenv('EMAIL_YA_PASS')

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "pontiaciv@yandex.ru"
    MAIL_PASSWORD = password
