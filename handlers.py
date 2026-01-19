from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import main_keyboard
from db import add_fish

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "🍣 Добро пожаловать в Tap Roll!\n\n"
        "Тапай ролл и получай рыбу 🐟",
        reply_markup=main_keyboard()
    )


@router.message(lambda msg: msg.text == "🐟 Тап")
async def tap_handler(message: Message):
    user_id = message.from_user.id

    add_fish(user_id, 1)

    await message.answer("🐟 +1 рыба!")


@router.message()
async def webapp_handler(message: Message):
    """
    Приём данных из Telegram Mini App
    """
    if message.web_app_data:
        data = message.web_app_data.data

        if "tap" in data:
            user_id = message.from_user.id
            add_fish(user_id, 1)

            await message.answer("🐟 +1 рыба из приложения!")
