import discord
from discord import app_commands
from flask import Flask
from threading import Thread
import os

app = Flask('')
@app.route('/')
def home():
    return "Bot On!"
def run():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# JANELA GRANDE QUE CONSERTA A DESORGANIZAÇÃO
class AnunciarModal(discord.ui.Modal, title="Criar Anúncio Organizado"):
    texto = discord.ui.TextInput(
        label="Cole seu texto aqui",
        style=discord.TextStyle.paragraph,
        placeholder="Cole aqui... pode dar ENTER a vontade que vai ficar organizado",
        required=True,
        max_length=4000
    )

    async def on_submit(self, interaction: discord.Interaction):
        # Isso arruma se você colar tudo embolado
        conteudo = self.texto.value
        # Separa os tópicos automaticamente
        conteudo = conteudo.replace(" · ", "\n\n· ").replace(" - ", "\n\n- ")

        embed = discord.Embed(
            description=conteudo,
            color=0x8A2BE2  # BORDA ROXA
        )
        embed.set_image(url="https://p16-flow-image-sign.ibyteimg.com/tos-mya-i-3rsxbfecgb/rc_gen_image/987665ba49dc494696f0847376401708.jpeg~tplv-0es2k971ck-image.image?rcl=2026090413411421ACB6BC0900447C92D7&rk3s=8e244e95&rrcfp=02a80fc2&x-expires=1791092495&x-signature=OIJeKOlaaXQVcvvndLZPfHm3hU4%3D")

        await interaction.response.send_message(embed=embed)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot logado como {bot.user}")

@tree.command(name="anunciar", description="Abre a janela para colar seu texto organizado")
async def anunciar(interaction: discord.Interaction):
    await interaction.response.send_modal(AnunciarModal())

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
