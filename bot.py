import discord
from discord import app_commands
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot GameBoost On!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot logado como {bot.user}")

@tree.command(name="regras", description="Manda as regras com a logo embaixo")
async def regras(interaction: discord.Interaction):
    descricao_regras = """
ou captura de IP.
Qualquer envolvimento em atividade maliciosa ou ilegal resultará em blacklist permanente e poderá ser denunciado ao Discord Trust & Safety.

**· Trocas e Divulgação**
Publicidade ou autopromoção não autorizada por DM é proibida.
Para comprar um anúncio ou divulgar um serviço, contate @Violet diretamente.
Para trocas, use o canal #⟫・trocas-e-vendas.

**· Observações Adicionais**
As regras e políticas podem mudar a qualquer momento sem aviso prévio.
Use o bom senso, seja respeitoso e ajude a manter BR2G Marketplace seguro, organizado e profissional.
"""

    embed = discord.Embed(
        description=descricao_regras,
        color=0x00FF00
    )
    
    embed.set_image(url="https://p16-flow-image-sign.ibyteimg.com/tos-mya-i-3rsxbfecgb/rc_gen_image/987665ba49dc494696f0847376401708.jpeg~tplv-0es2k971ck-image.image?rcl=2026090413411421ACB6BC0900447C92D7&rk3s=8e244e95&rrcfp=02a80fc2&x-expires=1791092495&x-signature=OIJeKOlaaXQVcvvndLZPfHm3hU4%3D")

    await interaction.response.send_message(embed=embed)

@tree.command(name="anunciar", description="Anunciar no marketplace")
@app_commands.describe(produto="Nome do produto")
async def anunciar(interaction: discord.Interaction, produto: str):
    embed = discord.Embed(
        title="BR2G Marketplace",
        description=f"✅ **Anúncio:** **{produto}**",
        color=0x5865F2
    )
    embed.set_image(url="https://p16-flow-image-sign.ibyteimg.com/tos-mya-i-3rsxbfecgb/rc_gen_image/987665ba49dc494696f0847376401708.jpeg~tplv-0es2k971ck-image.image?rcl=2026090413411421ACB6BC0900447C92D7&rk3s=8e244e95&rrcfp=02a80fc2&x-expires=1791092495&x-signature=OIJeKOlaaXQVcvvndLZPfHm3hU4%3D")

    await interaction.response.send_message(embed=embed)

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
