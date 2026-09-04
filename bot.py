import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="regras")
async def regras(ctx):
    embed = discord.Embed(
        title="GameBoost Marketplace | Regras e Orientações do Middleman",
        color=0x2ECC71,
        description=(
            "·  📜 **Siga os [Termos de Serviço](https://discord.com/terms) e as [Diretrizes da Comunidade](https://discord.com/guidelines) do Discord**\n"
            "GameBoost funciona na plataforma Discord. Todos devem seguir os Termos.\n\n"
            "·  ✅ Use o serviço oficial de Middleman do servidor quando solicitado.\n\n"
            "·  ⚠️ Ao abrir um ticket, inclua os detalhes e links relevantes.\n\n"
            "·  🔒 Não compartilhe dados pessoais ou senhas.\n\n"
            "·  💬 Se algo der errado, contate <@634098800822059012> ou visite <#1544753178434867390>.\n\n"
            "·  **Atividades Maliciosas**\n"
            "Não toleramos fraudes, roubo de cookies ou phishing. Resultará em blacklist.\n\n"
            "·  **Trocas e Divulgação**\n"
            "Publicidade por DM é proibida. Para trocas use <#1544752499670384720>."
        )
    )
    embed.set_footer(text="GameBoost Marketplace")
    await ctx.send(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
