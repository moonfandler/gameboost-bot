import discord
from discord.ext import commands
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
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Online como {bot.user}")

@bot.tree.command(name="anunciar", description="Manda texto no canal")
async def anunciar(interaction: discord.Interaction, mensagem: str):
    canal = bot.get_channel(CANAL_ID)
    await canal.send(mensagem)
    await interaction.response.send_message("Enviado!", ephemeral=True)

bot.run(os.environ.get("TOKEN"))
