from aiogram.types import Message
from keyboards import *
from config import *

async def startAnswer(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username or "NoUsername"  # Handle users with no username

    # Check if the user is already in users.txt
    user_exists = False
    try:
        with open("users.txt", "r") as file:
            for line in file:
                if str(user_id) in line:
                    user_exists = True
                    break
    except FileNotFoundError:
        # If the file doesn't exist, we'll create it when adding a new user
        pass

    # If the user is not in users.txt, add them
    if not user_exists:
        with open("users.txt", "a") as file:
            file.write(f"{user_id},@{username}\n")

    # Send the welcome message
    await message.answer(
        "Hello! Welcome to GLOCOIN \nYou are now the director of a crypto exchange.\nWhich one? You choose. Tap the screen, collect coins, pump up your passive income,\ndevelop your own income strategy.\nWe’ll definitely appreciate your efforts once the token is listed (the dates are coming soon).\nDon't forget about your friends — bring them to the game and get even more coins together!",
        reply_markup=main_builder
    )
