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
        conteudo = self.texto.value
        conteudo = conteudo.replace(" · ", "\n\n· ").replace(" - ", "\n\n- ")
        embed = discord.Embed(
            description=conteudo,
            color=0x8A2BE2  # BORDA ROXA
        )
        # IMAGEM ATUALIZADA CONFORME PEDIDO
        embed.set_image(url="https://chatgpt.com/backend-api/estuary/content?id=file_00000000adc4820e8e080051cc3f1ed1&ts=496807&p=fs&cid=1&sig=fef48ae3da814e00afda013c07e83c4430570e640b7865e13d0d06539db6f5f4&v=0")
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
