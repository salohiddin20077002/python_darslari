from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

buttons = ReplyKeyboardMarkup([["Lotindan kirilga"], ["Kirildan Lotinga"]] ,  resize_keyboard=True)


def start(update, context): 
    update.message.reply_text('Assalomu alaykum,\nXush kelibsiz {}'.format(update.message.from_user.first_name), reply_markup=buttons)
    return 1
    
def stats(update, context):
    update.message.reply_text('Lotindan Kirilga Belgilandi', reply_markup=buttons)

def world(update, context):
    update.message.reply_text('Kirildan lotinga Belgilandi', reply_markup=buttons)



updater = Updater('5229108455:AAFY5Y7U5EK3hr6S4ln7id4I0whZZt2XsqA', use_context=True)
conv_handler = ConversationHandler(
    entry_points = [(CommandHandler('start', start))],
    states={
        1:[
            MessageHandler(Filters.regex('^(Lotindan kirilga)$'), stats), 
            MessageHandler(Filters.regex('^(Kirildan Lotinga)$'), world),
        ]    
    },
    fallbacks=[MessageHandler(Filters.text, start)]        
    )

updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()