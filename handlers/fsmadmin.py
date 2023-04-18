from aiogram import types, Dispatcher,bot ,Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from . import client_kb


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        await FSMAdmin.id.set()
        await message.answer("ID какой??", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в личку!")


async def load_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    else:
        async with state.proxy() as data:
            data["id"] = message.from_user.id
            data["username"] = message.from_user.username
            data["name"] = message.text
        await FSMAdmin.next()
        await message.answer("Как твоё имя ,воин?")


async def load_name(message: types.Message, state: FSMContext):
    if not message.text.isalpha():
        await message.answer("Пиши буквы!")
    else:
        async with state.proxy() as data:
            data["name"] = message.text
        await FSMAdmin.next()
        await message.answer("Направление?", reply_markup=client_kb.gender_markup)


async def load_direction(message: types.Message, state: FSMContext):
    if message.text not in ["BACKEND", "BackEnd", "backend"]:
        await message.answer("Используй кнопки!")
    else:
        async with state.proxy() as data:
            data["direction"] = message.text
        await FSMAdmin.next()
        await message.answer("Сколько годиков??", reply_markup=client_kb.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши циферки!")
    else:
        async with state.proxy() as data:
            data["age"] = message.text
        await FSMAdmin.next()
    await message.answer("Скажи группу)")



async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["group"] = message.text
    await FSMAdmin.next()

    await message.answer("Все верно?", reply_markup=client_kb.submit_markup)


async def submit_state(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await state.finish()
        await message.answer("Все свободен)")
    if message.text.lower() == "заново":
        await FSMAdmin.id.set()
        await message.answer("IDDDD??")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Ну и пошел ты!")


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='отмена', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['mentor'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group,)
    dp.register_message_handler(submit_state, state=FSMAdmin.submit)