from aiogram import Router
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


otherRouter: Router = Router()

@otherRouter.message()
async def procces_NotExpectedMessage_handler(message: Message):
    await message.answer('i dont understand u')
