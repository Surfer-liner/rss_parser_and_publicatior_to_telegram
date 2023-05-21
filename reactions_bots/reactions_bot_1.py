import telebot
import random
import time

TOKEN = ''  
CHAT_ID = ''

reactions = ['👍', '❤️', '👀', '⚡', '🔥', '🏆'] 

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    random_number = random.randint(0, 1)

    if random_number == 1:
        reaction = random.choice(reactions)

        delay = random.randint(60, 120)

        time.sleep(delay)
        bot.send_chat_action(CHAT_ID, 'typing')
        time.sleep(2) 
        bot.send_message(CHAT_ID, reaction)
        print(f'Reacted with {reaction} after {delay} seconds')

    else:
        print('Skipped reaction')
        
bot.polling()
