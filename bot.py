"""
NOSHIT COIN TELEGRAM BOT
Deployed using heroku.
Author: vuki
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5073511122:AAHe2s-VgvRPkKQBlDpxai-TESx1gfAtFuw'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.send_text('Hi!')

def website(update, context):
    """Send a message when the command /website is issued."""
    update.message.reply_text('https://noshitcoin.io')

def contract(update, context):
    """Send a message when the command /contract is issued."""
    update.message.reply_text('0x53F042f3e809d2DcC9492dE2DbF05d1DA0EF5fbb')
    
def audit(update, context):
    """Send a message when the command /audit is issued."""
    update.message.reply_text('https://github.com/TechRate/Smart-Contract-Audits/blob/main/November/NOSHIT.pdf')

def chart(update, context):
    """Send a message when the command /audit is issued."""
    update.message.reply_text('/price@Poocoin_Pricebot')

def slippage(update, context):
    """Send a message when the command /contract is issued."""
    update.message.reply_text('tax:13% | slippage:13-15%')    


def locked(update, context):
    """Send a message when the command /contract is issued."""
    update.message.reply_text('LP Locked https://dxsale.app/app/v3/dxlplocksearch?id=0&add=0x53F042f3e809d2DcC9492dE2DbF05d1DA0EF5fbb&type=lpdefi&chain=BSC')

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("website", website))
    dp.add_handler(CommandHandler("contract", contract))
    dp.add_handler(CommandHandler("audit", audit))
    dp.add_handler(CommandHandler("chart", chart))
    dp.add_handler(CommandHandler("slippage", slippage))
    dp.add_handler(CommandHandler("locked", locked))
     

    # on noncommand i.e message - echo the message on Telegram
   

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://shrouded-waters-07443.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
