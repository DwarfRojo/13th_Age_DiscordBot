from discord.ext import commands

class Ready_Go(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronto! conectado como {self.bot.user}')

def setup(bot):
    bot.add_cog(Ready_Go(bot))