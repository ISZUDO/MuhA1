from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton




menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Darslarni boshlash")
        ]
    ],
    resize_keyboard=True
)




menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kompyuter Savodhonligi")
        ],
        [
            KeyboardButton(text="Grafik dizayn"),
            KeyboardButton(text="Dasturlash"),
        ],
        [
            KeyboardButton(text="Kerakli darslar"),
            KeyboardButton(text="Biz bilan bog'lanish"),
        ],
        [
            KeyboardButton(text="Bot haqida"),
        ],
        
    ],
    resize_keyboard=True
)