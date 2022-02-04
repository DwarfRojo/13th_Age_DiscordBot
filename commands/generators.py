from discord.ext import commands
from random import randint, choice
import discord

class Generators(commands.Cog):
    """Gerador de cartas e efeitos do RPG"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="signo")
    async def sign_generator(self, ctx):
        signs_list = [
            'Quetzalcoatl', 'Behemoth', 'Leviatã', 'Wiindigoo', 'Fogo Fatuo', 'Ifrit', 'Mangoroa', 'Nidhog',
            'Carbuncle', 'Silfide', 'Wyvern', 'Siren',
        ]

        sign_image_list = [
            'https://i.pinimg.com/564x/ae/9f/9c/ae9f9c8ac8ec210da41869a8131ff633.jpg',
            'https://i.pinimg.com/564x/6e/c1/b2/6ec1b282e5bcf20e9269eac2e0cc1d44.jpg',
            'https://i.pinimg.com/564x/c5/0a/21/c50a2198072df0cf7fbd697c88a16c8f.jpg',
            'https://i.pinimg.com/564x/d0/c3/18/d0c3183041f7f2eff89a626ddf3f4646.jpg',
            'https://i.pinimg.com/564x/53/9b/ad/539bad76371e256abe31b2a43d2af7ca.jpg',
            'https://i.pinimg.com/564x/0a/95/c2/0a95c2af572cf185300db14e13179ee3.jpg',
            'https://i.pinimg.com/564x/b9/bc/90/b9bc908fae1144ffcd22c504cb4f487b.jpg',
            'https://i.pinimg.com/564x/7a/d2/f7/7ad2f7aec88870e227fe4d350f18705f.jpg',
            'https://i.pinimg.com/564x/39/bd/27/39bd2782778c4fe35d491d65fca287f9.jpg',
            'https://i.pinimg.com/564x/a9/ab/41/a9ab413a24d0c4d17025bd41e6b0fc4d.jpg',
            'https://i.pinimg.com/564x/b7/ee/99/b7ee99177b8b1e17cfc6ae6dc45cd4b5.jpg',
            'https://i.pinimg.com/564x/e6/56/28/e656280d27b13680af48c5345c540a00.jpg',
        ]

        sign_generator = randint(0, len(signs_list) - 1)

        embed_image = discord.Embed(
            title=f"{signs_list[sign_generator]}",
            colour=0x00FFFF
        )

        embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed_image.set_footer(text=f'{self.bot.user.name} é um bot do Davus', icon_url=self.bot.user.avatar_url)

        embed_image.set_image(url=sign_image_list[sign_generator])

        await ctx.send(embed=embed_image)

    @commands.command(name="baú")
    async def normal_chest_items_generator(self, ctx):
        gemms = []
        gemm_ten = [
            'Azurita (azul escuro mosqueado opaco)',
            'Ágata malhada(marrom, azul, branca ou vermelho translúcido e listrado)',
            'Quartzo azul(azul claro transparente)',
            'Ágata ocular (círculos translúcidos de cinza, branco, marro, azul ou verde)',
            'Hematita (cinza escuro opaco)',
            'Lápis lazúli (azul claro e escuro opaco com manchas amarelas)',
            'Malaquita (opaco estriado com verde claro e escuro)',
            'Ágata musgo (rosa translúcido ou amarelo claro com cinza musgo ou marcas verdes)',
            'Obsidiana (preto opaco)',
            'Rodocrosita (azul claro opaco)',
            'Olho de tigre (marrom translúcido com centro dourado)',
            'Turquesa (azul esverdeado claro opaco)',
        ]

        for c in range(0, 5):
            gem_choice = f'{choice(gemm_ten)}'
            gemms.append(f'{gem_choice}')

        chest_loot = [
            f'-Machado comum \n-{gemms[0]} \n-{gemms[1]} \n-{gemms[2]}'
        ]

        response = f'{choice(chest_loot)}'

        await ctx.send(response)

    @commands.command(name="baúazul")
    async def blue_chest_generator(self, ctx):
        gemms = []
        gemm_twenty = [
            'Pedra de sangue(cinza escuro opaco com manchas vermelhas)',
        'Cornalina(de laranja a vermelho amarronzado opaco)',
        'Calcedônia(branco opaco)',
        'Crisoprásio(verde translúcido)',
        'Citrina(amarelo claro amarronzado transparente)',
        'Jaspe(azul, preto ou marrom opaco)',
        'Pedra lunar(branco translúcido com azul claro brilhante)',
        'Ônix(faixas opacas de preto e branco, ou preto ou branco puro)',
        'Quartzo(branco transparente, cinza ou amarelo esfumaçado)',
        'Sardônica(faixas opacas de vermelho e branco)',
        'Quartzo rosa estrela(pedra rosa translúcida com centro branco em forma de estrela)',
        'Zircônio(azul esverdeado claro transparente)',

        ]

        for c in range(0, 5):
            gem_choice = f'{choice(gemm_twenty)}'
            gemms.append(f'{gem_choice}')

        chest_loot = [
            f'-Runa \n-{gemms[0]} \n-{gemms[1]} \n-Colar Elfico, de cordão delicado e com uma flor brotando entre os veios do cordão',
            ''
        ]

        response = f'{choice(chest_loot)}'

        await ctx.send(response)

    @commands.command(name="baúroxo")
    async def purple_chest_generator(self, ctx):
        gemms = []
        gemm_fifty = [
            'Pedra de sangue(cinza escuro opaco com manchas vermelhas)',
        'Cornalina(de laranja a vermelho amarronzado opaco)',
        'Calcedônia(branco opaco)',
        'Crisoprásio(verde translúcido)',
        'Citrina(amarelo claro amarronzado transparente)',
        'Jaspe(azul, preto ou marrom opaco)',
        'Pedra lunar(branco translúcido com azul claro brilhante)',
        'Ônix(faixas opacas de preto e branco, ou preto ou branco puro)',
        'Quartzo(branco transparente, cinza ou amarelo esfumaçado)',
        'Sardônica(faixas opacas de vermelho e branco)',
        'Quartzo rosa estrela(pedra rosa translúcida com centro branco em forma de estrela)',
        'Zircônio(azul esverdeado claro transparente)',

        ]

        for c in range(0, 5):
            gem_choice = f'{choice(gemm_fifty)}'
            gemms.append(f'{gem_choice}')

        chest_loot = [
            f'-Runa \n-{gemms[0]} \n-{gemms[1]} \n-Colar Elfico, de cordão delicado e com uma flor brotando entre os veios do cordão',
            ''
        ]

        response = f'{choice(chest_loot)}'

        await ctx.send(response)

    @commands.command(name="loot")
    async def pick_a_loot(self, ctx):
        coin = randint(1, 50)

        loot_list = [
            'Ampulheta de bronze',
            f'{coin}PO e um machado gasto', f'{coin}PP e uma maça estrela', f'{coin}PPAgulha de costura', 'Algemas (obra-prima)',
            f'Algemas e {coin} PP', 'Algibeira', f'Anzol e {coin} PP', 'Apito de advertência', 'Balde (vazio)', 'Barril (vazio)',
            'Baú (vazio)', 'Caneco de cerâmica', 'Caneta tinteiro', 'Cantil	1 PO', 'Cesto (vazio)', 'Cobertor de inverno',
            'Corda de Cânhamo (15 m)', 'Corda de seda (15 m)', 'Corrente (3 m)', 'Escada (3 m)', 'Esmeril', 'Espelho de metal pequeno',
            'Estrepes', 'Fechadura muito simples', 'Fechadura padrão', 'Fechadura boa', 'Fechadura Incrível',
            'Frasco (vazio)', 'Garrafa de vinho (vidro)', 'Giz (1 pedaço)', 'jarro de cerâmica', 'Lâmpada',
            'Lanterna coberta', 'Lanterna furta-fogo', 'Lenha (por dia)', 'Lona (m²)', 'Luneta', 'Marreta', 'Giz branco',
            'Vela preta', 'Bandana vermelha', 'Dados de 6 lados', 'Brincos de ouro', 'Moeda com dois lados cara',
            'Vidro de ácido', 'Um pano fino embrulhando uma porção de gemas', 'Martelo', 'Mochila (vazia)', 'Óleo (500 ml)',
            'Pá', 'Panela de ferro', 'Parafina', 'Pé de cabra', 'Pederneira e isqueiro', 'Pergaminho (folha)', 'Picareta de mina',
            'Píton', 'Porta-mapas', 'Pote de cerâmica', 'Rações de viagem para 2 dias', 'Rede de pesca (5 x 5 m)',
            'Sabão (por kg)', 'Saco (vazio)', 'Saco de dormir', 'Sinete', 'Sino', 'Talha ou sisal', 'Tenda',
            'Tinta (vidro de 30 ml)', 'Tocha', 'Vara', 'Vela', 'Vidro para tinta ou poção',
        ]

        item = loot_list[randint(0, len(loot_list) - 1)]

        await ctx.send(item)

    @commands.command(name='tarot')
    async def pick_a_card(self, ctx):
        cards_images = [
            'https://i.pinimg.com/564x/6f/d9/1e/6fd91eb4e07572f0d15c7f0cf3cdaaed.jpg',
            'https://i.pinimg.com/564x/0d/65/73/0d6573cf0f889f33ca154fdd2c532d79.jpg',
            'https://i.pinimg.com/564x/bc/9f/83/bc9f83d115e5de0b01e830385d4f7f19.jpg',
            'https://i.pinimg.com/564x/07/eb/c2/07ebc21bf083e03a50052cffad23d726.jpg',
            'https://i.pinimg.com/564x/68/ea/f7/68eaf7c3bc425a98f3fd5f6883bb0909.jpg',
            'https://i.pinimg.com/564x/d2/75/bc/d275bc6727853b92d89e48cd84161754.jpg',
            'https://i.pinimg.com/736x/9c/b3/83/9cb383c478cf05c008d785ebbffb9ab2.jpg',
            'https://i.pinimg.com/564x/15/88/e6/1588e6a60f39fd951a85215e4edde0ce.jpg',
            'https://i.pinimg.com/564x/0a/24/ed/0a24ed0757a324b061df2b82b4e61144.jpg',
            'https://i.pinimg.com/564x/a0/c6/f0/a0c6f063640f7615466993cab3982938.jpg',
            'https://i.pinimg.com/564x/09/4b/d1/094bd1004fa3725f1dba31263e6c1d85.jpg',
            'https://i.pinimg.com/564x/ba/53/32/ba5332f012a22cc37dab9fcc18ed4c65.jpg',
            'https://i.pinimg.com/564x/35/ca/9f/35ca9f760235a6ceb06a0b696f2aa22c.jpg',
            'https://i.pinimg.com/564x/3a/10/5a/3a105ab5b24f57360618dec19b9369d6.jpg',
            'https://i.pinimg.com/564x/8d/ab/68/8dab68f6114b1ef6604903cd966e3486.jpg',
            'https://i.pinimg.com/564x/6b/46/7b/6b467b01b334d3cbfcd8088a78091dc8.jpg',
            'https://i.pinimg.com/564x/fc/eb/0c/fceb0c4c57af81755cf66f37cffdc5bf.jpg',
            'https://i.pinimg.com/564x/3f/18/9a/3f189ac7b71e8ae352e87b4ec5f395b0.jpg',
            'https://i.pinimg.com/564x/82/f3/4f/82f34f498470951fef66297adc432272.jpg',
            'https://i.pinimg.com/564x/b9/47/95/b947956eac6acfe2eca0fb83a10bf044.jpg',
            'https://i.pinimg.com/564x/b7/28/21/b728215763e50606ab97f12eb0e2b626.jpg',
            'https://i.pinimg.com/564x/2b/8d/58/2b8d5825c03bc469b1a0b0e42343d90d.jpg'
        ]

        card_name = [
            'Mundo', 'Julgamento',
            'Sol', 'Lua',
            'Estrela', 'Torre',
            'Temperança', 'Morte',
            'Enforcado', 'Força',
            'Roda da Fortuna', 'Heremita',
            'Justuça', 'Carroça',
            'Amantes', 'Hierophant',
            'Emperador', 'Imperatriz',
            'Papiza', 'Mago',
            'Tolo', 'Diabo'
        ]

        efeitos = [
            '1 Role 1d4, adicione ou subtraia o valor a uma jogada de ataque à distância de uma criatura',
            '2 Role 1d4, adicione ou subtraia o valor a uma jogada de ataque corpo a corpo de uma criatura',
            '3 Começa a ventar o suficiente para fazer coisas suscetíveis à ventania começarem a acontecer',
            '4 por que tá chovendo? (caso já esteja chovendo, começa a nevar)',
            '5 +1 na margem de crítico Crítico de uma criatura',
            '6 Se o alvo acertar com um resultado par natural o ataque conta como um crítico',
            '7 Tome apenas metade de dano arredondado para cima no próximo ataque que levar',
            '8 O ataque contra aquele alvo tem penalidade igual ao seu bônus de Carisma',
            '9 Você tem um vislumbre de um acontecimento do passado de um inimigo à sua escolha',
            '10 Role 1d12, a criatura naquela posição na iniciativa troca de lugar com quem vai agir após você',
            '11 Adiciona uma ação a mais, logo após você, para quem agiu antes do seu turno. Mas é apenas uma ação, o alvo deve escolher entre atacar ou mover-se. Ele não pode mover-se e atacar neste turno extra',
            '12 O alvo está preso ao chão, não pode mover seus pés. Mas ainda pode fazer ataques à distância',
            '13 Um alvo próximo está invisível até ele atacar ou até o fim do próximo turno',
            '14 O ultimo a errar um golpe está mudo',
            '15 O ultimo a tirar 16+ em uma rolagem de ataque ou resistir recarrega um poder ou magia que seja "por combate"',
            '16 O ultimo a errar com um resultado impar natural ganha +2 no próximo ataque',
            '17 O ultimo a acertar co um resultado par natural Baixa sua margem de crítico em 2 no próximo ataque',
            '18 O ultimo a errar com um resultado par natural SE acerta acertar o próximo ataque, rola na tabela de efeitos arcanos aleatórios',
            '19 O ultimo a acertar com um resultado impar natural Dobra seu tamanho. Apenas o tamanho, seus status se mantém.',
            '20 O próximo a acertar com um resultado par natural agora tem um rabo que permanece até o fim do combate. Caso já possua um rabo, um terceiro olho choroso cresce na bochehca de um dos lados do rosto',
            '21 O próximo a errar com um resultado par natural pode se desengajar livremente.',
            '22 O próximo a errar com um resultado impar natural Está flutuando. Bom passeio.',
        ]

        card_generator = randint(0, len(cards_images) - 1)

        embed_tarot = discord.Embed(
            title=f'{card_name[card_generator]}',
            color=0x00FFFF
        )
        embed_tarot.add_field(name='Efeito', value=f'{efeitos[card_generator]}')
        embed_tarot.set_image(url=cards_images[card_generator])

        await ctx.send(embed=embed_tarot)

    @commands.command(name='magiacaotica')
    async def chaotic_magic(self, ctx):
        efects = [
            'Role novamente nessa tabela no inicio de cada um de seus turnos, durante um minuto, ignorando este resultado nas rolagens subsequentes.',
            'Um escudo espectral flutuante surge ao seu lado pelo próximo minuto, concedendo um bônus de CA +2 e imunidade contra mísseis mágicos.',
            'Durante 1 minuto, você pode ver criaturas invisíveis.',
            'Você fica imune aos efeitos de álcool durante os próximos 5d6 dias.',
            'Um inevitável* escolhido pelo mestre surge em um espaço desocupado adjacente a você, desaparecendo 1 minuto depois.',
            'Seu cabelo cai, mas cresce de volta dentro de 24 horas.',
            'Você conjura a magia bola de fogo, centrada em você.',
            'Pelo próximo minuto, qualquer objeto inflamável que você toca pega fogo, desde que não esteja sendo usado ou carregado por outra criatura.',
            'Você conjura mísseis mágicos em um alvo qualquer.',
            'Você recupera o uso de uma magia já utilizada de mais baixo nível.',
            'Role 1d10. Sua altura muda uma quantidade de centímetros igual ao resultado do dado. Se o valor for um número ímpar, você encolhe. Se o valor for par, você cresce.',
            'Pelo próximo minuto, você deve gritar sempre que fala.',
            'Você conjura a magia confusão, centrada em você.',
            'Você lança a magia névoa obscurecente, centrada em você.',
            'Durante 1 minuto, você recebe cura acelerada 5.',
            'Até 3 criaturas a sua escolha dentro de 9m de distância recebem 4d10 pontos de dano elétrico.',
            'Uma longa barba feita de penas surge em seu rosto. A barba permanece até que você espirre, quando então as penas explodem para fora do seu rosto.',
            'Você fica apavorado em relação a criatura mais próxima até o fim do seu próximo turno.',
            'Você lança área escorregadia, centrada em você.',
            'Todas as criaturas a até 9m de você se tornam invisíveis durante 1 minuto. A invisibilidade termina se a criatura atacar ou conjurar uma magia.',
            'Criaturas recebem -4 em testes de resistência para resistir a uma de suas magias, lançada no próximo minuto.',
            'Todo dano que você receber pelo próximo minuto é reduzido à metade.',
            'A cor de sua pele muda para um tom vibrante de azul. A magia remover maldição pode anular esse efeito.',
            'Uma criatura aleatória a até 18m de você fica exausta por 1d4 horas.',
            'Um olho aparece em sua testa por 1 minuto. Durante esse tempo, você recebe +4 em testes de Percepção para procurar e observar.',
            'Você começa a brilhar, emitindo uma luz intensa com 9m de raio, durante o próximo minuto. Qualquer criatura que termine seu turno adjacente a você fica cega por uma rodada.',
            'Pelo próximo minuto, todos as suas magias com tempo de execução de uma ação padrão passam a ser conjuradas com uma ação de movimento.',
            'Você lança a magia metamorfose tórrida sobre si. Se falhar no teste de resistência, você se transforma em uma ovelha por uma hora.',
            'Você é teletransportado a até 18m para um espaço desocupado a sua escolha, e que você possa ver.',
            'Borboletas ilusórias e pétalas de rosas flutuam ao seu redor durante 1 minuto.',
            'Você é transportado para o plano astral até o fim de seu próximo turno, quando então retorna para sua posição original no plano material, ou o espaço desocupado mais próximo.',
            'Você recebe uma ação padrão adicional nesse turno.',
            'Sua próxima magia de dano lançada dentro de 1 minuto recebe os efeitos do talento Maximizar Magia.',
            'Todas as criaturas dentro de 9m de você sofrem 1d10 pontos de dano de energia negativa. Você recupera uma quantidade de pontos de vida iguais ao dano sofrido pelas criaturas.',
            'Role 1d10. Sua idade muda uma quantidade de anos igual ao resultado da rolagem. Se o valor for um número ímpar, você se torna mais jovem. Se o valor for par, você se torna mais velho.',
            'Você lança reflexos sobre si.',
            '1d6 cogumelos anões* controlados pelo mestre surgem a até 18m. Os cogumelos estarão apavorados em relação a você e desaparecem depois de 1 minuto.',
            'Você lança voo sobre uma criatura aleatória a até 18m de você.',
            'Você recupera 2d10 pontos de vida.',
            'Você se torna invisível pelo próximo minuto. Durante esse tempo, outras criaturas não podem ouvi-lo. A invisibilidade termina se você atacar ou lançar uma magia.',
            'Você se transforma em um vaso de planta até o começo de seu próximo turno. Enquanto estiver nesse estado, você é considerado indefeso contra todo tipo de ataque e não pode se mover. Se você for reduzido a 0 PV ou menos, você retorna para sua forma original.',
            'Se você morrer durante o próximo minuto, você imediatamente retorna à vida, de modo similar a magia reincarnação.',
            'Durante o próximo minuto, você pode se teletransportar para até 6m de distância como uma ação livre, uma vez por rodada.',
            'Você aumenta em uma categoria de tamanho pelo próximo minuto.',
            'Você lança levitação sobre você.',
            'Você e todas as criatura a até 9m de você recebem vulnerabilidade a dano de perfuração pelo próximo minuto.',
            'Um unicórnio** controlado pelo mestre surge em uma posição adjacente a você. Ele desaparece 1 minuto depois.',
            'Você fica rodeado por uma música sutil e etérea, pelo próximo minuto.',
            'Você não consegue falar pelo próximo minuto. Sempre que tenta, bolhas cor-de-rosa flutuam para fora de sua boca. Lançar uma magia exige um teste de Identificar Magia CD 15.',
            'Você recupera todos os PM gastos durante o dia, e pode usá-los imediatamente para preparar magias.',
            'Se tiver acesso ao bestiário do 13a Era, você acidentalmente invoca 1d3 wibbles (p. 222) que ou o atacam ou buscam causar pe-quenos distúrbios em outro lo-cal da batalha. Se o Mestre não gostar dessa ideia ou não tiver o Bestiário, bolhas de ar enormes saem da sua pele (uma vez) e lhe causam dano equivalente a 1d3 xseu nível.',
            'Você é atingido por uma pequena dobra temporal pulsante. Seu movimento e fala são um pouquinho mais lentos do que deveriam até que consiga se recuperar. Não há efeito neste turno, mas ao final dele diminua sua iniciativa em 2d6 pontos até um mínimo de 1.',
            'Cada criatura na batalha com pontos de vida temporário perde metade destes.',
            'Você só consegue falar através de perguntas. Se você ou seu personagem violar essa exigência, seu personagem leva 1 de dano na primeira vez, 2 na segunda e assim por diante. (Peça que outro jogador fique de olho.)',
            'As peculiaridades dos seus itens mágicos tomam controle. Se você não estiver conseguindo interpretar esse desastre de personalidade muito bem, o Mestre e os outros jogadores estão autorizados a sugerir um comportamento (in)apropriado.',
            'Você passa a absorver traços de sonalidades de espíritos do local, seja lá quais sejam. É um desafio de atuação improvisada! Felizmente para seus aliados, são apenas traços e não trocas completas de personalidade.',
            'Você precisa falar na voz que imagine ser a da última criatura que seu mago do caos atacou. Se a criatura parecer não ter voz, invente uma com sua incrível habilidade de interpretação.',
            'Pequenos roedores guinchantes surgem de qualquer esconderijo possível do qual você se aproximar. Não há nenhum efeito real além do fato de serem um tanto barulhentos e o fato de roedores surgirem de lugares inesperados.',
            'A sua canção favorita (do PJ) co-meça a tocar magicamente ao seu redor, ficando cada vez mais e mais alta (diga à mesa que tipo de música é ou então cantarole-a). Isso pode ou não interferir com canções bárdicas ou monstros que precisam ser ouvidos claramente para causar seu efeito terrível.',
            'Seu sexo é trocado. A mudança pode ser permanente ao final da estranheza, mas a decisão é sua. O quanto permanente as coisas forem para você.',
            'Chifres ou espinhos de algum tipo começam a crescer por todo seu corpo. Se já possuir chifres, você os perde. Alguns chifres (ou a falta deles) permanecem depois do término da estranheza.',
            'Um de seus braços se torna um tentáculo funcional. Não possui efeito na mecânica do jogo, mas a não ser que você seja especial ou sortudo, não será um tentáculo muito bonito. Você decide se ele permanece ou não depois do término da estranheza.',
            'Um rajada de vento poderosa circula pelo campo de batalha. Provavelmente não causa nenhum efeito sério, a não ser que algo que esteja acontecendo possa ser afetado por uma grande rajada de vento.',
            'Todas as criaturas deixam rastros coloridos conformem se movem, transformando a batalha em uma obra de arte estranha e colorida. As imagens desaparecem após cerca de 10 segundos.',
            'Há uma mudança em um pequeno detalhe da sua aparência: cor de cabelo, espaços entre os dentes, se você é destro ou canhoto, etc. Esta mudança, sabe, é meio permanente.',
            'Há uma explosão de areia, poeira explosiva ou outro tipo de fragmentos ao seu redor, causando 1d4 de dano por patamar a cada criatura próxima.',
            'Há uma tensão no ar, ou o ruído de um trovão distante, ou uma sensação de desastre iminente. A próxima criatura que errar um ataque nesta batalha leva um dano igual ao seu modificador de Carisma (dobre seu modificador de Carisma no 5° nível; triplique-o no 8° nível).',
            'Auras esvoaçantes tremem e criam imagens borradas pelo campo de batalha, ou surgem ventos gelados que aquecem conforme passam, ou as luzes fraquejam e piscam... e a criatura que levou a maior quantidade de dano na batalha ganha o equivalente a 10% dos seus pontos devida em pontos de vida temporários.',
            'Uma criatura aleatória da batalha (que não seja você) se teleporta para o lado de um de seus inimigos aleatórios (que não seja você) e passa a estar engajada a ele.',
            '(Efeito global) Há uma séria distorção no espaço, afetando magias e ataques a distância de todas as criaturas na batalha: criaturas próximas contam como se estivessem longe, enquanto criaturas ao longe contam como estando próximas.',
            'A primeira magia que você conjurar neste combate possuirá efeitos (não dano) de uma magia dois níveis acima dela, se possível.',
            '(Efeito global) Todos os testes normais de resistência feitos por criaturas no combate passam a ser testes fáceis (6+).',
            '(Efeito global) As bordas de tudo ao redor ficam borradas. Nenhuma criatura consegue interceptar outra. Tentativas de desengajar são bem-sucedidas automaticamente.',
            '(Efeito global) Os campeões levam nada! Até o final de seu próximo turno, testes de resistência que falharem contam como bem-sucedidos, enquanto testes de resistência bem-sucedidos contam como erros!',
            'Role o dado de intensidade e use o novo resultado.',
            '(Efeito global) Cada criatura na batalha que esteja levando dano contínuo recebe aquele dano imediatamente. Em seguida, todos os efeitos de dano contínuo cessam.',
            '(Efeito global) Cada criatura que faça um ataque contra DF na verdade atacará DM. Ataques contra DM passam a atacar DF.',
            'Sua sombra se separa e se move agitadamente ao seu redor. Até o final desta estranheza, você recebe um bônus de +2 no ataque, mas uma penalidade de -2 em testes de resistência. Sua personalidade pode ou não ser afetada. Isso fica a seu critério.',
            'Escolha a si mesmo ou um aliado com pontos de vida temporário e dobre esses pontos de vida. Se não houver ninguém com PV temporários, que pena!',
            'Um efeito especial mágico (não mecânico) de grande escala ocorre, à sua escolha, e toda criatura no combate ignora todas as resistências.',
            'Você ganha uma ação rápida adicional a cada um de seus turnos enquanto esta estranheza estiver em efeito.',
            'Quando um de seus aliados conjurar uma magia arcana nesta batalha, essa magia recebe um pequeno efeito extra escolhido pelo Mestre (algo que combine com a magia e com a trama).',
            'Você e seus aliados recebem pequenas auréolas, ou uma luz divina se esparrama pelo local, ou suas faces começam a brilhar sutilmente. Quando um de seus aliados conjurar uma magia divina nesta batalha, essa magia recebe um pequeno efeito extra escolhido pelo Mestre (algo que combine com a magia e com a trama).',
            '''Suas características são embaralhadas, formando outra combinação. Você recebe um poder racial aleatório
              até o final do seu próximo turno. Igno-
              re resultados que dupliquem um po-
              der racial que já possua. Role um d8. 
              1: poder anão “esse é o seu melhor golpe?”
              2: poder de elfo negro “cruel”
              3: poder de alto elfo “teleporte do sangue nobre”
              4: poder de gnomo “confusão”
              5: poder de meio-elfo “surpresa”
              6: poder de halfling “evasivo”; 7: poder de sagrado “halo”
              8: poder de tiefling “maldição do caos”.
              (Veja o capítulo 3 do livro bási-
              co de 13a Era para mais detalhes sobre poderes raciais.)''',
            'Se um de seus aliados estiver com 0 pontos de vida ou menos, esse aliado pode rolar um teste de resistência contra morte gratuitamente, que não contará no total de falhas em testes contra morte.',
            'Escolha uma criatura (incluindo você) que já tenha se revigorado neste combate. Ela poderá se revigorar novamente neste combate (usando a mesma ação que usaria normalmente) como se ainda não tivesse se revigorado (não há rolagem se for a primeiro uso).',
            'Sua presença é um borrão através do espaço, espírito e tempo; você pode lutar em espírito no seu turno (livro básico do 13a Era, página 166) além de agir normalmente em seu turno.',
            'Seu corpo se desloca, ondula ou fica transparente. Você não recebe nenhum dano de erro enquanto esta estranheza o afetar.',
            'Os itens mágicos da área começam a falar imediatamente. Você ou um aliado a sua escolha pode rolar para recarregar um item mágico (à escolha da criatura afetada).',
            'Algo relacionado a sua singularidade dá muito certo para você. Cabe a você e o Mestre decidirem juntos o que. Contudo, a palavra final é do Mestre.',
            'Se você e seus aliados fugirem IMEDIATAMENTE (livro básico do 13a Era, p. 166), pode ser difícil de explicar. É tudo culpa da magia caótica.',
            'Role mais duas vezes nesta tabela. Se quiser poderá ignorar um dos resultados rolados, mas precisa ficar com o outro. Se rolar o mesmo resultado duas vezes, essa estranheza ocorre apenas uma vez',
            'Você recebe uma ação padrão extra durante seu próximo turno depois que esta estranheza esteja em efeito.',
            ]

        random_effect = randint(0, len(efects))
        await ctx.send(efects[random_effect])

    @commands.command(name='clima')
    async def weather_define(self, ctx):
        clima = ['Sol', 'chuva', 'nublado', 'Muito calor', 'Chuva Forte', 'Ventania']
        generator = randint(0, len(clima) - 1)
        url = ['https://i.pinimg.com/564x/8c/c6/cd/8cc6cd483b1969b8a3a8ebc4970da71d.jpg',
               'https://i.pinimg.com/564x/05/a8/0f/05a80f51472175f1015a49c275ff6929.jpg',
               'https://i.pinimg.com/564x/c2/9b/8e/c29b8e4ef8bc2f853469cd6af616ef8e.jpg',
               'https://i.pinimg.com/564x/0b/8b/5c/0b8b5ca8129c95cce6e81b19ba1206fe.jpg',
               'https://i.pinimg.com/564x/d9/c4/dd/d9c4dd6768c57881cb3a6e44c06d5613.jpg',
               'https://i.pinimg.com/564x/17/3d/75/173d7582fa667f1eaa5c7905cef99426.jpg']

        embed_image = discord.Embed(
            title=clima[generator],
            color=0x00FFFF
        )

        embed_image.set_image(url=url[generator])

        response = generator

        await ctx.send(embed=embed_image)

    @commands.command(name="item")
    async def item_generator(self, ctx):
        item = ['Arma Animada', 'Camisa de Tecido Mágico', 'Cajado do Feitiço Desesperado',
                'Símbolo Blasfemo', 'Anel das Palavras Adocicadas:', 'Cinto da Humildade',
                'Escudo da Aversão do Destino',
                'Anel do Ciclo', 'Armadura Enraizada']

        item_description = ['''Durante toda a batalha, ou até errar um ataque, esta arma pode fazer ataques básicos
    sozinha em qualquer turno que não usá-la para fazer um ataque. Ela usa +5 como seu bônus de ataque (campeão:
    +10; épico: +15). Este ataque básico não pode ativar ataques flexíveis; trate-o como se um aliado estivesse atacando um
    inimigo. A espada não se beneficia do dado de intensidade. Lembre-se, você só pode se conectar com uma arma mágica
    por vez – se tiver uma arma animada, você não pode usar outra arma corpo a corpo mágica.''',
                            '''Quando conjurar uma magia que tem você como alvo,  você também carrega a camisa com esta magia.
    Quando a camisa está carregada, você pode ativá-la como uma ação livre para  receber os benefícios da magia por uma rodada. 
    A magia precisa ser uma que dure por uma batalha inteira – não é possível carregá-la com porta dimensional ou teleporte. 
    Por exemplo, se conjurar borrão em si mesmo numa luta, você pode usar a camisa para lançar borrão novamente, por uma rodada, 
    numa batalha futura. A aparência da camisa se modifica para refletir a magia carregada – se você colocar queda suave nela, 
    ela se tornará fofinha e sedosa; se estiver guardando respirar debaixo d’água, ela fica verde e gruda na pele.''',
                            '''Ative este cajado como uma ação livre para ignorar qualquer condição de entorpecido,
    obstruído ou enfraquecido afetando-o ao fazer um ataque de magia arcana. O cajado não se livra das condições – só fortalece
    a magia para ele atravessá-las.''',
                            '''Ao conjurar uma magia que permite a um aliado se curar usando uma recuperação,
    você pode decidir invocar o poder desta relíquia antes que a recuperação seja rolada. O aliado pode re-rolar qualquer dado
    de recuperação que rolar 1 ou 2. Este aliado fica endividado a realizar um serviço para os Deuses da Escuridão. Você
    especifica o serviço – auxiliar o Cruzado, apoiar os Deuses da Escuridão contra os Deuses da Luz, pilhar um templo,
    fazer uma oferenda para o templo dos Deuses da Escuridão, exigir um pedaço maior do tesouro para você...
    Se o aliado se recusar a realizar o serviço (ou se o serviço for considerado mesquinho ou irrelevante demais), você e o
    aliado serão amaldiçoados de alguma forma. A natureza da maldição depende do serviço, mas quase certamente terá a ver
    com algo desagradável ou repugnante que não interfere com a sua habilidade de servir aos Deuses. Prepare-se para pústulas.''',
                            ''''Este anel de sinete tem o símbolo da Diabolista e é grande o suficiente para ser notado do
    outro lado de uma sala. Enquanto usa-lo, você recebe +6 de bônus em testes de perícia para convencer alguém a ajudar 
    você de alguma forma. Seu alvo fica magicamente compelido a analisar seu caso favoravelmente, pensando em você como alguém
     eloquente, interessante e mais do que sensual. Entretanto, ele possui o efeito oposto em todas as outras
    testemunhas da conversa, incluindo outros PJs – eles acreditam que você é dissimulado, manipulativo e rude, independente
     do que você disser ou fizer. Ah, que seja, não é como se eles pudessem causar problemas mais tarde.
    Você pode tentar evitar a restrição do anel ao insistir em uma conferência particular. É claro que isso não vai deixar 
    ninguém suspeito nem paranoico.''',
                            '''Este simples cinto de couro permite você passar num teste de resistência
    (incluindo um teste de morte) ou usar uma recuperação para se curar, mas só quando realmente precisar. Você só pode usar
    este item quando estiver com 10 ou menos pontos de vida, ou numa situação similarmente perigosa. Após usar o cinto, você
    precisa pagar seu débito ao cosmo, e faz isso ou sacrificando outro item mágico verdadeiro, ou aceitando uma missão sem
    nenhuma oferta ou esperança de recompensa.''',
                            '''Este escudo polido porta o símbolo de um Signo. Uma vez por nível, ao sofrer um revés na 
    campanha (página 166 do livro básico de 13a Era), você pode invocar o poder do escudo para prevenir os piores efeitos do 
    revés. Coisas ruins ainda acontecem, mas eventos conspiram para te dar uma chance de luta para consertar as coisas. Tomando 
    o exemplo do livro, se os personagens estavam a caminho de resgatar um cativo de um sacrif ício profano e sofrem um revés 
    na campanha através da fuga, então, sem o escudo, a vítima acaba sendo morta. Com o escudo, talvez o cativo esteja sangrando 
    quando chegar na câmara ritualística, e se conseguirem chegar até ele com rapidez, podem salvar sua vida. Ou talvez esteja 
    morto, mas existem espíritos da luz impedindo o demônio convocado, então há uma chance de impedir que a alma dela seja 
    consumida. Os poderes da luz tratam com mais leniência aos reveses na campanha sofridos por causa de rolagens de dados 
    bem ruins do que em revés ocorridos através da hesitação, decisões ruins ou covardia.''',
                            '''Quando um aliado próximo falha em um teste contra morte ou de último suspiro, você pode 
    cancelar esta falha e manter o aliado vivo. Entretanto, cada vez que fizer isso, você deve escolher outro aliado próximo 
    para “perder” um teste contra morte. Se este segundo aliado cair a pontos de vida negativo e precisar realizar
    testes de resistência, isso fará com que eles morram após um teste contra morte a menos do que o normal. (Geralmente, 
    você morre após quatro falhas contra morte; se alguém usar o anel do ciclo em você, você morrerá após três.)
    O anel do ciclo não pode ser usado para preservar alguém que já perdeu um teste contra morte para o anel.
    Testes contra morte “enchem” de novo quando um personagem passa de nível. Você não pode usar o anel do ciclo em si mesmo, 
    seja para se salvar ou para sacrificar sua própria força vital para salvar outros. Druidas devem estar de fora do ciclo 
    da vida'''
                            '''Raízes e gavinhas se arrastam deste traje de armadura pesada. No comando, a armadura se 
    enraíza no chão, aumentando seu bônus para a CA em +1, mas mantendo o usuário preso. Libertar a armadura do chão e 
    terminar a condição de preso exige uma ação padrão; o bônus de +1 na CA é perdido assim que o usuário se desprende''']

        quirk = ['Adora delegar', 'Compelido a modificar seu penteado e vestimentas para complementar a camisa.',
                 'GRITA DEMAIS', 'Exige respeito e tributo em excesso', 'Gorduroso',
                 'Incapaz de falar sem ser evasivo.',
                 'Incapaz de dizer "não" para um pedido de ajuda',
                 'Sempre pensa nos piores resultados que provavelmente nunca acontecerão',
                 'Bizarramente alegre na presença da morte', 'Sono pesado'
                 ]

        recarga = ['11+', '11+', '16+', '11+', 'Não tem', '11+', 'Não tem', 'Não tem', 'Ação rápida => 6+']

        url_image = [
            'https://cdnb.artstation.com/p/assets/images/images/031/982/849/large/mukhlis-nur-sinlaire-sword-018-nature-inspired-copy.jpg?1605134763',
            'https://i.pinimg.com/564x/bf/f0/a3/bff0a38b5afc90e53c3c00b80deb26c9.jpg',
            'https://i.pinimg.com/564x/f7/a0/50/f7a050e416d480e637a3d43318b8ac1d.jpg',
            'https://i.pinimg.com/564x/d8/e4/96/d8e4966ff16b8535ab54bdb2c2ed4de1.jpg',
            'https://i.pinimg.com/564x/de/6f/ef/de6fefdabd9b1e91349dd105f7a46573.jpg',
            'https://i.pinimg.com/736x/25/31/19/2531196727563cf09d2daa69ab9d7938.jpg',
            'https://i.pinimg.com/564x/b4/64/26/b464260d3582381f23798ca8f5da85f8.jpg',
            'https://i.pinimg.com/564x/23/0b/e8/230be875630872e2b9a4fea2bf85b7ca.jpg',
            'https://i.pinimg.com/564x/49/1e/b6/491eb6ef0c95e195b3d39baca32ff306.jpg'
        ]
        generator = randint(0, len(item) - 1)
        name = ctx.author.name

        embed_image = discord.Embed(
            title=f'{item[generator]}',
            color=0x00FFFF
        )

        embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed_image.set_footer(text=f'{self.bot.user.name} é um bot do Davus', icon_url=self.bot.user.avatar_url)

        embed_image.add_field(name='Bônus', value='+ 1')
        embed_image.add_field(name='Peculiaridade', value=f'{quirk[generator]}')
        embed_image.add_field(name='Recarga', value=f'{recarga[generator]}')
        embed_image.add_field(name='Efeito', value=f'{item_description[generator]}', inline=False)

        embed_image.set_image(url=url_image[generator])

        await ctx.send(embed=embed_image)

def setup(bot):
    bot.add_cog(Generators(bot))
