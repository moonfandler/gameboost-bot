import discord
from discord.ext import commands
import os
from flask import Flask
import threading

# pra não cair no Render
app = Flask('')
@app.route('/')
def home(): return "Bot online"
threading.Thread(target=lambda: app.run(host='0.0.0.0', port=8080)).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logado como {bot.user}")

@bot.command(name="regras")
async def regras(ctx):
    embed = discord.Embed(
        title="GameBoost Marketplace | Regras e Orientações",
        color=0x2ECC71, # barrinha verde fina igual BR2G
        description=(
            "·  📜 **Siga os [Termos de Serviço](https://discord.com/terms) e as [Diretrizes da Comunidade](https://discord.com/guidelines)**\n"
            "Todos devem seguir os Termos do Discord. Descumprimento = blacklist.\n\n"
            "·  ✅ Use o serviço oficial de Middleman quando solicitado.\n\n"
            "·  ⚠️ Ao abrir ticket, inclua detalhes e links relevantes.\n\n"
            "·  🔒 Não compartilhe dados pessoais ou senhas.\n\n"
            "·  💬 Dúvidas? Contate <@634098800822059012> ou <#1544753178434867390>\n\n"
            "·  **Atividades Maliciosas**\n"
            "Fraude, cookie logger, phishing = blacklist permanente.\n\n"
            "·  **Trocas e Divulgação**\n"
            "DM de publicidade é proibida. Use <#1544752499670384720>."
        )
    )
    embed.set_footer(text="GameBoost Marketplace")
    await ctx.send(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
