import asyncio
import logging
from loader import bot, dp
from handlers import remindRouter, interactiveRouter, writeRouter, adminRouter, otherRouter
from database import redisClient
# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    logger.info('Starting bot')
    dp.include_routers(remindRouter, interactiveRouter, writeRouter, adminRouter, otherRouter)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
