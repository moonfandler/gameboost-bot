import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# --- CONFIG ---
COR_BORDA = 0x5865F2
TOKEN = os.getenv("TOKEN")

# --- FLASK PRA MANTER ONLINE (se você usa) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot online!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# --- BOT ---
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")
    try:
        synced = await tree.sync()
        print(f"{len(synced)} comandos sincronizados")
    except Exception as e:
        print(e)

# --- COMANDO CORRIGIDO: AGORA ELE USA O TEXTO QUE VOCÊ DIGITA ---
@tree.command(name="anunciar", description="Envia um anúncio para o canal")
async def anunciar(interaction: discord.Interaction, texto: str, titulo: str = "📢 Anúncio - GameBoost Marketplace"):
    # só ADM
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Só ADM pode usar.", ephemeral=True)
        return

    embed = discord.Embed(
        title=titulo,
        description=texto,
        color=COR_BORDA
    )
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    embed.set_footer(text="🚀 GameBoost Marketplace", icon_url=bot.user.display_avatar.url)

    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("✅ Enviado!", ephemeral=True)

# Inicia flask em segundo plano
Thread(target=run_flask).start()

bot.run(TOKEN)
