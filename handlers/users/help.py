"""Справка по телеграм боту"""
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    """Возвращает пользователю справку телеграмм бота

    Args:
    message (types.Message): сообщение пользователя
"""
    text = (
        "Список команд: ",
        "/start - Начать диалог",
        "/help - Получить справку",
        "/menu - Главное меню",
        "/admin_panel - Панель администратора")
    await message.answer("\n".join(text))
