from aiogram import Router
from aiogram.filters import Command, and_f
from aiogram.types import Message
from filters import IsAdmin
from loader import admin_list, redisClient, config

from keyboards import create_admin_interface
from services import DbServices


from database import metadata, init_tables


adminRouter: Router = Router()
ch_id: str


# ----------------------------------------------------------------------------------------

@adminRouter.message(and_f(Command(commands=['admin']), IsAdmin(admin_list)))
async def procces_OpenAdminPanel_handler(message: Message):
    await message.answer(text='admin', reply_markup=create_admin_interface())


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
@adminRouter.message(and_f(Command(commands=['getusers']), IsAdmin(admin_list)))
async def procces_GetUsers_handler(message: Message):
    users = await DbServices().get_users_list()
    user_list = ', '.join(users)

    if user_list:
        await message.answer('All available users 😊: \n' + user_list)
    else:
        await message.answer('No users found. 😔')


# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------

@adminRouter.message(and_f(Command(commands=['registerdb']), IsAdmin(admin_list)))
async def procces_TestCommand_handler(message: Message):
    if await redisClient.get('postgresDB_check') is not None:
        await message.answer('Your DB are already registered')

    else:

        db_name = config.pg_db_name.get_secret_value()

        await init_tables(db_name=db_name, meta_data=metadata)
        await message.answer('DB is success registered!')
        await redisClient.set(name='postgresDB_check', value='checked')

# ----------------------------------------------------------------------------------------
