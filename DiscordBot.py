from discord.ext import commands
from decouple import config

bot = commands.Bot("!")

def load_cogs(bot):
    bot.load_extension('commands.generators')
    bot.load_extension('commands.on_ready')
    bot.load_extension('commands.stores')

load_cogs(bot)

TOKEN = config('secret_token')
bot.run(TOKEN)
