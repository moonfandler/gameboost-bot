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

@bot.tree.command(name="anunciar", description="Anúncio bonito estilo BR2G")
@app_commands.describe(mensagem="Mensagem principal do anúncio")
async def anunciar(interaction: discord.Interaction, mensagem: str):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("❌ Só ADM!", ephemeral=True)
        return

    embed = discord.Embed(
        title="GameBoost Marketplace | Regras e Orientações",
        description=f"""
{mensagem}

· 📜 **Siga os Termos de Serviço e as Diretrizes da Comunidade do Discord**
GameBoost Marketplace funciona na plataforma Discord. Todos os membros devem seguir os Termos de Serviço.

· ✅ **Use o serviço oficial da GameBoost quando solicitado.**

· ⚠️ **Ao abrir um ticket, inclua os detalhes e links relevantes** quando necessário.

· 🔒 **Não compartilhe dados pessoais ou senhas.**

· 💬 **Se algo der errado, entre em contato com a equipe ou o suporte.**

Para mais informações, acesse **[https://www.gameboost.com/](https://www.gameboost.com/)** ou abra um ticket em <#{1544751928108388392}>.
""",
        color=0x00D26A  # verde igual da foto
    )
    embed.set_footer(text="GameBoost Marketplace • Suporte 24 horas")

    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("✅ Anúncio no estilo BR2G enviado!", ephemeral=True)

bot.run(os.getenv("TOKEN"))
