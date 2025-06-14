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


# ////////////////////////////////////////////////////////////////////////

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print(f"El bot está conectado como {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Comandos slash sincronizados: {len(synced)}")
    except Exception as NombreDelError:
        print(f"Error al sincronizar comandos: {NombreDelError}")


# ////////////////////////////////////////////////////////////////////////
# /////////////////////                            ///////////////////////
# /////////////////////       FUNCIONES DE         ///////////////////////
# /////////////////////     EMBEDS (MENSAJES)      ///////////////////////
# /////////////////////                            ///////////////////////
# ////////////////////////////////////////////////////////////////////////


def get_ciclos_cursos_embeds():
    lista_ciclos = []

    embed0 = discord.Embed(
        title="Primer ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed0.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed0.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed0)


    embed1 = discord.Embed(
        title="Segundo ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed1.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed1.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed1)

    embed2 = discord.Embed(
        title="Tercer ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed2.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed2.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed2)


    embed3 = discord.Embed(
        title="Cuarto ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed3.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed3.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed3)

    embed4 = discord.Embed(
        title="Quinto ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed4.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed4.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed4)

    embed5 = discord.Embed(
        title="Sexto ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed5.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed5.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed5)
    
    embed6 = discord.Embed(
        title="Séptimo ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed6.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed6.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed6)

    embed7 = discord.Embed(
        title="Octavo ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed7.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed7.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed7)

    embed8 = discord.Embed(
        title="Noveno ciclo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed8.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed8.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed8)

    embed9 = discord.Embed(
        title="Cursos electivos",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el curso.\n
            - **BFI01** - Física 1
            - **BMA01** - Cálculo diferencial
            - **BMA03** - Álgebra lineal
            - **EE250** - Dibujo técnico
            - **BIC01** - Introducción a la computación
            - **BRN01** - Realidad Nac. Constitución y DD.HH
            - **CBS01** - Fundamentos de programación
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed9.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed9.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed9)

    return lista_ciclos


def get_primer_ciclo_embeds():
    embeds = []

    embed1 = discord.Embed(title="📗 Física 1", description="", color=discord.Color.dark_green())
    embed1.add_field(name="▸  Laboratorios", value="Laboratorios de distintos ciclos.", inline=False)
    embed1.add_field(name="▸  Prácticas", value="Prácticas y exámenes desde el ciclo 2017-1.", inline=False)
    embed1.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📙 Cálculo diferencial", description="", color=discord.Color.orange())
    embed2.add_field(name="▸  Prácticas", value="Prácticas y exámenes desde el ciclo 2017-1.", inline=False)
    embed2.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📗 Álgebra lineal", description="", color=discord.Color.green())
    embed3.add_field(name="▸  Prácticas", value="Prácticas y exámenes desde el ciclo 2017-1.", inline=False)
    embed3.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📙 Dibujo técnico", description="", color=discord.Color.green())
    embed4.add_field(name="▸  Prácticas", value="Prácticas y exámenes desde el ciclo 2017-1.", inline=False)
    embed4.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📗 Introducción a la computación", description="", color=discord.Color.green())
    embed5.add_field(name="▸  Prácticas", value="Prácticas y exámenes desde el ciclo 2017-1.", inline=False)
    embed5.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📙 Realidad Nac. Constitución y DD.HH", description="", color=discord.Color.green())
    embed6.add_field(name="▸  Prácticas", value="Prácticas y exámenes desde el ciclo 2017-1.", inline=False)
    embed6.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📗 Fundamentos de programación", description="", color=discord.Color.green())
    embed7.add_field(name="▸  Prácticas", value="Prácticas y exámenes desde el ciclo 2017-1.", inline=False)
    embed7.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds


def get_ayuda_embed():

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

    return embed


def get_ciclos_embeds():

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
    
    return embed


# ////////////////////////////////////////////////////////////////////////
# /////////////////////                            ///////////////////////
# /////////////////////       FUNCIONES DE         ///////////////////////
# /////////////////////    LISTAS DESPLEGABLES     ///////////////////////
# /////////////////////                            ///////////////////////
# ////////////////////////////////////////////////////////////////////////

def despliegue_lista_ciclos():

    opciones = []

    opciones.append(discord.SelectOption(label="1er ciclo", value=1))
    opciones.append(discord.SelectOption(label="2do ciclo", value=2))
    opciones.append(discord.SelectOption(label="3er ciclo", value=3))
    opciones.append(discord.SelectOption(label="4to ciclo", value=4))
    opciones.append(discord.SelectOption(label="5to ciclo", value=5))
    opciones.append(discord.SelectOption(label="6to ciclo", value=6))
    opciones.append(discord.SelectOption(label="7mo ciclo", value=7))
    opciones.append(discord.SelectOption(label="8vo ciclo", value=8))
    opciones.append(discord.SelectOption(label="9no ciclo", value=9))
    opciones.append(discord.SelectOption(label="Electivos", value=10))

    return opciones


def despliegue_lista_cursos():

    lista_cursos = []

    opciones0 = [
        discord.SelectOption(label="Física 1", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones0)

    opciones1 = [
        discord.SelectOption(label="Fundamentos de Ing. térmica y de fluidos", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones1)

    opciones2 = [
        discord.SelectOption(label="Fundamentos de Electricidad y Magnetismo", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones2)

    opciones3 = [
        discord.SelectOption(label="Introducción a la física moderna", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones3)

    opciones4 = [
        discord.SelectOption(label="Insertar opciones de quinto ciclo", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones4)

    opciones5 = [
        discord.SelectOption(label="Insertar opciones de sexto ciclo", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones5)

    opciones6 = [
        discord.SelectOption(label="Insertar opciones de séptimo ciclo", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones6)

    opciones7 = [
        discord.SelectOption(label="Insertar opciones de octavo ciclo", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones7)

    opciones8 = [
        discord.SelectOption(label="Insertar opciones de noveno ciclo", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones8)

    opciones9 = [
        discord.SelectOption(label="Insertar opciones de cursos electivos", value=1),
        discord.SelectOption(label="Cálculo diferencial", value=2),
        discord.SelectOption(label="Álgebra lineal", value=3),
        discord.SelectOption(label="Dibujo técnico", value=4),
        discord.SelectOption(label="Introducción a la computación", value=5),
        discord.SelectOption(label="Realidad Nac. Constitución y DD.HH", value=6),
        discord.SelectOption(label="Fundamentos de programación", value=7),
    ]
    lista_cursos.append(opciones9)

    return lista_cursos

# ///////////////////////////////////////////////////////////////////////////////////////////

async def mostrar_help(ctx_or_interaction):

    embed = get_ayuda_embed()

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(embed=embed) # Responde al comando de texto con el embed
    else:
        await ctx_or_interaction.response.send_message(embed=embed, ephemeral=False)  # Responde al comando slash con el embed


async def menu_main(ctx_or_interaction):

    view = NumeroMenuCiclo()  # Crea una instancia de la clase NumeroMenuCiclo

    embed = get_ciclos_embeds()

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(view=view, embed=embed) # Responde al comando de texto con el embed
    else:
        await ctx_or_interaction.response.send_message(view=view, embed=embed, ephemeral=False)  # Responde al comando slash con el embed


@bot.command(name="help")
async def help_text(ctx):
    await mostrar_help(ctx)

@bot.tree.command(name="help", description="Muestra la lista de comandos disponibles.")
async def help_slash(interaction: discord.Interaction):
    await mostrar_help(interaction)

@bot.command(name="menu")
async def help_text(ctx):
    await menu_main(ctx)

@bot.tree.command(name="menu", description="Muestra el menú principal de FIEE-BOT.")
async def help_slash(interaction: discord.Interaction):
    await menu_main(interaction)


# //////////////////////////////////////////////////////////////////////////////////////////////


class NumeroMenuCiclo(discord.ui.View):

    opciones = despliegue_lista_ciclos()

    @discord.ui.select(
        placeholder="Selecciona un ciclo.",
        min_values=1,
        max_values=1,
        options=opciones,
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):

        view1 = NumeroMenuPrimerCiclo(int(select.values[0]))  # Crea una instancia de la vista con el número seleccionado
        embeds = get_ciclos_cursos_embeds()
        await interaction.response.edit_message(view=view1, embed=embeds[int(select.values[0])-1])  # Edita el mensaje original con la información del ciclo seleccionado


class NumeroMenuPrimerCiclo(discord.ui.View):

    ciclo_seleccionado = 0 

    def __init__(self, ciclo_seleccionado):
        super().__init__()
        NumeroMenuPrimerCiclo.ciclo_seleccionado = ciclo_seleccionado-1  # Guarda el número del ciclo seleccionado

    despliegue_lista_cursos = despliegue_lista_cursos()

    @discord.ui.select(
        placeholder="Selecciona un curso.",
        min_values=1,
        max_values=1,
        options=despliegue_lista_cursos[ciclo_seleccionado],  # Usa la lista de opciones definida arriba
    )
    async def select_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        curso_elegido_num = int(select.values[0])-1  # Obtiene el índice del curso seleccionado
        embed = get_primer_ciclo_embeds()
        embed[curso_elegido_num].set_footer(text="Gracias por usar FIEE-BOT.")
        embed[curso_elegido_num].set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
        await interaction.response.edit_message(embed=embed[curso_elegido_num], view=None)  # Edita el mensaje original con la información del curso seleccionado


# ///////////////////////////////////////////////////////////////////////////////////////////

bot.run("MTM3OTg5MDYyMjQ1Nzk3NDc5NA.G6HXNR.ig6eSs1pb0nKKCaxDoAN46UES8-xrIhF-MxNNA")
