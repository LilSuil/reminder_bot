from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

writeRouter = Router()

@writeRouter.message(F.text == 'Folders management 📁')
async def procces_FoldersManagement_handler(message: Message):
    await message.answer('good')

@writeRouter.message(F.text == 'Notions management 📄')
async def procces_NotionsManagement_handler(message: Message):
    await message.answer_dice()