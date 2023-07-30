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

    button_FoldersManagement: KeyboardButton = KeyboardButton(text='Folders management 📁')
    button_NotionsManagement: KeyboardButton = KeyboardButton(text='Notions management 📄')
    button_RemindersManagement: KeyboardButton = KeyboardButton(text='Reminder management ⏰')

    buttons.append([[button_FoldersManagement, button_NotionsManagement], [button_RemindersManagement]])

    start_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            buttons[0][0],
            buttons[0][1],
        ],
        resize_keyboard=True,
    )

    return start_kb


def create_foldersManageMenu_keyboard() -> ReplyKeyboardMarkup:
    buttons = []

    button_FolderCreate: KeyboardButton = KeyboardButton(text='Create Folder 📂')
    button_FolderDelete: KeyboardButton = KeyboardButton(text='Delete Folder ❌')
    button_FolderList: KeyboardButton = KeyboardButton(text='Folder list 📒')
    button_FolderCheck: KeyboardButton = KeyboardButton(text='Check folder 🔍')
    button_ChooseFolder: KeyboardButton = KeyboardButton(text='Choose folder 📌')
    button_GoToStartMenu: KeyboardButton = KeyboardButton(text='Back to start')

    buttons.append(
        [[button_FolderCreate, button_ChooseFolder, button_FolderDelete], [button_FolderList, button_FolderCheck],
         [button_GoToStartMenu]])

    folders_mg_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(

        keyboard=[

            buttons[0][0],
            buttons[0][1],
            buttons[0][2],

        ],
        resize_keyboard=True
    )

    return folders_mg_kb


def create_NotionsManageMenu_keyboard() -> ReplyKeyboardMarkup:
    buttons = []

    button_NotionCreate: KeyboardButton = KeyboardButton(text='Create notion ✏️')
    button_NotionDelete: KeyboardButton = KeyboardButton(text='Delete notion ❌')
    button_NotionRead: KeyboardButton = KeyboardButton(text='Read notion 🔎')
    button_NotionRedact: KeyboardButton = KeyboardButton(text='Redact notion 📝')
    button_GoToStartMenu: KeyboardButton = KeyboardButton(text='Back to start')

    buttons.append(
        [[button_NotionCreate, button_NotionRead, button_NotionDelete], [button_NotionRedact], [button_GoToStartMenu]])

    notions_mg_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            buttons[0][0],
            buttons[0][1],
            buttons[0][2],

        ],
        resize_keyboard=True
    )
    return notions_mg_kb


def create_ReminderManageMenu_keyboard() -> ReplyKeyboardMarkup:
    buttons = []

    button_CreateRemind: KeyboardButton = KeyboardButton(text='Create remind 🚨')
    button_DeleteRemind: KeyboardButton = KeyboardButton(text='Delete remind ❌')
    button_CheckReminds: KeyboardButton = KeyboardButton(text='Check reminds 📋')
    button_GoToStartMenu: KeyboardButton = KeyboardButton(text='Back to start')

    buttons.append([[button_CreateRemind, button_CheckReminds], [button_DeleteRemind], [button_GoToStartMenu]])

    remind_mg_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
        keyboard=[
            buttons[0][0],
            buttons[0][1],
            buttons[0][2]
        ],
        resize_keyboard=True
    )

    return remind_mg_kb
