from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from db import create_read

but = ReplyKeyboardMarkup(    
    keyboard=[
        [KeyboardButton(text='Watch moves!')],
        [KeyboardButton(text='🧑🏻‍💻 Admin')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


adm = InlineKeyboardBuilder()     
adm.add(InlineKeyboardButton(text='Admin', callback_data='adm', url='https://t.me/rakhimboev'))

back = InlineKeyboardBuilder()
back.add(InlineKeyboardButton(text="back", callback_data='back'))


a = InlineKeyboardBuilder()
a.add(InlineKeyboardButton(text='Add', callback_data='add'))
a.add(InlineKeyboardButton(text='Delete', callback_data='dele'))
a.add(InlineKeyboardButton(text='Back', callback_data='back'))


c = InlineKeyboardBuilder()
c.add(InlineKeyboardButton(text='Kino korish', callback_data='adabiy'))



number = InlineKeyboardBuilder()
for i in range(1,10):
    number.add(InlineKeyboardButton(text=str(i), callback_data=str(i)))
number.adjust(2)



product = InlineKeyboardBuilder()

for row in create_read():
    data = row[1]
    product.add(InlineKeyboardButton(text=data, callback_data=data))
product.add(InlineKeyboardButton(text='Back',callback_data='back'))
product.adjust(2)

