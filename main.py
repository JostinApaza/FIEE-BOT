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
        valor_seleccionado = int(self.select.values[0])  # obtiene el número del ciclo seleccionado
        view1 = NumeroMenuPrimerCiclo(valor_seleccionado)  # crea una nueva vista
        embeds = get_ciclos_cursos_embeds()
        await interaction.response.edit_message(
            view=view1,
            embed=embeds[valor_seleccionado - 1]
        )


class NumeroMenuPrimerCiclo(discord.ui.View):

    def __init__(self, ciclo_seleccionado):
        super().__init__()

        opciones = despliegue_lista_cursos()[ciclo_seleccionado-1]

        self.select = discord.ui.Select(
            placeholder="Selecciona un curso.",
            min_values=1,
            max_values=1,
            options=opciones,
        )

        self.select.callback = self.select_callback
        self.add_item(self.select)


    async def select_callback(self, interaction: discord.Interaction):
        curso_elegido_num = int(self.select.values[0]) - 1
        embed = get_primer_ciclo_embeds()
        embed[curso_elegido_num].set_footer(text="Gracias por usar FIEE-BOT.")
        embed[curso_elegido_num].set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")
        await interaction.response.edit_message(embed=embed[curso_elegido_num], view=None)


# ///////////////////////////////////////////////////////////////////////////////////////////

bot.run("MTM3OTg5MDYyMjQ1Nzk3NDc5NA.G6HXNR.ig6eSs1pb0nKKCaxDoAN46UES8-xrIhF-MxNNA")
