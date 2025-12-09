from config import ADMINS
def send_to_admins(bot, message):
    for admin_id in ADMINS:
        bot.send_message(admin_id,message)