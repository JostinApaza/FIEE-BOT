import discord # Importa el módulo principal "discord" de la librería discord.py
from discord.ext import commands # Importa el submódulo "commands" desde el submódulo de extensiones discord.ext, que facilita crear comandos para el bot
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
            - **BFI05** - Fund. de Ing. térmica y de fluidos
            - **BMA02** - Cálculo integral
            - **BMA09** - Algoritmos y estructuras de datos I
            - **BQU01** - Química I
            - **EE152** - Fund. de ingeniería del computador
            - **BRC01** - Redacción y comunicación
            - **CBN01** - Redes de datos I
            - **CBS02** - Sistemas operativos I
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
            - **BFI03** - Fundamentos de electricidad y magnetismo
            - **BMA05** - Ecuaciones diferenciales
            - **BMA10** - Probabilidades y estadística
            - **BMA15** - Programación orientada a objetos
            - **BEG01** - Economía general
            - **CBN02** - Redes de datos II
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
            - **BFI06** - Introducción a la física moderna
            - **EE410** - Análisis de señales y sistemas
            - **BMA07** - Cálculo vectorial
            - **BMA18** - Métodos numéricos
            - **EE320** - Circuitos eléctricos I
            - **EE306** - Electrotecnia e instalación de redes
            - **BEF01** - Ética y filosofía política
            - **CBS03** - Sistemas operativos II
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
            - **BFM16** - Mecánica de fluidos y termodinámica
            - **BMA22** - Procesos estocásticos
            - **EE418** - Dispositivos y circuitos electrónicos I
            - **EE420** - Circuitos eléctricos II
            - **EE428** - Laboratorio de electrónica
            - **EE522** - Electromagnetismo I
            - **EE647** - Sistemas de control I
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
            - **EE430** - Sistemas de comunicaciones I
            - **EE438** - Dispositivos y circuitos electrónicos II
            - **EE458** - Laboratorio de electrónica
            - **EE588** - Electromagnetismo II
            - **EE604** - Microcontroladores
            - **EE648** - Sistemas de control II
            - **CODE1** - blank text
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
            - **EE467** - Protocolos de enrutamiento y arquitectura de redes
            - **EE528** - Conversión de energía electromecánica
            - **EE530** - Sistemas de comunicaciones II
            - **EE590** - Fibra óptica
            - **CODE2** - blank
            - **CODE3** - blank
            - **CODE4** - blank
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
            - **BEG06** - Formulación y evaluación de proyectos
            - **EE498** - Laboratorio de radiocomunicaciones
            - **EE592** - Microondas
            - **CODE5** - blank
            - **CODE6** - blank
            - **CODE7** - blank
            - **CODE8** - blank
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
            - **EE708** - Sistemas de conmutación
            - **CODE9** - Gestión y seguridad de redes
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
            - 
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed9.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed9.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional
    lista_ciclos.append(embed9)

    return lista_ciclos

# ////////////////////////////////////////////////////////////////////////

def get_primer_ciclo_embeds():
    embeds = []

    embed1 = discord.Embed(title="📗 Física 1", description="", color=discord.Color.dark_green())
    embed1.add_field(name="▸  Laboratorios", value="Laboratorios de distintos ciclos.", inline=False)
    embed1.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed1.add_field(name="▸  Prácticas", value="Prácticas y exámenes del curso.", inline=False)
    embed1.add_field(name="▸  Cuadernos", value="Cuadernos y libros del curso.", inline=False)
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


def get_segundo_ciclo_embeds():
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

def get_tercer_ciclo_embeds():
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

def get_cuarto_ciclo_embeds():
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


def get_quinto_ciclo_embeds():
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

def get_sexto_ciclo_embeds():
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

def get_septimo_ciclo_embeds():
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


def get_octavo_ciclo_embeds():
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


def get_noveno_ciclo_embeds():
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


def get_cursos_electivos_embeds():
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

# /////////////////////////////////////////////////////////////////////////////////////

