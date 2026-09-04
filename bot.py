import discord
from discord import app_commands
import os
from flask import Flask
import threading

# Mantém o Render acordado
app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"
def run_flask():
    app.run(host='0.0.0.0', port=8080)
threading.Thread(target=run_flask).start()

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot logado como {bot.user}")

@tree.command(name="anunciar", description="Anuncia os termos bonitinhos")
async def anunciar(interaction: discord.Interaction):
    COR_BORDA = 0x5A65FF  # azul/roxo neon que combina com seu logo

    embed = discord.Embed(
        title="📜 Termos de Serviço - GameBoost Marketplace",
        color=COR_BORDA
    )
    embed.set_thumbnail(url=bot.user.display_avatar.url)

    embed.add_field(name="📌 Ao usar nossos serviços você concorda com:", value="\u200b", inline=False)
    
    embed.add_field(name="⚠️ Responsabilidade e Blacklist", value="Pode resultar em blacklist temporária ou permanente do serviço. Não somos responsáveis por itens ou fundos perdidos durante ou depois da troca.", inline=False)
    
    embed.add_field(name="🤖 Sobre Erros do Middleman", value="Mesmo que a perda aconteça por um erro do Middleman, não assumimos responsabilidade. Somos humanos e erros podem acontecer. Se você espera uma experiência totalmente sem erros, use um serviço automatizado de Middleman.\n\n> Ex: itens duplicados ou excluídos.", inline=False)
    
    embed.add_field(name="💳 Detalhes do Pagamento", value="Confira todos os dados de pagamento antes de confirmar a troca. Não assumiremos responsabilidade por erros como endereço de cripto, nomes de usuário ou dados de pagamento incorretos.", inline=False)
    
    embed.add_field(name="ℹ️ Informações Adicionais", value="Usar extensões ou sistemas como RoEarn, catálogos dentro do jogo ou métodos de doação que tentam 'salvar' Robux fará o recebedor receber **10% a menos**. Isso também se aplica a jogos como PLS DONATE.", inline=False)

    embed.set_footer(text="🚀 GameBoost Marketplace", icon_url=bot.user.display_avatar.url)

    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("✅ Enviado!", ephemeral=True)

bot.run(os.getenv("TOKEN"))
