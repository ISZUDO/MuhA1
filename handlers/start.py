from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart
from keyboards.start_menu import menu,menu2
start_router: Router = Router()


@start_router.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer(f"Assalomu alaykum {msg.from_user.full_name},  mening botimga hush kelibsiz", reply_markup=menu)

@start_router.message(F.text=="Darslarni boshlash")
async def dars_handler(msg:Message):
    await msg.answer("Quydagilardan bittasini tanlang iltimos!", reply_markup=menu2)
