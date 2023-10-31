import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import os

api = "https://meme-api.com/gimme"
botToken = "Your Bot Token"

bot = telebot.TeleBot(botToken)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    userID = str(call.from_user.id)
    data = call.data
    if data == 'meme':
        i1 = [[InlineKeyboardButton(text=f'Another One',
         callback_data=f'meme')]]
        inline_keyboard = InlineKeyboardMarkup(i1)
        photo = open('photo.jpg', 'wb')
        req = requests.get(api).json()['preview'][-1]
        photo.write(requests.get(req).content)
        photo.close()
        inline_keyboard = InlineKeyboardMarkup(i1)
        with open('photo.jpg', 'rb') as photo_file:
            media = telebot.types.InputMediaPhoto(media=photo_file)
            bot.edit_message_media(
                media=media,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=inline_keyboard
            )
            bot.edit_message_reply_markup(
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=inline_keyboard
            )

@bot.message_handler(commands=['start'])
def start(message):
    photo = open('photo.jpg', 'wb')
    req = requests.get(api).json()['preview'][-1]
    photo.write(requests.get(req).content)
    photo.close()
    i1 = [[InlineKeyboardButton(text=f'Another One',
     callback_data=f'meme')]]
    inline_keyboard = InlineKeyboardMarkup(i1)
    # Send the downloaded photo to the chat
    with open('photo.jpg', 'rb') as photo_file:
        bot.send_photo(message.chat.id, photo_file,
        reply_markup=inline_keyboard)
    os.remove('photo.jpg')


bot.infinity_polling()
#https://www.facebook.com/zerocruch/
#https://tiktok.com/@zerocruch
#https://www.youtube.com/@zerocruch
#https://www.instagram.com/zerocruch_
