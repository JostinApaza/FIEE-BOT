import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Comandos slash sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")

@bot.command(name='info')
async def info(ctx):
    embed = discord.Embed(
        title="Información del Bot",
        description="Este es un ejemplo de un comando de texto.",
        color=discord.Color.green()
    )
    embed.add_field(name="Versión", value="1.0.0", inline=True)
    embed.add_field(name="Autor", value="TuNombre", inline=True)
    embed.set_footer(text="Gracias por usar el bot")
    embed.set_thumbnail(url="https://i.imgur.com/rdm3W9t.png")  # opcional

    await ctx.send(embed=embed)


# ///////////////////////////////////////////////////////////////////////////////////////////


def get_embeds():
    embeds = []

    embed1 = discord.Embed(title="📘 Página 1", description="Esta es la primera página del menú.", color=discord.Color.blue())
    embed1.add_field(name="Dato A", value="Contenido de prueba A", inline=False)
    embed1.add_field(name="Dato B", value="Contenido de prueba B", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📙 Página 2", description="Aquí tienes la segunda página.", color=discord.Color.orange())
    embed2.add_field(name="Info útil", value="Texto aleatorio de relleno", inline=False)
    embed2.set_footer(text="Continúa navegando para ver más")
    embeds.append(embed2)

    embed3 = discord.Embed(title="📗 Página 3", description="Última página del menú.", color=discord.Color.green())
    embed3.add_field(name="Resumen", value="Gracias por revisar este menú paginado.", inline=False)
    embed3.set_image(url="https://via.placeholder.com/300x100.png?text=Imagen+de+ejemplo")
    embeds.append(embed3)

    return embeds

class MenuView(discord.ui.View):
    def __init__(self, author, embeds, timeout=60):
        super().__init__(timeout=timeout)
        self.author = author
        self.embeds = embeds
        self.page = 0
        self.message = None

    async def update_message(self):
        await self.message.edit(embed=self.embeds[self.page], view=self)

    def not_author(self, interaction):
        return interaction.user != self.author

    @discord.ui.button(label="⏮️", style=discord.ButtonStyle.secondary)
    async def first(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.not_author(interaction):
            return await interaction.response.send_message("❌ Solo el autor puede usar los botones.", ephemeral=True)
        self.page = 0
        await interaction.response.defer()
        await self.update_message()

    @discord.ui.button(label="⬅️", style=discord.ButtonStyle.primary)
    async def previous(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.not_author(interaction):
            return await interaction.response.send_message("❌ Solo el autor puede usar los botones.", ephemeral=True)
        self.page = max(0, self.page - 1)
        await interaction.response.defer()
        await self.update_message()

    @discord.ui.button(label="➡️", style=discord.ButtonStyle.primary)
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.not_author(interaction):
            return await interaction.response.send_message("❌ Solo el autor puede usar los botones.", ephemeral=True)
        self.page = min(len(self.embeds) - 1, self.page + 1)
        await interaction.response.defer()
        await self.update_message()

    @discord.ui.button(label="⏭️", style=discord.ButtonStyle.secondary)
    async def last(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.not_author(interaction):
            return await interaction.response.send_message("❌ Solo el autor puede usar los botones.", ephemeral=True)
        self.page = len(self.embeds) - 1
        await interaction.response.defer()
        await self.update_message()

# Registro del comando slash
@bot.tree.command(name="menu", description="Muestra un menú con embeds y botones de navegación.")
async def menu(interaction: discord.Interaction):
    embeds = get_embeds()
    view = MenuView(interaction.user, embeds)
    message = await interaction.response.send_message(embed=embeds[0], view=view, ephemeral=False)
    # interaction.response.send_message devuelve None, no el mensaje, así que necesitamos obtener el mensaje
    # Por eso, usamos followup
    # Esperamos para poder obtener el mensaje
    sent_message = await interaction.original_response()
    view.message = sent_message

@bot.event
async def on_ready():
    print(f"Bot listo. Conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Comandos slash sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Error sincronizando comandos slash: {e}")

# //////////////////////////////////////////

@bot.command()
async def menu(ctx):
    """Muestra un menú con embeds y botones de navegación."""
    embeds = get_embeds()
    view = MenuView(ctx.author, embeds)
    message = await ctx.send(embed=embeds[0], view=view)
    view.message = message
    
# ////////////////////////////////////////////

@bot.command()
async def imagen(ctx):
    embed = discord.Embed(
        title="Imagen grande",
        description="Aquí tienes una imagen grande incrustada.",
        color=discord.Color.blue()
    )

    # Imagen principal grande
    embed.set_image(url="https://fondosmil.co/fondo/17031.jpg")

    # (Opcional) miniatura pequeña
    # embed.set_thumbnail(url="https://example.com/miniatura.jpg")

    await ctx.send(embed=embed)

bot.run("MTM3OTg5MDYyMjQ1Nzk3NDc5NA.G6HXNR.ig6eSs1pb0nKKCaxDoAN46UES8-xrIhF-MxNNA")
