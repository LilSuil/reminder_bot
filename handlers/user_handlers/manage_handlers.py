from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from keyboards import create_foldersManageMenu_keyboard, create_NotionsManageMenu_keyboard, create_ReminderManageMenu_keyboard
from loader import redisClient


manageRouter = Router()

# ---------------------------------------------------------------------------------------------------------------

# In this block: There are handlers: folder list , check folder (in interactive router: create folder, choose folder, delete folder).
@manageRouter.message(F.text == 'Folders management 📁')
async def procces_FoldersManagement_handler(message: Message):
    await message.answer('<b>Folders manage menu:</b>', reply_markup=create_foldersManageMenu_keyboard())


# ---------------------------------------------------------------------------------------------------------------

# In this block: There are handlers: read notion (in interactive router: create notion, delete notion, redact notion).
@manageRouter.message(F.text == 'Notions management 📄')
async def procces_NotionsManagement_handler(message: Message):
    await message.answer('<b>Notions manage menu:</b>', reply_markup=create_NotionsManageMenu_keyboard())

# ---------------------------------------------------------------------------------------------------------------

# In this block: There are handlers: Check Reminds (in interactive router: create remind, delete remind)
@manageRouter.message(F.text == 'Reminder management ⏰')
async def procces_ReminderManagement_handler(message: Message):
    await message.answer('<b>Reminder manage menu:</b>', reply_markup=create_ReminderManageMenu_keyboard())

# ---------------------------------------------------------------------------------------------------------------
