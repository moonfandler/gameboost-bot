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

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Online como {bot.user}")

@bot.tree.command(name="anunciar", description="Anúncio bonito da GameBoost")
@app_commands.describe(mensagem="Texto do anúncio")
async def anunciar(interaction: discord.Interaction, mensagem: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Só ADM!", ephemeral=True)
        return

    embed = discord.Embed(
        title="⚠️ ATENÇÃO - Plataforma Oficial",
        description=f"### 🔗 Link Oficial:\n**https://www.gameboost.com/**\n\n{mensagem}\n\n---\n**🛒 Quer comprar itens?**\nAcesse nosso site oficial para ver novidades e ofertas.\n\n**💬 Precisa de ajuda?**\nNosso suporte funciona **24h**. Abra um ticket em <#{1544751928108388392}> e nossa equipe te ajuda!",
        color=0x9B0000
    )
    embed.set_footer(text="GameBoost Marketplace • Suporte 24 horas", icon_url="https://www.gameboost.com/favicon.ico")
    embed.set_thumbnail(url="https://www.gameboost.com/favicon.ico")

    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("✅ Anúncio bonito enviado!", ephemeral=True)

bot.run(os.getenv("TOKEN"))