def get_fisica_1_laboratorios_embed():

    embed = discord.Embed(
        title="Laboratorios de Física 1",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el periodo.\n
            - Laboratorios 2019-II
            - Laboratorios 2020-II
            - Laboratorios 2021-II
            - Laboratorios 2023-I
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fisica_1_clases_embed():

    embed = discord.Embed(
        title="Clases de Física 1",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Clases PDF's - Prof. Caro
            - Clases PDF's 2020-I-II - Prof. Huallpa
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fisica_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de Física 1",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fisica_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Física 1",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed



# /////////////////////////////////////////////////////////////////////////////////////

def get_calc_diferencial_clases_embed():

    embed = discord.Embed(
        title="Clases de calc. diferencial.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_calc_diferencial_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de cálculo diferencial:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_calc_diferencial_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de cálculo diferencial",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_algebra_lineal_clases_embed():

    embed = discord.Embed(
        title="Clases de álgebra_lineal.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_algebra_lineal_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de algebra_lineal:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_algebra_lineal_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de algebra_lineal:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_dibujo_tecnico_clases_embed():

    embed = discord.Embed(
        title="Clases de dibujo_tecnico.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_dibujo_tecnico_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de dibujo_tecnico:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_dibujo_tecnico_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de dibujo_tecnico:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_intro_computacion_clases_embed():

    embed = discord.Embed(
        title="Clases de intro_computacion.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_intro_computacion_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de intro_computacion:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_intro_computacion_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de intro_computacion:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_realidad_nacional_clases_embed():

    embed = discord.Embed(
        title="Clases de realidad_nacional.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_realidad_nacional_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de realidad_nacional:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_realidad_nacional_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de realidad_nacional:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_fundamentos_programacion_clases_embed():

    embed = discord.Embed(
        title="Clases de fundamentos_programacion.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_programacion_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de fundamentos_programacion:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_programacion_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de fundamentos_programacion:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_fisica_2_clases_embed():

    embed = discord.Embed(
        title="Clases de fisica_2.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fisica_2_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de fisica_2:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fisica_2_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de fisica_2:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed



# /////////////////////////////////////////////////////////////////////////////////////

def get_calculo_integral_clases_embed():

    embed = discord.Embed(
        title="Clases de calculo_integral.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_calculo_integral_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de calculo_integral:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_calculo_integral_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de calculo_integral:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_algoritmos_1_clases_embed():

    embed = discord.Embed(
        title="Clases de algoritmos_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_algoritmos_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de algoritmos_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_algoritmos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de algoritmos_1:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_quimica_1_clases_embed():

    embed = discord.Embed(
        title="Clases de quimica_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_quimica_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de quimica_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_quimica_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de quimica_1:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_fundamentos_computador_clases_embed():

    embed = discord.Embed(
        title="Clases de fundamentos_computador.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_computador_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de fundamentos_computador:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_computador_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de fundamentos_computador:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_redaccion_clases_embed():

    embed = discord.Embed(
        title="Clases de redaccion.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_redaccion_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de redaccion:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_redaccion_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de redaccion:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_redes_1_clases_embed():

    embed = discord.Embed(
        title="Clases de redes_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_redes_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de redes_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_redes_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de redes_1:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_operativos_1_clases_embed():

    embed = discord.Embed(
        title="Clases de operativos_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_operativos_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de operativos_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_operativos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de operativos_1:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_fundamentos_electricidad_magnetismo_clases_embed():

    embed = discord.Embed(
        title="Clases de fundamentos_electricidad_magnetismo.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_electricidad_magnetismo_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de fundamentos_electricidad_magnetismo:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_electricidad_magnetismo_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de fundamentos_electricidad_magnetismo:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_ecuaciones_diferenciales_clases_embed():

    embed = discord.Embed(
        title="Clases de ecuaciones_diferenciales.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_ecuaciones_diferenciales_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de ecuaciones_diferenciales:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_ecuaciones_diferenciales_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de ecuaciones_diferenciales:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_poo_clases_embed():

    embed = discord.Embed(
        title="Clases de poo.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_poo_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de poo:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_poo_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de poo:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_economia_clases_embed():

    embed = discord.Embed(
        title="Clases de economia.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_economia_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de economia:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_economia_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de economia:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_probabilidades_clases_embed():

    embed = discord.Embed(
        title="Clases de probabilidades.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_probabilidades_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de probabilidades:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_probabilidades_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de probabilidades:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_redes_2_clases_embed():

    embed = discord.Embed(
        title="Clases de redes_2.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_redes_2_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de redes_2:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_redes_2_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de redes_2:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_intro_moderna_clases_embed():

    embed = discord.Embed(
        title="Clases de intro_moderna.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_intro_moderna_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de intro_moderna:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_intro_moderna_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de intro_moderna:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_circuitos_1_clases_embed():

    embed = discord.Embed(
        title="Clases de circuitos_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_circuitos_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de circuitos_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_circuitos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de circuitos_1:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_calc_vectorial_clases_embed():

    embed = discord.Embed(
        title="Clases de calc_vectorial.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_calc_vectorial_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de calc_vectorial:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_calc_vectorial_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de calc_vectorial:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_analisis_senales_clases_embed():

    embed = discord.Embed(
        title="Clases de analisis_senales.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_analisis_senales_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de analisis_senales:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_analisis_senales_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de analisis_senales:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_operativos_2_clases_embed():

    embed = discord.Embed(
        title="Clases de operativos_2.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_operativos_2_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de operativos_2:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_operativos_2_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de operativos_2:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_electrotecnia_clases_embed():

    embed = discord.Embed(
        title="Clases de electrotecnia.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_electrotecnia_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de electrotecnia:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_electrotecnia_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de electrotecnia:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_metodos_numericos_clases_embed():

    embed = discord.Embed(
        title="Clases de metodos_numericos.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_metodos_numericos_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de metodos_numericos:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_metodos_numericos_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de metodos_numericos:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_etica_filosofia_clases_embed():

    embed = discord.Embed(
        title="Clases de etica_filosofia.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_etica_filosofia_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de etica_filosofia:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_etica_filosofia_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de etica_filosofia:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_procesos_estocasticos_clases_embed():

    embed = discord.Embed(
        title="Clases de procesos_estocasticos.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_procesos_estocasticos_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de procesos_estocasticos:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_procesos_estocasticos_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de procesos_estocasticos:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////

def get_example_clases_embed():

    embed = discord.Embed(
        title="Clases de example.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_example_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de example:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_example_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de example:",
        description=textwrap.dedent(f"""\
            \n
            - Prueba
            -
            -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


# /////////////////////////////////////////////////////////////////////////////////////


def opciones_fisica_1_embeds():

    embeds = []

    embeds.append(get_fisica_1_laboratorios_embed())  # [0]
    embeds.append(get_fisica_1_clases_embed())        # [1]
    embeds.append(get_fisica_1_examenes_embed())      # [2]
    embeds.append(get_fisica_1_cuadernos_embed())     # [3]

    return embeds

def opciones_calc_diferencial_embeds():

    embeds = []

    embeds.append("get_calc_diferencial_laboratorios_embed()")  # [0]
    embeds.append(get_calc_diferencial_clases_embed())  # [1]
    embeds.append(get_calc_diferencial_examenes_embed())  # [2]
    embeds.append(get_calc_diferencial_cuadernos_embed())  # [3]

    return embeds

def opciones_algebra_lineal_embeds():
    embeds = []

    embeds.append("get_algebra_lineal_laboratorios_embed()")  # [0]
    embeds.append(get_algebra_lineal_clases_embed())        # [1]
    embeds.append(get_algebra_lineal_examenes_embed())      # [2]
    embeds.append(get_algebra_lineal_cuadernos_embed())     # [3]

    return embeds

def opciones_dibujo_tecnico_embeds():
    embeds = []

    embeds.append("get_dibujo_tecnico_laboratorios_embed()")  # [0]
    embeds.append(get_dibujo_tecnico_clases_embed())        # [1]
    embeds.append(get_dibujo_tecnico_examenes_embed())      # [2]
    embeds.append(get_dibujo_tecnico_cuadernos_embed())     # [3]

    return embeds

def opciones_intro_computacion_embeds():
    embeds = []

    embeds.append("get_intro_computacion_laboratorios_embed()")  # [0]
    embeds.append(get_intro_computacion_clases_embed())        # [1]
    embeds.append(get_intro_computacion_examenes_embed())      # [2]
    embeds.append(get_intro_computacion_cuadernos_embed())     # [3]

    return embeds

def opciones_realidad_nacional_embeds():
    embeds = []

    embeds.append("get_realidad_nacional_laboratorios_embed()")  # [0]
    embeds.append(get_realidad_nacional_clases_embed())        # [1]
    embeds.append(get_realidad_nacional_examenes_embed())      # [2]
    embeds.append(get_realidad_nacional_cuadernos_embed())     # [3]

    return embeds

def opciones_fundamentos_programacion_embeds():
    embeds = []

    embeds.append("get_fundamentos_programacion_laboratorios_embed()")  # [0]
    embeds.append(get_fundamentos_programacion_clases_embed())        # [1]
    embeds.append(get_fundamentos_programacion_examenes_embed())      # [2]
    embeds.append(get_fundamentos_programacion_cuadernos_embed())     # [3]

    return embeds

# /////////////////////////////////////////////////////////////////////////////////////


def opciones_fisica_2_embeds():
    embeds = []

    embeds.append("get_fisica_2_laboratorios_embed()")  # [0]
    embeds.append(get_fisica_2_clases_embed())        # [1]
    embeds.append(get_fisica_2_examenes_embed())      # [2]
    embeds.append(get_fisica_2_cuadernos_embed())     # [3]

    return embeds

def opciones_calculo_integral_embeds():
    embeds = []

    embeds.append("get_calculo_integral_laboratorios_embed()")  # [0]
    embeds.append(get_calculo_integral_clases_embed())        # [1]
    embeds.append(get_calculo_integral_examenes_embed())      # [2]
    embeds.append(get_calculo_integral_cuadernos_embed())     # [3]

    return embeds

def opciones_algoritmos_1_embeds():
    embeds = []

    embeds.append("get_algoritmos_1_laboratorios_embed()")  # [0]
    embeds.append(get_algoritmos_1_clases_embed())        # [1]
    embeds.append(get_algoritmos_1_examenes_embed())      # [2]
    embeds.append(get_algoritmos_1_cuadernos_embed())     # [3]

    return embeds

def opciones_fundamentos_computador_embeds():
    embeds = []

    embeds.append("get_fundamentos_computador_laboratorios_embed()")  # [0]
    embeds.append(get_fundamentos_computador_clases_embed())        # [1]
    embeds.append(get_fundamentos_computador_examenes_embed())      # [2]
    embeds.append(get_fundamentos_computador_cuadernos_embed())     # [3]

    return embeds

def opciones_quimica_1_embeds():
    embeds = []

    embeds.append("get_quimica_1_laboratorios_embed()")  # [0]
    embeds.append(get_quimica_1_clases_embed())        # [1]
    embeds.append(get_quimica_1_examenes_embed())      # [2]
    embeds.append(get_quimica_1_cuadernos_embed())     # [3]

    return embeds

def opciones_redes_1_embeds():
    embeds = []

    embeds.append("get_redes_1_laboratorios_embed()")  # [0]
    embeds.append(get_redes_1_clases_embed())        # [1]
    embeds.append(get_redes_1_examenes_embed())      # [2]
    embeds.append(get_redes_1_cuadernos_embed())     # [3]

    return embeds

def opciones_redaccion_embeds():
    embeds = []

    embeds.append("get_redaccion_laboratorios_embed()")  # [0]
    embeds.append(get_redaccion_clases_embed())        # [1]
    embeds.append(get_redaccion_examenes_embed())      # [2]
    embeds.append(get_redaccion_cuadernos_embed())     # [3]

    return embeds

# /////////////////////////////////////////////////////////////////////////////////////


def opciones_fundamentos_electricidad_magnetismo_embeds():
    embeds = []

    embeds.append("get_fundamentos_electricidad_magnetismo_laboratorios_embed()")  # [0]
    embeds.append(get_fundamentos_electricidad_magnetismo_clases_embed())        # [1]
    embeds.append(get_fundamentos_electricidad_magnetismo_examenes_embed())      # [2]
    embeds.append(get_fundamentos_electricidad_magnetismo_cuadernos_embed())     # [3]

    return embeds

# /////////////////////////////////////////////////////////////////////////////////////


def get_opciones_primer_ciclo_embeds():

    embeds = []

    embeds.append(opciones_fisica_1_embeds())  # [0]
    embeds.append(opciones_calc_diferencial_embeds())  # [1]
    embeds.append(opciones_algebra_lineal_embeds())  # [2]
    embeds.append(opciones_dibujo_tecnico_embeds())  # [3]
    embeds.append(opciones_intro_computacion_embeds())  # [4]
    embeds.append(opciones_realidad_nacional_embeds())  # [5]
    embeds.append(opciones_fundamentos_programacion_embeds())  # [6]

    return embeds


def get_opciones_segundo_ciclo_embeds():
    embeds = []

    embeds.append(opciones_fisica_2_embeds())  # [0]
    embeds.append(opciones_calculo_integral_embeds())  # [1]
    embeds.append(opciones_algoritmos_1_embeds())  # [2]
    embeds.append(opciones_fundamentos_computador_embeds())  # [3]
    embeds.append(opciones_quimica_1_embeds())  # [4]
    embeds.append(opciones_redes_1_embeds())  # [5]
    embeds.append(opciones_redaccion_embeds())  # [6]

    return embeds


def get_opciones_todos_los_ciclos_embeds():

    embeds = []

    embeds.append(get_opciones_primer_ciclo_embeds())  # [0]
    embeds.append(get_opciones_segundo_ciclo_embeds())  # [1]

    return embeds




# /////////////////////////////////////////////////////////////////////////////////////


def get_lista_cursos_suprema_embeds():

    lista_de_listas = []

    lista_de_listas.append(get_primer_ciclo_embeds()) # [0]
    lista_de_listas.append(get_segundo_ciclo_embeds())
    lista_de_listas.append(get_tercer_ciclo_embeds())
    lista_de_listas.append(get_cuarto_ciclo_embeds())
    lista_de_listas.append(get_quinto_ciclo_embeds())
    lista_de_listas.append(get_sexto_ciclo_embeds())
    lista_de_listas.append(get_septimo_ciclo_embeds())
    lista_de_listas.append(get_octavo_ciclo_embeds())
    lista_de_listas.append(get_noveno_ciclo_embeds())
    lista_de_listas.append(get_cursos_electivos_embeds()) # [9]
    
    return lista_de_listas



# ///////////////////////////////////////////////////////////////////////////////////

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

def despliegue_lista_opciones_LAB():

    opciones = []

    opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=7))

    return opciones

def despliegue_lista_opciones_LAB_NO_CUADERNO():

    opciones = []

    opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=7))

    return opciones

def despliegue_lista_opciones_NO_LAB():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=7))

    return opciones

def despliegue_lista_opciones_NO_LAB_NO_PC():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    # opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=7))

    return opciones

def despliegue_lista_opciones_NO_LAB_NO_PC_NO_CUADERNO():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    # opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=7))

def despliegue_lista_opciones_NO_LAB_NO_PC_NO_CLASE():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    # opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    # opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=7))

    return opciones
def despliegue_lista_opciones_NO_LAB_NO_CUADERNO():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=7))

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
        discord.SelectOption(label="Asesorías 1er ciclo", value=8),
    ]
    lista_cursos.append(opciones0)

    opciones1 = [
        discord.SelectOption(label="Fundamentos de Ing. térmica y de fluidos", value=1),
        discord.SelectOption(label="Cálculo integral", value=2),
        discord.SelectOption(label="Química", value=3),
        discord.SelectOption(label="Algoritmos y estructuras de datos I", value=4),
        discord.SelectOption(label="Fund. de ingeniería del computador", value=5),
        discord.SelectOption(label="Redacción y comunicación", value=6),
        discord.SelectOption(label="Redes de datos I", value=7),
        discord.SelectOption(label="Sistemas operativos I", value=8),
    ]
    lista_cursos.append(opciones1)

    opciones2 = [
        discord.SelectOption(label="Fundamentos de Electricidad y Magnetismo", value=1),
        discord.SelectOption(label="Ecuaciones diferenciales", value=2),
        discord.SelectOption(label="Probabilidades y estadística", value=3),
        discord.SelectOption(label="Programación orientada a objetos", value=4),
        discord.SelectOption(label="Economía general", value=5),
        discord.SelectOption(label="Redes de datos II", value=6),
    ]
    lista_cursos.append(opciones2)

    opciones3 = [
        discord.SelectOption(label="Introducción a la física moderna", value=1),
        discord.SelectOption(label="Análisis de señales y sistemas", value=2),
        discord.SelectOption(label="Cálculo vectorial", value=3),
        discord.SelectOption(label="Métodos numéricos", value=4),
        discord.SelectOption(label="Circuitos eléctricos I", value=5),
        discord.SelectOption(label="Electrotecnia e instalación de redes", value=6),
        discord.SelectOption(label="Ética y filosofía", value=7),
        discord.SelectOption(label="Sistemas operativos II", value=8),
    ]
    lista_cursos.append(opciones3)

    opciones4 = [
        discord.SelectOption(label="Mecánica de fluidos y termodinámica", value=1),
        discord.SelectOption(label="Procesos estocásticos", value=2),
        discord.SelectOption(label="Dispositivos y circuitos electrónicos I", value=3),
        discord.SelectOption(label="Circuitos eléctricos II", value=4),
        discord.SelectOption(label="Laboratorio de electrónica I", value=5),
        discord.SelectOption(label="Electromagnetismo I", value=6),
        discord.SelectOption(label="Sistemas de control I", value=7),
    ]
    lista_cursos.append(opciones4)

    opciones5 = [
        discord.SelectOption(label="Sistemas de comunicaciones I", value=1),
        discord.SelectOption(label="Dispositivos y circuitos electrónicos II", value=2),
        discord.SelectOption(label="Laboratorio de electrónica II", value=3),
        discord.SelectOption(label="Electromagnetismo II", value=4),
        discord.SelectOption(label="Microcontroladores", value=5),
        discord.SelectOption(label="Sistemas de control II", value=6),
        discord.SelectOption(label="-", value=7),
    ]
    lista_cursos.append(opciones5)

    opciones6 = [
        discord.SelectOption(label="Protocolos", value=1),
        discord.SelectOption(label="Conversión de energía electromecánica", value=2),
        discord.SelectOption(label="Sistemas de comunicaciones II", value=3),
        discord.SelectOption(label="Fibra óptica", value=4),
        discord.SelectOption(label="-", value=5),
        discord.SelectOption(label="-", value=6),
        discord.SelectOption(label="-", value=7),
    ]
    lista_cursos.append(opciones6)

    opciones7 = [
        discord.SelectOption(label="Formulación y evaluación de proyectos", value=1),
        discord.SelectOption(label="Laboratorio de radiocomunicaciones", value=2),
        discord.SelectOption(label="Microondas", value=3),
        discord.SelectOption(label="-", value=4),
        discord.SelectOption(label="-", value=5),
        discord.SelectOption(label="-", value=6),
        discord.SelectOption(label="-", value=7),
    ]
    lista_cursos.append(opciones7)

    opciones8 = [
        discord.SelectOption(label="Sistemas de conmutación", value=1),
        discord.SelectOption(label="Gestión y seguridad de redes", value=2),
        discord.SelectOption(label="-", value=3),
        discord.SelectOption(label="-", value=4),
        discord.SelectOption(label="-", value=5),
        discord.SelectOption(label="-", value=6),
        discord.SelectOption(label="-", value=7),
    ]
    lista_cursos.append(opciones8)

    opciones9 = [
        discord.SelectOption(label="Algoritmos y estructuras de datos II", value=1),
        discord.SelectOption(label="Ingeniería de software", value=2),
        discord.SelectOption(label="Aprendizaje de máquina y minería de datos", value=3),
        discord.SelectOption(label="Introducción a la ingeniería biomédica", value=4),
        discord.SelectOption(label="Electrónica de radiocomunicaciones", value=5),
        discord.SelectOption(label="Redes inalámbricas y móviles", value=6),
        discord.SelectOption(label="Sistema de radiocomunicaciones", value=7),
        discord.SelectOption(label="Antenas", value=8),
        discord.SelectOption(label="Redes de automatización", value=9),
        discord.SelectOption(label="Ingeniería de audio y video", value=10),
        discord.SelectOption(label="Inglés profesional", value=11),
        discord.SelectOption(label="-", value=12),
    ]
    lista_cursos.append(opciones9)

    return lista_cursos

# ///////////////////////////////////////////////////////////////////////////////////////////

async def show_help(ctx_or_interaction):

    embed = get_ayuda_embed()

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(embed=embed) # Responde al comando de texto con el embed
    else:
        await ctx_or_interaction.response.send_message(embed=embed, ephemeral=False)  # Responde al comando slash con el embed


async def show_menu(ctx_or_interaction):

    view = NumeroMenuCiclo()

    embed = get_ciclos_embeds()

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(view=view, embed=embed) # Responde al comando de texto con el embed
    else:
        await ctx_or_interaction.response.send_message(view=view, embed=embed, ephemeral=False)  # Responde al comando slash con el embed


# ///////////////////////////////////////////////////////////////////////////////////////////


@bot.command(name="help")
async def help_text(ctx):
    await show_help(ctx)

@bot.tree.command(name="help", description="Muestra la lista de comandos disponibles.")
async def help_slash(interaction: discord.Interaction):
    await show_help(interaction)

@bot.command(name="menu")
async def help_text(ctx):
    await show_menu(ctx)

@bot.tree.command(name="menu", description="Muestra el menú principal de FIEE-BOT.")
async def help_slash(interaction: discord.Interaction):
    await show_menu(interaction)


# //////////////////////////////////////////////////////////////////////////////////////////////


class NumeroMenuCiclo(discord.ui.View):
    def __init__(self):
        super().__init__()

        opciones = despliegue_lista_ciclos()

        self.select = discord.ui.Select(
            placeholder="Selecciona un ciclo.",
            min_values=1,
            max_values=1,
            options=opciones,
        )

        self.select.callback = self.select_callback
        self.add_item(self.select)


    async def select_callback(self, interaction: discord.Interaction):

        ciclo_seleccionado = int(self.select.values[0])-1  # obtiene el número del ciclo seleccionado

        view1 = NumeroMenuTodosLosCiclos(ciclo_seleccionado)

        embed1 = get_ciclos_cursos_embeds()[ciclo_seleccionado]

        await interaction.response.edit_message(view=view1, embed=embed1)


class NumeroMenuTodosLosCiclos(discord.ui.View):

    def __init__(self, ciclo_seleccionado):
        super().__init__()

        self.ciclo_seleccionado = ciclo_seleccionado
        opciones = despliegue_lista_cursos()[ciclo_seleccionado]

        self.select = discord.ui.Select(
            placeholder="Selecciona un curso.",
            min_values=1,
            max_values=1,
            options=opciones,
        )

        self.select.callback = self.select_callback
        self.add_item(self.select)


    async def select_callback(self, interaction: discord.Interaction):

        curso_seleccionado = int(self.select.values[0]) - 1

        view2 = NumeroMenuOpcionesCurso(self.ciclo_seleccionado, curso_seleccionado)

        embed = get_lista_cursos_suprema_embeds()[self.ciclo_seleccionado][curso_seleccionado]
        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(view=view2, embed=embed)


class NumeroMenuOpcionesCurso(discord.ui.View):

    def __init__(self, ciclo_seleccionado, curso_seleccionado):
        super().__init__()

        self.ciclo_seleccionado = ciclo_seleccionado
        self.curso_seleccionado = curso_seleccionado

        if ciclo_seleccionado == 0:  # Primer ciclo

            if curso_seleccionado == 0: # Física 1
                opciones = despliegue_lista_opciones_LAB()

            if curso_seleccionado == 1: # Cálculo diferencial
                opciones = despliegue_lista_opciones_NO_LAB

            if curso_seleccionado == 2: # Álgebra lineal
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: # Dibujo técnico
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: # Introducción a la computación
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 5: # Realidad Nac. Constitución y DD.HH
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6: # Fundamentos de programación
                opciones = despliegue_lista_opciones_LAB()
            
        if ciclo_seleccionado == 1:  # Segundo ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 2:  # Tercer ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 3:  # Cuarto ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 4:  # Quinto ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 5:  # Sexto ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 6:  # Séptimo ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 7:  # Octavo ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 8:  # Noveno ciclo
            pass # Falta llenar

        if ciclo_seleccionado == 9:  # Cursos electivos
            pass # Falta llenar
            
        
        self.select = discord.ui.Select(
            placeholder="Selecciona un curso.",
            min_values=1,
            max_values=1,
            options=opciones,
        )

        self.select.callback = self.select_callback
        self.add_item(self.select)


    async def select_callback(self, interaction: discord.Interaction):
        
        opcion_elegida = int(self.select.values[0]) - 1
        embed =  discord.Embed(title="POR LLENAR", description="", color=discord.Color.blue())
        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(embed=embed, view=None)



# ///////////////////////////////////////////////////////////////////////////////////////////

bot.run("MTM3OTg5MDYyMjQ1Nzk3NDc5NA.G6HXNR.ig6eSs1pb0nKKCaxDoAN46UES8-xrIhF-MxNNA")
