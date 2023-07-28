from aiogram import Router
from aiogram.methods import DeleteMessage

from aiogram.filters import Command, and_f
from aiogram.types import Message, CallbackQuery
from filters import IsAdmin, CheckDB
from loader import admin_list, redisClient, bot
from services import SerializeServices
from keyboards import create_confirmFlushDB_kb, create_admin_interface

adminRouter: Router = Router()

# ----------------------------------------------------------------------------------------
m_id: str
ch_id: str

@adminRouter.message(and_f(Command(commands=['admin']), IsAdmin(admin_list)))
async def procces_OpenAdminPanel_handler(message: Message):
    await message.answer(text='admin', reply_markup=create_admin_interface())


@adminRouter.message(and_f(Command(commands=['flushdb']), IsAdmin(admin_list)))
async def procces_FlushDb_handler(message: Message):
    global m_id, ch_id

    await message.answer('Are you sure you want to clear the database?',
                         reply_markup=create_confirmFlushDB_kb('confirm', 'denied'))

    m_id = message.message_id + 1
    ch_id = message.chat.id


@adminRouter.callback_query(lambda callback: callback.data in ['confirm', 'denied'])
async def procces_ProccesCheckFlushDbAnswer_handler(callback: CallbackQuery):
    global m_id, ch_id

    match callback.data:

        case 'confirm':

            await redisClient.flushdb()
            await callback.answer('DB is flushed')
            await bot.delete_message(message_id=m_id, chat_id=ch_id)

        case 'denied':
            await callback.answer('DB flushing canceled')
            await bot.delete_message(message_id=m_id, chat_id=ch_id)

        case _:
            await bot.delete_message(message_id=m_id, chat_id=ch_id)


# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
@adminRouter.message(and_f(Command(commands=['getusers']), IsAdmin(admin_list)))
async def procces_GetUsers_handler(message: Message):
    susers = list(await redisClient.smembers('USERS'))
    users = [user.decode('utf-8') for user in susers]
    user_list = ', '.join(users)

    if user_list:
        await message.answer('All available users 😊: \n' + user_list)
    else:
        await message.answer('No users found. 😔')


# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
@adminRouter.message(and_f(Command(commands=['getdata']), IsAdmin(admin_list), CheckDB(redisClient)))
async def procces_GetData_handler(message: Message):
    await message.answer(
        str((await SerializeServices().deserialize(await redisClient.get(f'USER_DATA-{message.from_user.id}')))))


# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------


@adminRouter.message(and_f(Command(commands=['test']), IsAdmin(admin_list)))
async def procces_TestCommand_handler(message: Message):
    pass
# ----------------------------------------------------------------------------------------
