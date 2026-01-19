from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🎮 Играть",
                    web_app=WebAppInfo(
                        url="https://tapalka-webapp.vercel.app/"
                    )
                )
            ],
            [KeyboardButton(text="🐟 Тап")]
        ],
        resize_keyboard=True
    )
