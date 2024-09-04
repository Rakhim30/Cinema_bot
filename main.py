import asyncio
from config import token , dp
from aiogram import F 
from buttons import *
from aiogram.filters.command import CommandStart,Command
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.state import State,StatesGroup
from aiogram.filters import Filter,StateFilter
from aiogram.fsm.context import FSMContext
from states import *
from db import create_ad, create_add,create_read,delete


@dp.callback_query(StateFilter('*'),F.data=='back')
async def go_start(call: CallbackQuery,state:FSMContext):
    first_name = call.message.from_user.first_name
    await call.message.answer(f'{first_name}', reply_markup=but)
    await state.set_state(My_State.starts)


@dp.message(CommandStart())
async def go_start(message: Message,state:FSMContext):
    first_name = message.from_user.first_name
    await message.answer_photo(photo='https://png.pngtree.com/element_our/png/20181119/cinema-vector-illustration-png_242108.jpg', caption=f'Helo {first_name}', reply_markup=but)
    await state.set_state(My_State.starts)    


@dp.message(F.text=='🧑🏻‍💻 Admin', My_State.starts)
async def go_start(message: Message,state:FSMContext):
    user_id = message.from_user.id
    if 554507627 == user_id:
        await message.answer(f'Admin', reply_markup=a.as_markup())
        await state.set_state(My_State.adv)
    else:    
        first_name = message.from_user.first_name
        await message.answer("Admin:", reply_markup=adm.as_markup())
        await state.clear()



@dp.callback_query(F.data=='add',My_State.adv)
async def ad(call:CallbackQuery, state: FSMContext):
    await call.message.answer(f'add video:')
    await state.set_state(My_State.osh) 

    

@dp.message(F.text,My_State.osh)
async def ad(message:Message, state: FSMContext):
    await message.answer(f'Add name:')
    text = message.text
    await state.update_data({'kino':text})
    await state.set_state(My_State.name)
    
@dp.message(F.text,My_State.name)
async def ad(message:Message, state: FSMContext):
    await message.answer(f'Add description:')
    text = message.text
    await state.update_data({'name':text})
    await state.set_state(My_State.prise)

    
@dp.message(F.text,My_State.prise)
async def ad(message:Message, state: FSMContext):
    text = message.text
    await state.update_data({'desc': text}) 
    data = await state.get_data()
    i = data.get('kino')
    n = data.get('name')
    d = data.get('desc')
    create_add(i,n,d)
    await message.answer('koshildi', reply_markup=a.as_markup())





@dp.callback_query(F.data == 'dele',My_State.adv)
async def deel(call:CallbackQuery,state:FSMContext):
    user = call.from_user.id
    b = InlineKeyboardBuilder()
    for i in create_read():
        b.add(InlineKeyboardButton(text=i[1], callback_data=i[1]))
    b.add(InlineKeyboardButton(text='Orqaga', callback_data='back'))
    await call.message.answer(f'Ochirmoqchi bolganingizni tanlang', reply_markup=b.as_markup())
    await state.set_state(My_State.a)

@dp.callback_query(F.data,My_State.a)    
async def deel(call:CallbackQuery,state:FSMContext):
    tw = call.data
    delete(tw)
    await call.message.answer('Ochirildi',reply_markup=back.as_markup())
    await state.clear()




@dp.message(F.text=='Watch moves!',My_State.starts)
async def as_start(message: Message,state:FSMContext):
    await message.answer(f'Moves:',reply_markup=product.as_markup())
    await state.set_state(My_State.b)

@dp.callback_query(F.data,My_State.b)
async def reg_one(call: CallbackQuery, state: FSMContext):
    text=call.data
    for i in create_read( ):
        if i[1] == text:
            await token.send_video(call.message.chat.id, video=i[0], caption=f"{i[1]},{i[2]}")
    await state.clear()




async def main():
    await dp.start_polling(token)

asyncio.run(main())