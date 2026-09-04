import discord
from discord.ext import commands
from discord import app_commands
from flask import Flask
from threading import Thread
import os

app = Flask('')
@app.route('/')
def home(): return "GameBoost Online!"
def run(): app.run(host='0.0.0.0', port=8080)
Thread(target=run).start()

CANAL_ID = 1544751928108388392

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Online como {bot.user}")

@bot.tree.command(name="anunciar", description="Faz o bot falar no canal")
@app_commands.describe(mensagem="O que o bot vai escrever", canal="Qual canal (opcional)")
async def anunciar(interaction: discord.Interaction, mensagem: str, canal: discord.TextChannel = None):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Só ADM pode usar!", ephemeral=True)
        return
    if canal is None:
        canal = bot.get_channel(CANAL_ID) or interaction.channel
    await canal.send(mensagem)
    await interaction.response.send_message(f"✅ Enviado em {canal.mention}", ephemeral=True)

bot.run(os.getenv("TOKEN"))
