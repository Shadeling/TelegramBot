
import telebot
import loadData
import requests
import time
from telebot import types

botsData, dataDict = loadData.loadData()

# for botName in botsData:
#     newBot = telebot.TeleBot(botsData[botName])
#     botsData[botName] = newBot

print(botsData)
print("\n\n")
print(dataDict)
token = '6033206483:AAFbCMZ1Mu9tbFDURLn7oqpb9Ry-Hsnm3nc'
bot=telebot.TeleBot(token)





@bot.message_handler(commands=['start'])
def start(message):
  createMarkUp('1', message)
  
  
def createMarkUp(id, message):
  line = dataDict[id]
  print(line)
  print("\n")
  if line["NextType"] == "WithoutButtons":
    markup = None
  else:
    markup = types.InlineKeyboardMarkup(row_width=1)
    num = 1
    while num <= int(line["ButtonsNum"]):
      markup.add(types.InlineKeyboardButton(text = line[f'Text{num}'], callback_data=line[f'ID{num}']))
      num = num+1
  bot.send_message(chat_id=message.chat.id,
                     text=line["Data"],
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
  id = call.data
  print(f'\n\nCall Data: {call.data}')
  if(id != ''):
    createMarkUp(id, call.message)
    
    
bot.infinity_polling()
    
# while True:
#   try:
#     bot.polling(none_stop=True, interval=0, timeout=0)
#   except requests.exceptions.ConnectionError:
#     print (" ConnectionError exception occured while polling, restart in 1 second...")
#     time.sleep(1)
#     continue
#   except telebot.apihelper.ApiException:
#     print (" ApiException exception occured while polling, restart in 1 second...")
#     time.sleep(1)
#     continue
#   except requests.exceptions.ReadTimeout:
#     print (" ReadTimeout exception occured while polling, restart in 1 second...")
#     time.sleep(1)
#   except:
#     print (" Another exception while polling, restart in 1 second...")
#     time.sleep(1)
#     continue

