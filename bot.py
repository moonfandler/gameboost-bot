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

class AnunciarModal(discord.ui.Modal, title="Criar Anúncio Organizado"):
    texto = discord.ui.TextInput(
        label="Cole seu texto aqui",
        style=discord.TextStyle.paragraph,
        placeholder="Cole aqui... pode dar ENTER a vontade que vai ficar organizado",
        required=True,
        max_length=4000
    )

    async def on_submit(self, interaction: discord.Interaction):
        conteudo = self.texto.value
        conteudo = conteudo.replace(" · ", "\n\n· ").replace(" - ", "\n\n- ")

        embed = discord.Embed(
            description=conteudo,
            color=0x8A2BE2
        )
        embed.set_image(url="attachment://banner.png")
        file = discord.File("banner.png", filename="banner.png")

        await interaction.response.send_message(embed=embed, file=file)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"Bot logado como {bot.user}")

@tree.command(name="anunciar", description="Abre a janela para colar seu texto organizado")
async def anunciar(interaction: discord.Interaction):
    await interaction.response.send_modal(AnunciarModal())

keep_alive()
bot.run(os.getenv("DISCORD_TOKEN"))
