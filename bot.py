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
    await interaction.response.defer(ephemeral=True)

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
    
    embed.set_image(url="COLOQUE_O_LINK_DA_SUA_IMAGEM_AQUI")

    await interaction.channel.send(embed=embed)
    await interaction.followup.send("Regras enviadas!", ephemeral=True)

@tree.command(name="anunciar", description="Anunciar no marketplace")
@app_commands.describe(produto="Nome do produto")
async def anunciar(interaction: discord.Interaction, produto: str):
    await interaction.response.defer(ephemeral=True)

    embed = discord.Embed(
        title="BR2G Marketplace",
        description=f"✅ **Anúncio:** **{produto}**",
        color=0x5865F2
    )

    embed.set_image(url="COLOQUE_O_LINK_DA_SUA_IMAGEM_AQUI")

    await interaction.channel.send(embed=embed)
    await interaction.followup.send(f"Anunciado: {produto}", ephemeral=True)

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
