from keyboards import create_startMenu_keyboard
from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon import LEXICON_RU

otherRouter: Router = Router()


@otherRouter.message(F.text == 'Back to start')
async def procces_BackToStart_handler(message: Message):
    await message.answer(LEXICON_RU['Back to start'], reply_markup=create_startMenu_keyboard())


@otherRouter.message()
async def procces_NotExpectedMessage_handler(message: Message):
    await message.answer(LEXICON_RU['other_message'])
