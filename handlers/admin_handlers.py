from aiogram import Router, F
from aiogram.filters import Command, and_f, StateFilter
from aiogram.types import Message, CallbackQuery
from filters import IsAdmin, CheckDB
from loader import admin_list, redisClient, bot
from states import FSM_FillUserID
from aiogram.fsm.context import FSMContext
from keyboards import create_confirmFlushDB_kb, create_admin_interface, create_cancel_keyboard
from services import DbServices, SerializeServices
from lexicon import LEXICON_RU

adminRouter: Router = Router()
ch_id: str


# ----------------------------------------------------------------------------------------

@adminRouter.message(and_f(Command(commands=['admin']), IsAdmin(admin_list)))
async def procces_OpenAdminPanel_handler(message: Message):
    await message.answer(text='admin', reply_markup=create_admin_interface())


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
@adminRouter.message(and_f(Command(commands=['flushdb']), IsAdmin(admin_list)))
async def procces_FlushDb_handler(message: Message):
    global ch_id
    await message.answer('Are you sure you want to clear the database?',
                         reply_markup=create_confirmFlushDB_kb('confirm', 'denied'))
    ch_id = message.chat.id


@adminRouter.callback_query(lambda callback: callback.data in ['confirm', 'denied'])
async def procces_ProccesCheckFlushDbAnswer_handler(callback: CallbackQuery):
    global ch_id
    match callback.data:

        case 'confirm':

            await redisClient.flushdb()
            await callback.answer('DB is flushed')
            await bot.delete_message(message_id=callback.message.message_id, chat_id=ch_id)

        case 'denied':
            await callback.answer('DB flushing canceled')
            await bot.delete_message(message_id=callback.message.message_id, chat_id=ch_id)

        case _:
            await bot.delete_message(message_id=callback.message.message_id, chat_id=ch_id)


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
@adminRouter.message(and_f(Command(commands=['getdata']), IsAdmin(admin_list), CheckDB(redisClient)))
async def procces_GetUserID_handler(message: Message, state: FSMContext):
    await message.answer('Enter user ID:', reply_markup=create_cancel_keyboard())
    await state.set_state(FSM_FillUserID.state_UserID)

@adminRouter.message(and_f(Command(commands=['getdata']), IsAdmin(admin_list), ~CheckDB(redisClient)))
async def procces_GetUserID_handler(message: Message):
    await message.answer('DB is empty')
@adminRouter.message(and_f(StateFilter(FSM_FillUserID.state_UserID), lambda message: int(message.text.isdigit())))
async def procces_PrintUserData_handler(message: Message, state: FSMContext):
    await state.update_data(us_id=message.text)
    data = await state.get_data()
    if data['us_id'] in await DbServices().get_users_list():
        await message.answer(
            str((await SerializeServices().deserialize(await redisClient.get(f'USER_DATA-' + data['us_id'])))))
    else:
        await message.answer('User not found')
    await state.clear()

@adminRouter.message(and_f(StateFilter(FSM_FillUserID.state_UserID), F.text == 'Cancel ❌'))
async def procces_CancelGetUserData_handler(message: Message, state: FSMContext):
    await message.answer('<b>Procces canceled ❌</b>', reply_markup=create_admin_interface())
    await state.clear()

@adminRouter.message(and_f(StateFilter(FSM_FillUserID.state_UserID), lambda message: not (int(message.text.isdigit()))))
async def procces_IncorrectUserIdLetters_handler(message: Message):
    await message.answer(text=LEXICON_RU['UserID_Error'])


# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------
@adminRouter.message(and_f(Command(commands=['test']), IsAdmin(admin_list)))
async def procces_TestCommand_handler(message: Message):
    print(message.from_user.id)
# ----------------------------------------------------------------------------------------
