import logging
import sys

def setup_logging():
    """Настройка глобального логирования"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler("bot.log", encoding="utf-8")  # также запись в файл
        ]
    )

def get_logger(name: str):
    """Получение логгера с именем модуля"""
    return logging.getLogger(name)

# Автоматическая настройка при импорте
setup_logging()