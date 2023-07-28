from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_RU


def create_admin_interface() -> ReplyKeyboardMarkup:
    buttons = []

    button_FlushDB: KeyboardButton = KeyboardButton(text='/flushdb')
    button_GetUsers: KeyboardButton = KeyboardButton(text='/getusers')
    button_GetData: KeyboardButton = KeyboardButton(text='/getdata')
    button_Test: KeyboardButton = KeyboardButton(text='/test')
    button_BackStart: KeyboardButton = KeyboardButton(text='Back to start')

    buttons.append([[button_FlushDB, button_GetUsers], [button_GetData, button_Test], [button_BackStart]])

    admin_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(

        keyboard=[
            buttons[0][0],
            buttons[0][1],
            buttons[0][2]
        ],
        resize_keyboard=True,
    )

    return admin_kb


def create_confirmFlushDB_kb(*buttons) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    kb_builder.row(*[InlineKeyboardButton(
        text=LEXICON_RU[button], callback_data=button) for button in buttons])

    return kb_builder.as_markup()
