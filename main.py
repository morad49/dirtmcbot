import discord
from discord.ext import commands
import os

# إعداد الصلاحيات
intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'تم تشغيل البوت بنجاح: {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # الأمر الذي طلبته
    if message.content.lower() == "mc":
        await message.channel.send("say my name")

    await bot.process_commands(message)

# Render يتطلب أحياناً وجود "منفذ" (Port) ليعرف أن التطبيق يعمل
# سنستخدم التوكن من متغيرات البيئة للأمان
token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
else:
    print("خطأ: لم يتم العثور على التوكن في Environment Variables")
