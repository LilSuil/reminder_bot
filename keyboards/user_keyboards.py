from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon import LEXICON_RU


def create_cancel_keyboard() -> ReplyKeyboardMarkup:
    buttons = []

    button_Cancel: KeyboardButton = KeyboardButton(text='Cancel ❌')

    buttons.append([[button_Cancel]])

    cancel_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            buttons[0][0]
        ],
        resize_keyboard=True
    )

    return cancel_kb


def create_startMenu_keyboard() -> ReplyKeyboardMarkup:
    buttons = []

    button_Test: KeyboardButton = KeyboardButton(text='/test')
    buttons.append([[button_Test]])

    start_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            buttons[0][0],
        ],
        resize_keyboard=True,
    )

    return start_kb
