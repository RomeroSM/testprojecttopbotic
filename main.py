import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, CallbackQuery
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton


bot_tok = '5361620297:AAEg7tJIZslchQMu5Fp8wPIAyVaeZ57Jo6Y'

bot = Bot(token = bot_tok)
dp = Dispatcher(bot)

resume = InlineKeyboardButton('Продолжить', callback_data='resume')
resume1 = InlineKeyboardButton('Продолжить', callback_data='resume1')
resume2 = InlineKeyboardButton('Продолжить', callback_data='resume2')
resume3 = InlineKeyboardButton('Продолжить', callback_data='resume3')
resume4 = InlineKeyboardButton('Продолжить', callback_data='resume4')
resume5 = InlineKeyboardButton('Продолжить', callback_data='resume5')
resume6 = InlineKeyboardButton('Продолжить', callback_data='resume6')
resume7 = InlineKeyboardButton('Продолжить', callback_data='resume7')
resume8 = InlineKeyboardButton('Продолжить', callback_data='resume8')
rsm_kbtn = InlineKeyboardMarkup().add(resume)
rsm1_kbtn = InlineKeyboardMarkup().add(resume1)
rsm2_kbtn = InlineKeyboardMarkup().add(resume2)
rsm3_kbtn = InlineKeyboardMarkup().add(resume3)
rsm4_kbtn = InlineKeyboardMarkup().add(resume4)
rsm5_kbtn = InlineKeyboardMarkup().add(resume5)
rsm6_kbtn = InlineKeyboardMarkup().add(resume6)
rsm7_kbtn = InlineKeyboardMarkup().add(resume7)
rsm8_kbtn = InlineKeyboardMarkup().add(resume8)

bakery1 = InlineKeyboardButton('Сахарова', callback_data='Sakharova')
bakery2 = InlineKeyboardButton('Глушко', callback_data='Glushko')
bakery3 = InlineKeyboardButton('Фучика', callback_data='fuchika')
bakery4 = InlineKeyboardButton('пр. Победы', callback_data='Victory_Avenue')
bakery_kbtn = InlineKeyboardMarkup(row_width=1).add(bakery1, bakery2, bakery3, bakery4)

type_of_verification1 = InlineKeyboardButton('Общая', callback_data='general')
type_of_verification2 = InlineKeyboardButton('Торговый зал', callback_data='Trading_floor')
type_of_verification3 = InlineKeyboardButton('Производство', callback_data='production')
type_of_verification4 = InlineKeyboardButton('Счетчик', callback_data='counter')
tov_kbtn = InlineKeyboardMarkup(row_width=1).add(type_of_verification1, type_of_verification2, type_of_verification3, type_of_verification4)

general_question1_1 = InlineKeyboardButton('Норма', callback_data='general_question1_1')
general_question1_2 = InlineKeyboardButton('Проблема', callback_data='general_question1_2')
general_question2_1 = InlineKeyboardButton('Норма', callback_data='general_question2_1')
general_question2_2 = InlineKeyboardButton('Проблема', callback_data='general_question2_2')
general_question3_1 = InlineKeyboardButton('Норма', callback_data='general_question3_1')
general_question3_2 = InlineKeyboardButton('Проблема', callback_data='general_question3_2')
general_question4_1 = InlineKeyboardButton('Норма', callback_data='general_question4_1')
general_question4_2 = InlineKeyboardButton('Проблема', callback_data='general_question4_2')
gnq_kbtn1 = InlineKeyboardMarkup(row_width=2).add(general_question1_1, general_question1_2)
gnq_kbtn2 = InlineKeyboardMarkup(row_width=2).add(general_question2_1, general_question2_2)
gnq_kbtn3 = InlineKeyboardMarkup(row_width=2).add(general_question3_1, general_question3_2)
gnq_kbtn4 = InlineKeyboardMarkup(row_width=2).add(general_question4_1, general_question4_2)

get_started = InlineKeyboardButton('Начать работу', callback_data='get_started')
gtst_kbtn = InlineKeyboardMarkup(row_width=1).add(get_started)



@dp.message_handler(commands='start')

async def strt_menu(message: Message):
    await message.answer(f'Привет!\n'
                         f'Ты являешься незарегистрированным пользователем.\n'
                         f'Для регистрации введи команду /reg')


@dp.message_handler(commands='reg')

async def reg(message: Message):
    await message.answer(f'Поздравляю!\n'
                         f'Вы были успешно зарегистрированы!', reply_markup=rsm_kbtn)





@dp.callback_query_handler()
async def buttons(call: CallbackQuery):
    chat_id = call.from_user.id
    if call.data == 'resume':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Приветствую!\n'
                                                     f'Вы готовы начать работу?', reply_markup=gtst_kbtn)
    elif call.data == 'get_started':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Выберите нужную вам пекарню', reply_markup=bakery_kbtn)
    elif call.data == 'Sakharova':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Выберите тип проверки, который вы хотите произвести', reply_markup=tov_kbtn)
    elif call.data == 'Glushko':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Выберите тип проверки, который вы хотите произвести', reply_markup=tov_kbtn)
    elif call.data == 'fuchika':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Выберите тип проверки, который вы хотите произвести', reply_markup=tov_kbtn)
    elif call.data == 'Victory_Avenue':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Выберите тип проверки, который вы хотите произвести', reply_markup=tov_kbtn)
    elif call.data == 'general':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 1', reply_markup=gnq_kbtn1)
    elif call.data == 'Trading_floor':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 1', reply_markup=gnq_kbtn1)
    elif call.data == 'production':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 1', reply_markup=gnq_kbtn1)
    elif call.data == 'counter':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 1', reply_markup=gnq_kbtn1)
    elif call.data == 'general_question1_1':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 2', reply_markup=gnq_kbtn2)
    elif call.data == 'general_question1_2':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Отправьте фото проблемы', reply_markup=rsm1_kbtn)
    elif call.data == 'resume1':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Оставьте комментарий', reply_markup=rsm5_kbtn)
    elif call.data == 'resume5':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 2', reply_markup=gnq_kbtn2)
    elif call.data == 'general_question2_1':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 3', reply_markup=gnq_kbtn3)
    elif call.data == 'general_question2_2':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Отправьте фото проблемы', reply_markup=rsm2_kbtn)
    elif call.data == 'resume2':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Оставьте комментарий', reply_markup=rsm6_kbtn)
    elif call.data == 'resume6':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 3', reply_markup=gnq_kbtn3)
    elif call.data == 'general_question3_1':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 4', reply_markup=gnq_kbtn4)
    elif call.data == 'general_question3_2':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Отправьте фото проблемы', reply_markup=rsm3_kbtn)
    elif call.data == 'resume3':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Оставьте комментарий', reply_markup=rsm7_kbtn)
    elif call.data == 'resume7':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Вопрос 4', reply_markup=gnq_kbtn4)
    elif call.data == 'general_question4_1':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Спасибо что провели проверку!')
    elif call.data == 'general_question4_2':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Отправьте фото проблемы', reply_markup=rsm4_kbtn)
    elif call.data == 'resume4':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Спасибо что провели проверку!', reply_markup=rsm8_kbtn)
    elif call.data == 'resume8':
        await call.message.delete()
        await bot.send_message(chat_id=chat_id, text=f'Спасибо что провели проверку!')





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
