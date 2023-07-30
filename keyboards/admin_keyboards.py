from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_RU


def create_admin_interface() -> ReplyKeyboardMarkup:
    buttons = []

    button_GetUsers: KeyboardButton = KeyboardButton(text='/getusers')
    button_RegisterDB: KeyboardButton = KeyboardButton(text='/registerdb')
    button_BackStart: KeyboardButton = KeyboardButton(text='Back to start')

    buttons.append([[button_RegisterDB, button_GetUsers], [button_BackStart]])

    admin_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(

        keyboard=[
            buttons[0][0],
            buttons[0][1],
        ],
        resize_keyboard=True,
    )

    return admin_kb
