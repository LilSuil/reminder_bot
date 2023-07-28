from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon import LEXICON_RU
from services import DbServices
from keyboards import create_startMenu_keyboard

interactiveRouter: Router = Router()


@interactiveRouter.message(CommandStart())
async def procces_StartCommand_handler(message: Message):
    await message.answer(text=LEXICON_RU['start'], reply_markup=create_startMenu_keyboard())
    await DbServices().collectUser_in_DB(message.from_user.id)


@interactiveRouter.message(Command(commands=['help']))
async def procces_HelpCommand_handler(message: Message):
    await message.answer(text=LEXICON_RU['help'])
