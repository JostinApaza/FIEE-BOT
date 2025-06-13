import discord # Importa el módulo principal "discord" de la librería discord.py
from discord.ext import commands # Importa el submódulo "commands" desde el submódulo de extensiones discord.ext, que facilita crear comandos para el bot
from discord import app_commands # Importa el submódulo "app_commands" para manejar comandos slash
import textwrap

intents = discord.Intents.default() # Crea un objeto de la clase discord.Intents con la configuración por defecto

intents.message_content = True    # Leer mensajes (necesario para reconocer comandos de texto)
intents.members = False           # Ver miembros del servidor
intents.presences = False         # Ver estados de usuarios (online, offline)
intents.guilds = False            # Ver información del servidor


prefix = "!"  # Define el prefijo que se usará para los comandos del bot

bot = commands.Bot(command_prefix = prefix, intents=intents, help_command=None) # Define el prefijo de los comandos y las "intenciones" (permisos internos) del bot


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f"El bot está conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Comandos slash sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Error al sincronizar comandos: {e}")


async def mostrar_help(ctx_or_interaction):

    embed = discord.Embed(
        title="Lista de comandos de FIEE-BOT.",
        description=textwrap.dedent(f"""\
            El prefix configurado para este servidor es `{prefix}`.\n
            Aquí tienes una lista de los comandos disponibles:
            - {prefix}help: Muestra este mensaje de ayuda.
            - {prefix}menu: Muestra el menú de navegación principal, de todo el material disponible.
            - {prefix}creditos: Muestra los créditos y agradecimientos de FIEE-BOT.
            - {prefix}aportar: Muestra información de contacto para aportar material académico al proyecto.
            - {prefix}setprefix: Cambia el prefijo del bot en este servidor (requiere permisos de administrador).
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed.add_field(name="Versión", value="1.0", inline=False)
    embed.add_field(name="Autores", value="-", inline=False)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(embed=embed) # Responde al comando de texto con el embed
    else:
        await ctx_or_interaction.response.send_message(embed=embed, ephemeral=False)  # Responde al comando slash con el embed



async def menu_main(ctx_or_interaction):

    embed = discord.Embed(
        title="Repositorio de FIEE-BOT.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el ciclo.\n
            - **Primer ciclo**
            - **Segundo ciclo**
            - **Tercer ciclo**
            - **Cuarto ciclo**
            - **Quinto ciclo**
            - **Sexto ciclo**
            - **Séptimo ciclo**
            - **Octavo ciclo**
            - **Noveno ciclo**
            - **Electivos**
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    
    view = NumeroMenu()  # Crea una instancia de la clase NumeroMenu

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(view=view, embed=embed) # Responde al comando de texto con el embed
    else:
        await ctx_or_interaction.response.send_message(view=view, embed=embed, ephemeral=False)  # Responde al comando slash con el embed


# Comando de texto para mostrar ayuda
@bot.command(name="help")
async def help_text(ctx):
    await mostrar_help(ctx)

# Comando slash para mostrar ayuda
@bot.tree.command(name="help", description="Muestra la lista de comandos disponibles.")
async def help_slash(interaction: discord.Interaction):
    await mostrar_help(interaction)


# Comando de texto para mostrar el menú principal

# Comando de texto para mostrar menú
@bot.command(name="menu3")
async def help_text(ctx):
    await menu_main(ctx)

# Comando slash para mostrar menú
@bot.tree.command(name="menu3", description="Muestra el menú principal de FIEE-BOT.")
async def help_slash(interaction: discord.Interaction):
    await menu_main(interaction)









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


class NumeroMenu(discord.ui.View):

    opciones = [discord.SelectOption(label=str(i), description=f"Opción número {i}") for i in range(1, 10)]
    opciones.append(discord.SelectOption(label="Electivos", description="Opción para los cursos electivos"))

    @discord.ui.select(
        placeholder="Selecciona un ciclo.",
        min_values=1,
        max_values=1,
        options=opciones,
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        numero_elegido = select.values[0]
        await interaction.response.send_message(f"Elegiste el ciclo {numero_elegido}", ephemeral=True)



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



# ////////////////////////////////////////////



@bot.command()
async def menu(ctx):
    # Muestra un menú con embeds y botones de navegación
    embeds = get_embeds()
    view = MenuView(ctx.author, embeds)
    message = await ctx.send(embed=embeds[0], view=view)
    view.message = message
    
    

@bot.command()
async def menu2(ctx):
    
    view = NumeroMenu()
    await ctx.send("Selecciona un número del menú desplegable:", view=view)




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
