from aiogram import Router, types
from aiogram.filters import Command
from logger_config import get_logger
from keyboards.main_menu import get_main_menu


# Тут будут импорты кнопок
# ----------------------------

from datetime import date


# Тут нужны будут запросы в БД


# Система логирования
logger = get_logger(__name__)

# Добавляем роутер
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):

    # Получаем данные пользователя (потом будет проверка на уникальность)
    telegram_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    welcome_text = (f"👋 Привет, {first_name or 'друг'}!\n")

    # Отправляем приветственное сообщение с меню
    await message.answer(text=welcome_text, reply_markup=get_main_menu())

@router.message(Command("help"))
async def cmd_help(message:types.Message):
    help_text = (
        f"Эта команда описывает основные команды бота\n"
        "⚡ Доступные команды:\n"
        "Пока многие функции находятся в разработке"
    )

    await message.answer(text=help_text, reply_markup=get_main_menu())