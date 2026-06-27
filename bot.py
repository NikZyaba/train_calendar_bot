# Основной файл запуска
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault
import asyncio
from dotenv import load_dotenv
from logger_config import get_logger

# Загружаю переменные окружения
load_dotenv()

logger = get_logger(__name__)


# Возможно тут будут миграции с применением alembic


# Создаем команды для бота (в начале (режим разработки, потом удалим)
async def set_commands_bot(bot: Bot):
    """Установка команд бота"""
    commands = [BotCommand(command="start", description="Запустить бота"),
                BotCommand(command="help", description="Описание бота")
                ]
    await bot.set_my_commands(commands=commands)


# Действия при запуске бота
async def on_startup(bot: Bot):
    """Действия при запуске бота"""
    await set_commands_bot(bot=bot)
    logger.info("✅ Бот готов к работе!")


# Основная функция запуска бота

async def main():
    """Основная функция запуска бота"""
    bot = Bot(token=os.getenv("TOKEN"))
    storage = MemoryStorage()
    dp = Dispatcher()

    # Регистрируем обработчик запуска
    dp.startup.register(on_startup)

    logger.info("Бот готов к запуску")

    try:
        # Регистрация роутеров
        from handlers.start import router as start_router

        dp.include_router(start_router)

        logger.info("✅ Роутеры зарегистрированы")
        # Конец регистрации роутеров
    except Exception as e:
        logger.error(f"❌ Ошибка при загрузке роутеров: {e}")

    logger.info("🚀 Запуск бота...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
