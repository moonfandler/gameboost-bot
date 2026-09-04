import discord
from discord import app_commands
from flask import Flask
from threading import Thread
import os

app = Flask('')
@app.route('/')
def home():
    return "Bot On!"
def run():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

class AnunciarModal(discord.ui.Modal, title="Criar Anúncio"):
    texto = discord.ui.TextInput(label="Cole seu texto aqui", style=discord.TextStyle.paragraph, required=True, max_length=4000)
    async def on_submit(self, interaction: discord.Interaction):
        conteudo = self.texto.value.replace(" · ", "\n\n· ").replace(" - ", "\n\n- ")
        embed = discord.Embed(description=conteudo, color=0x2B88D8)
        file = discord.File("banner.png", filename="banner.png")
        embed.set_image(url="attachment://banner.png")
        await interaction.response.send_message(embed=embed, file=file)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"ONLINE - {bot.user}")

@tree.command(name="anunciar", description="Criar anúncio com banner")
async def anunciar(interaction: discord.Interaction):
    await interaction.response.send_modal(AnunciarModal())

# NOVO COMANDO SEM IMAGEM - tem que ficar AQUI
class TextoModal(discord.ui.Modal, title="Criar Texto sem Imagem"):
    texto = discord.ui.TextInput(label="Cole seu texto aqui", style=discord.TextStyle.paragraph, required=True, max_length=4000)
    async def on_submit(self, interaction: discord.Interaction):
        conteudo = self.texto.value.replace(" · ", "\n\n· ").replace(" - ", "\n\n- ")
        embed = discord.Embed(description=conteudo, color=0x2B88D8)
        await interaction.response.send_message(embed=embed)

@tree.command(name="texto", description="Anunciar SEM imagem")
async def texto_cmd(interaction: discord.Interaction):
    await interaction.response.send_modal(TextoModal())

# ISSO SEMPRE TEM QUE SER O FINAL
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
