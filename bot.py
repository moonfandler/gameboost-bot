import discord
from discord import app_commands
from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot GameBoost On!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot logado como {bot.user}")

@tree.command(name="anunciar", description="Seu texto já sai organizado igual do print")
@app_commands.describe(texto="Cole seu texto aqui. Use \\n para quebrar linha")
async def anunciar(interaction: discord.Interaction, texto: str):
    # Isso arruma a desorganização e quebra as linhas
    texto_arrumado = texto.replace("\\n", "\n")

    embed = discord.Embed(
        description=texto_arrumado,
        color=0x00FF00
    )
    embed.set_image(url="https://p16-flow-image-sign.ibyteimg.com/tos-mya-i-3rsxbfecgb/rc_gen_image/987665ba49dc494696f0847376401708.jpeg~tplv-0es2k971ck-image.image?rcl=2026090413411421ACB6BC0900447C92D7&rk3s=8e244e95&rrcfp=02a80fc2&x-expires=1791092495&x-signature=OIJeKOlaaXQVcvvndLZPfHm3hU4%3D")

    await interaction.response.send_message(embed=embed)

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
