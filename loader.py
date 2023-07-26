from config_data import load_config, Config
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis


config: Config = load_config('misc/.env')
bot: Bot = Bot(token=config.bot_token.get_secret_value(), parse_mode='HTML')

redisClient = Redis(db=1)
redisStorage: RedisStorage = RedisStorage(redis=redisClient)

dp: Dispatcher = Dispatcher(storage=redisStorage)

