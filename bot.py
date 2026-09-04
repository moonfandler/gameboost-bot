import discord
from discord import app_commands
from flask import Flask
from threading import Thread
import os

# --- PARTE DO SITE PRA NÃO DORMIR NO RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot GameBoost On!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- PARTE DO BOT DO DISCORD ---
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot logado como {bot.user} - {len(tree.get_commands())} comandos sincronizados!")

# SEU COMANDO ANUNCIAR ARRUMADO
@tree.command(name="anunciar", description="Anunciar no marketplace da GameBoost")
@app_commands.describe(
    produto="Nome do produto que você quer anunciar"
)
async def anunciar(interaction: discord.Interaction, produto: str):
    # FIX DO ERRO "O aplicativo não respondeu"
    await interaction.response.defer(ephemeral=True)

    embed = discord.Embed(
        title="GameBoost Marketplace",
        description=f"✅ **Anúncio criado com sucesso!**\n\nProduto: **{produto}**\nAnunciado por: {interaction.user.mention}",
        color=0x5865F2
    )
    embed.set_footer(text="GameBoost Marketplace • APP")
    
    # Manda no canal onde usou o comando
    await interaction.channel.send(embed=embed)
    
    # Responde pra você que deu certo
    await interaction.followup.send(f"Anunciado: {produto}", ephemeral=True)

# INICIA TUDO
keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
