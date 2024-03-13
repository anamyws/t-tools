import telebot
import instaloader

# تهيئة التوكن الخاص بالبوت
bot_token = input ("توكن :")

# إنشاء كائن البوت
bot = telebot.TeleBot(bot_token)

# استخدام مكتبة instaloader للحصول على معلومات حساب انستغرام
def get_instagram_account(username):
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, username)
    return profile.full_name, profile.followers, profile.followees, profile.mediacount, profile.profile_pic_url, profile.biography

# استقبال الرسائل والتعامل معها
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! قم بإرسال اسم المستخدم لحساب انستغرام لعرض معلوماته.")

@bot.message_handler(func=lambda message: True)
def get_instagram_info(message):
    username = message.text
    account_name, followers, followees, mediacount, profile_pic_url, biography = get_instagram_account(username)
    if account_name and followers and followees and mediacount:
        bot.send_photo(message.chat.id, profile_pic_url)
        reply = f"Name: {account_name}\n\nFollowers: {followers}\n\nFollowees: {followees}\n\nMediacount: {mediacount}\n\nBiography: {biography}\n\nInstagram Account: https://www.instagram.com/{username}/"
    else:
        reply = "فشل تأكد من استخدام اليوزر بشكل صحيح."
    bot.reply_to(message, reply)

# تشغيل البوت
bot.polling()