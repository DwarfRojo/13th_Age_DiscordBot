from discord.ext import commands

class Stores(commands.Cog):
    """Gerador de cartas e efeitos do RPG"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='a.armas')
    async def alaumir_weapon_store(self, ctx):
        weapon_list = f"""Adaga/Faca....1po
    Foice....8po
    Espada curta....4 po
    Espada Longa....7 po
    Montante....10 po
    Maça....5 po
    Machado de mão....3 po
    Manoplas de batalha....4 po
    Martelo de arremesso....3po
    Porrete....5 pp
    Rede, com pesos....3 po"""

        await ctx.send(weapon_list)

    @commands.command(name='a.shop')
    async def alaumir_comu_item_store(self, ctx):
        items = '''Cachimbo (1 uso)....2 pc
    Cobertor (lã)....5 pp
    Arpéu (ferro)....1po
    Corda, 30 metros boa....6pp
    Corda, 30 metros pobre....2pp
    Corrente, ferro (3m)....5po
    Mochila/bolsa de viagens....1po
    Ração de viagens....25pp
    Caixa de pederneira e isqueiro....1pp
    Espelho, pequeno....2po
    Ferramentas de ladino (aventureiro)....2po
    Ferramentas de ladino (campeão)....20po
    Flechas/ quadrelos/munição de funda....1pp/cada
    Frasco (cerâmica)...5pc
    Frasco (cristal)....5po
    Frasco (vidro)....5pp
    Grimório (aventureiro)....10po
    Grimório (campeão)....100po
    Grimório (épico)....1.000po
    Instrumento musical (intrincado)....15po
    Instrumento musical (simples)....4po
    Lanterna (comum)....8pp
    Livro de orações....2po
    Martelo, pequeno....3pp
    Gato malhado grande de Ugalpé, garantidamente livre de pulgas e possessões demoníacas....20po
    Ervas para chá calmante....2pp
    Ervas de picante....2pp'''

        await ctx.send(items)

    @commands.command(name='a.taverna')
    async def tavern_cardapio(self, ctx):
        cardapio = '''Cerveja, Anã (caneca)....3po
    Cerveja, boa (caneca)....6pc
    Cerveja, pobre (caneca)....2pc
    Ração de viagem (1 dia)....5pp
    Refeição, banquete (para 5)....8po
    Refeição, boa....3pp
    Refeição, comum....1pp
    Refeição, excelente....8pp
    Vinho, bom (garrafa)....1pp
    Vinho, élfi co (garrafa)....1–5po
    Vinho, pobre (garrafa)....4pc'''

    @commands.command(name='a.inn')
    async def inn_alaumir(self, ctx):
        inn = '''quarto para 4 pessoas....3pp
    quarto para 4 pessoas com café da manhã....1po
    quarto para 4 pessoas de melhor qualidade....1po
    quarto 4 pessoas de melhor qualidade com café da manhã....2po'''

        await ctx.send(inn)

    @commands.command(name='a.smith')
    async def alaumir_ferreiro(self, ctx):
        ferreiro = '''Adaga de Ferro Olográfico....30po
    Espada...8po
    Martelo....1po
    Martelo de guerra....7po
    Espada longa....10
    Espada de Duas Mãos Bem Ornamentada...15po'''

        await ctx.send(ferreiro)


def setup(bot):
    bot.add_cog(Stores(bot))