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

# Config do bot
intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot logado como {bot.user}")

@tree.command(name="anunciar", description="Anuncia os termos bonitinhos")
async def anunciar(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📜 Termos de Serviço - GameBoost Marketplace",
        description=(
            "**Ao usar nossos serviços você concorda com:**\n\n"
            "Pode resultar em blacklist temporária ou permanente do serviço. Não somos responsáveis por itens ou fundos perdidos durante ou depois da troca.\n\n"
            "Mesmo que a perda aconteça por um erro do Middleman, não assumimos responsabilidade. Somos humanas e erros podem acontecer. Se você espera uma experiência totalmente sem erros, use um serviço automatizado de Middleman.\n\n"
            "Ex: itens duplicados ou excluídos.\n\n"
            "**Detalhes do Pagamento:** Confira todos os dados de pagamento antes de confirmar a troca. Não assumiremos responsabilidade por erros como endereço de cripto, nomes de usuário ou dados de pagamento incorretos.\n\n"
            "**Informações Adicionais:** Usar extensões ou sistemas como RoEarn, catálogos dentro do jogo ou métodos de doação que tentam 'salvar' Robux fará o recebedor receber 10% a menos. Isso também se aplica a jogos como PLS DONATE; esses métodos não são recomendados."
        ),
        color=0x00D26A
    )
    embed.set_footer(text="BR2G Marketplace • Middleman Oficial")
    
    await interaction.channel.send(embed=embed)
    await interaction.response.send_message("✅ Enviado bonitinho!", ephemeral=True)

bot.run(os.getenv("TOKEN"))
