import datetime

from database import redisClient, users_main_data, users_serialized_data, get_async_engine
from services.serialize_services import SerializeServices
from aiogram.types import Message
from loader import config
from sqlalchemy import insert, select


class DbServices:

    def __init__(self):
        self.db_name = config.pg_db_name.get_secret_value()

    @staticmethod
    async def collectUser_in_DB(user_id) -> None:
        await redisClient.sadd('USERS', user_id)

    @staticmethod
    async def get_users_list() -> list:
        susers = list(await redisClient.smembers('USERS'))
        users = [user.decode('utf-8') for user in susers]

        return users

    async def collect_user_data(self, message: Message, table_1=users_main_data, table_2=users_serialized_data,
                                engine=None) -> None:
        engine = await get_async_engine(self.db_name)
        # first table data
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        user_id = message.from_user.id
        current_folder = 'None'
        register_date = datetime.datetime.now()

        # second table data
        user_id = message.from_user.id
        notion_data = await SerializeServices().serialize({})
        remind_data = await SerializeServices().serialize({})

        async with engine.begin() as conn:
            await conn.execute(
                insert(table_1).values(
                    user_id=user_id,
                    register_time=register_date,
                    first_name=first_name,
                    last_name=last_name,
                    current_folder=current_folder
                )
            )

            # Вставляем данные в таблицу users_serialized_data (table_2)
            await conn.execute(
                insert(table_2).values(
                    user_id=user_id,
                    notions_data_serialized=notion_data,
                    remind_data_serialized=remind_data
                )
            )

    async def get_user_data(self, user_id, table_1=users_main_data, table_2=users_serialized_data, engine=None):
        engine = await get_async_engine(self.db_name)
        async with engine.connect() as conn:
            # Определяем объекты столбцов, которые нужны из таблицы users_main_data (table_1)
            columns_table_1 = [
                table_1.c.user_id,
                table_1.c.register_time,
                table_1.c.first_name,
                table_1.c.last_name,
                table_1.c.current_folder
            ]

            # Определяем объекты столбцов, которые нужны из таблицы users_serialized_data (table_2)
            columns_table_2 = [
                table_2.c.user_id,
                table_2.c.notions_data_serialized,
                table_2.c.remind_data_serialized
            ]

            # Запрос данных из таблицы users_main_data (table_1) для указанного user_id
            query_table_1 = select(*columns_table_1).where(table_1.c.user_id == user_id)
            result_table_1 = await conn.execute(query_table_1)
            user_data_table_1 = result_table_1.fetchone()

            # Запрос данных из таблицы users_serialized_data (table_2) для указанного user_id
            query_table_2 = select(*columns_table_2).where(table_2.c.user_id == user_id)
            result_table_2 = await conn.execute(query_table_2)
            user_data_table_2 = result_table_2.fetchone()

            return user_data_table_1, user_data_table_2
