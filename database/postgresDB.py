from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from sqlalchemy import MetaData, Table, Column, String, Integer, LargeBinary, DateTime
from loader import config


pg_db_username = config.pg_db_username.get_secret_value()
pg_db_name = config.pg_db_name.get_secret_value()
pg_db_password = config.pg_db_password.get_secret_value()
pg_db_host = config.pg_db_host.get_secret_value()

metadata = MetaData()

users_main_data = Table(
    "users_main_data",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("register_time", DateTime),
    Column("first_name", String(50)),
    Column("last_name", String(50)),
    Column("current_folder", String(100))
)

users_serialized_data = Table(
    "users_serialized_data",
    metadata,
    Column("user_id", Integer, primary_key=True),
    Column("notions_data_serialized", LargeBinary),
    Column("remind_data_serialized", LargeBinary)
)


async def get_async_engine(db_name: str) -> AsyncEngine:
    engine = create_async_engine(
        f"postgresql+asyncpg://{pg_db_username}:{pg_db_password}@{pg_db_host}/{db_name}"
    )

    return engine

async def init_tables(db_name: str, meta_data: MetaData) -> None:
    engine = await get_async_engine(db_name)

    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)








