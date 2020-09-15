import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
import settings

from handlers import greeting_user, send_cat_picture, change_avatar, get_contact, get_location, talk_to_me


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def main():
    mybot = Updater(settings.API_KEY)

    logging.info('Bot started')
    dp = mybot.dispatcher  # отвечает за общение бота и скрипта

    # комманды которые вводит юзер в боте
    dp.add_handler(CommandHandler("start", greeting_user, pass_user_data=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True, ))
    dp.add_handler(MessageHandler(Filters.regex('Прислать котика'), send_cat_picture, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.regex('Сменить аватарку'), change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mybot.start_polling()  # получает команду.
    mybot.idle()


if __name__ == '__main__':
    main()
