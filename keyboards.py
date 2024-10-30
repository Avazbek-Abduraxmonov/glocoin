from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

panel = [
    [
        InlineKeyboardButton(text="Statistika 📊", callback_data='status')
    ],
    [
        InlineKeyboardButton(text="Reklama 🏆", callback_data='rek'),
        InlineKeyboardButton(text="Malumotlar bazasi 🗂", callback_data="baza")
    ]
]

panel_builder = InlineKeyboardMarkup(inline_keyboard=panel)


main_menu = [
    [
        InlineKeyboardButton(text="Play GLC", url="http://t.me/glocoinbot/glc")
    ],
    [
        InlineKeyboardButton(text="Join Community", url="https://t.me/glocoin")
    ]
]

main_builder = InlineKeyboardMarkup(inline_keyboard=main_menu)