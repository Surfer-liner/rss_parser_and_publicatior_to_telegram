import telebot
import random
import time

TOKEN = '5837781877:AAEM9ApnIcRrkN44K0PbmozAUlLQRmtWnxY'  # Замените на свой токен бота
CHAT_ID = -1001661936464  # ID группы, куда бот будет ставить реакции

reactions = ['👍', '❤️', '👀', '⚡', '🔥', '🏆']  # Список доступных реакций

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Генерируем случайное число 0 или 1
    random_number = random.randint(0, 1)

    if random_number == 1:
        # Выбираем случайную реакцию из списка
        reaction = random.choice(reactions)

        # Генерируем случайную задержку от 60 до 120 секунд
        delay = random.randint(60, 120)

        # Отправляем реакцию через заданную задержку
        time.sleep(delay)
        bot.send_chat_action(CHAT_ID, 'typing')
        time.sleep(2)  # Имитация набора сообщения
        bot.send_message(CHAT_ID, reaction)
        print(f'Reacted with {reaction} after {delay} seconds')

    else:
        print('Skipped reaction')


bot.polling()
