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

def get_ciclos_embeds():

    embed = discord.Embed(
        title="📚 Repositorio de FIEE-BOT.",
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

def agregar_pcs_clases_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Prácticas", value="Prácticas y exámenes.", inline=False)
    embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)

    return embed

def agregar_labs_pcs_clases_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Laboratorios", value="Laboratorios de distintos ciclos.", inline=False)
    embed.add_field(name="▸  Prácticas", value="Prácticas y exámenes.", inline=False)
    embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)

    return embed


def get_primer_ciclo_embeds():
    embeds = []

    embed1 = discord.Embed(title="📚 Física 1", description="", color=discord.Color.dark_green())
    embed1 = agregar_labs_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://cdn.discordapp.com/attachments/1384359269570187284/1384616543538774246/Syllabus_BFI01_Fisica_1.pdf?ex=68531424&is=6851c2a4&hm=6e6106be23cab05db5f85fc8991dd6d80a2b4f862f14f81820c4c6e992d889d0&)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo diferencial", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Álgebra lineal", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Dibujo técnico", description="", color=discord.Color.green())
    embed4 = agregar_pcs_clases_campos(embed4)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Introducción a la computación", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Realidad Nac. Constitución y DD.HH", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Fundamentos de programación", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds


def get_segundo_ciclo_embeds():
    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Ing. térmica y de fluidos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    embed8 = discord.Embed(title="📚 Sistemas operativos I", description="", color=discord.Color.green())
    embed8 = agregar_pcs_clases_campos(embed7)
    embed8.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed8)

    return embeds

def get_tercer_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de electricidad y magnetismo", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Ecuaciones diferenciales", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Probabilidades y estadística", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Programación Orientada a Objetos", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Economía General", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redes de datos II", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds

def get_cuarto_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Introducción a la física moderna", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Análisis de señales y sistemas", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Cálculo vectorial", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Circuitos eléctricos I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Métodos numéricos", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Ética y filosofía", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Electrotecnia e instalación de redes", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    embed8 = discord.Embed(title="📚 Sistemas operativos II", description="", color=discord.Color.green())
    embed8 = agregar_pcs_clases_campos(embed7)
    embed8.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed8)

    return embeds


def get_quinto_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Mecánica de fluidos y termodinámica I", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds

def get_sexto_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Ing. térmica y de fluidos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds

def get_septimo_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Ing. térmica y de fluidos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds


def get_octavo_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Ing. térmica y de fluidos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds


def get_noveno_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Ing. térmica y de fluidos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed7)

    return embeds


def get_cursos_electivos_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Ing. térmica y de fluidos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/Documents/TODOS%20LOS%20DRIVES%20FIEE%20UNI/Drive%201er%20Ciclo/BFI01%20F%C3%ADsica%201/Syllabus%20BFI01%20(F%C3%ADsica%201).pdf)", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
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
            - [Cuaderno Física 2020-03-20 16.04.15.pdf](https://download1500.mediafire.com/9w6sla8v5drgfzbpYQAEk7ve62ssrG0oi4m88TeX2yG9NckODt96EyTnC5O4h4YlRsm2u76ObJx0NljObrDBiTuZ4auoTJ6hCWptUqNOp9-DRkVhGnbND5czu8ISHfknX6GKTWwrIVq17R3tt5NNDJ4uYEyalqY4Pwcw2DdN5XI24m8/xsswn33etbow4ng/Cuaderno+F%C3%ADsica+2020-03-20+16.04.15.pdf)
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
            - PC 5
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
            - PC 5
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
            - PC 5
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
            - PC 5
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
            - PC 5
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

def get_calculo_vectorial_cuadernos_embed():

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


# %&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def get_electromagnetismo_1_clases_embed():

    embed = discord.Embed(
        title="Clases de Electromagnetismo I.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_electromagnetismo_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de electromagnetismo_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - PC 5
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_electromagnetismo_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de electromagnetismo_1:",
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

def get_dispositivos_1_clases_embed():

    embed = discord.Embed(
        title="Clases de dispositivos_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_dispositivos_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de dispositivos_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - PC 5
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_dispositivos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de dispositivos_1:",
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


def get_mecanica_fluidos_1_clases_embed():

    embed = discord.Embed(
        title="Clases de mecanica_fluidos_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_mecanica_fluidos_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de mecanica_fluidos_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - PC 5
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_mecanica_fluidos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de mecanica_fluidos_1:",
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


def get_laboratorio_electronica_1_clases_embed():

    embed = discord.Embed(
        title="Clases de laboratorio_electronica_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_laboratorio_electronica_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de laboratorio_electronica_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - PC 5
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_laboratorio_electronica_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de laboratorio_electronica_1:",
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

def get_sistemas_control_1_clases_embed():

    embed = discord.Embed(
        title="Clases de sistemas_control_1.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_sistemas_control_1_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de sistemas_control_1:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - PC 5
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_sistemas_control_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de sistemas_control_1:",
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

def get_circuitos_2_clases_embed():

    embed = discord.Embed(
        title="Clases de circuitos_2.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_circuitos_2_examenes_embed():

    embed = discord.Embed(
        title="Practicas y exámenes de circuitos_2:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - PC 5
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_circuitos_2_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de circuitos_2:",
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



# ///////////////////////////////////////////////////////////////////////////////////////


def get_embed_curso_example():
    embed = discord.Embed(
        title="Example",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

# ////////////////////////////////////////////////////////////////////////////////////////


def get_embed_calc_diferencial_pc1():
    embed = discord.Embed(
        title="1ra PC - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calc_diferencial_pc2():
    embed = discord.Embed(
        title="2da PC - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_calc_diferencial_pc3():
    embed = discord.Embed(
        title="3ra PC - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calc_diferencial_pc4():
    embed = discord.Embed(
        title="4ta PC - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calc_diferencial_pc5():
    embed = discord.Embed(
        title="5ta PC - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calc_diferencial_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calc_diferencial_exfinal():
    embed = discord.Embed(
        title="Ex. finales - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calc_diferencial_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calc_diferencial_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - calc_diferencial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_calc_diferencial_pcs():

    lista = []

    lista.append(get_embed_calc_diferencial_pc1())
    lista.append(get_embed_calc_diferencial_pc2())
    lista.append(get_embed_calc_diferencial_pc3())
    lista.append(get_embed_calc_diferencial_pc4())
    lista.append(get_embed_calc_diferencial_pc5())
    lista.append(get_embed_calc_diferencial_exparcial())
    lista.append(get_embed_calc_diferencial_exfinal())
    lista.append(get_embed_calc_diferencial_exsusti())
    lista.append(get_embed_calc_diferencial_entrada())

    return lista


def get_embed_algebra_lineal_pc1():
    embed = discord.Embed(
        title="1ra PC - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algebra_lineal_pc2():
    embed = discord.Embed(
        title="2da PC - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_algebra_lineal_pc3():
    embed = discord.Embed(
        title="3ra PC - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algebra_lineal_pc4():
    embed = discord.Embed(
        title="4ta PC - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algebra_lineal_pc5():
    embed = discord.Embed(
        title="5ta PC - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algebra_lineal_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algebra_lineal_exfinal():
    embed = discord.Embed(
        title="Ex. finales - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algebra_lineal_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algebra_lineal_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - algebra_lineal",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_algebra_lineal_pcs():

    lista = []

    lista.append(get_embed_algebra_lineal_pc1())
    lista.append(get_embed_algebra_lineal_pc2())
    lista.append(get_embed_algebra_lineal_pc3())
    lista.append(get_embed_algebra_lineal_pc4())
    lista.append(get_embed_algebra_lineal_pc5())
    lista.append(get_embed_algebra_lineal_exparcial())
    lista.append(get_embed_algebra_lineal_exfinal())
    lista.append(get_embed_algebra_lineal_exsusti())
    lista.append(get_embed_algebra_lineal_entrada())

    return lista

def get_embed_dibujo_tecnico_pc1():
    embed = discord.Embed(
        title="1ra PC - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_dibujo_tecnico_pc2():
    embed = discord.Embed(
        title="2da PC - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_dibujo_tecnico_pc3():
    embed = discord.Embed(
        title="3ra PC - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_dibujo_tecnico_pc4():
    embed = discord.Embed(
        title="4ta PC - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_dibujo_tecnico_pc5():
    embed = discord.Embed(
        title="5ta PC - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_dibujo_tecnico_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_dibujo_tecnico_exfinal():
    embed = discord.Embed(
        title="Ex. finales - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_dibujo_tecnico_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_dibujo_tecnico_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - dibujo_tecnico",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_dibujo_tecnico_pcs():

    lista = []

    lista.append(get_embed_dibujo_tecnico_pc1())
    lista.append(get_embed_dibujo_tecnico_pc2())
    lista.append(get_embed_dibujo_tecnico_pc3())
    lista.append(get_embed_dibujo_tecnico_pc4())
    lista.append(get_embed_dibujo_tecnico_pc5())
    lista.append(get_embed_dibujo_tecnico_exparcial())
    lista.append(get_embed_dibujo_tecnico_exfinal())
    lista.append(get_embed_dibujo_tecnico_exsusti())
    lista.append(get_embed_dibujo_tecnico_entrada())

    return lista

def get_embed_intro_computacion_pc1():
    embed = discord.Embed(
        title="1ra PC - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_computacion_pc2():
    embed = discord.Embed(
        title="2da PC - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_intro_computacion_pc3():
    embed = discord.Embed(
        title="3ra PC - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_computacion_pc4():
    embed = discord.Embed(
        title="4ta PC - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_computacion_pc5():
    embed = discord.Embed(
        title="5ta PC - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_computacion_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_computacion_exfinal():
    embed = discord.Embed(
        title="Ex. finales - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_computacion_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_computacion_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - intro_computacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_intro_computacion_pcs():

    lista = []

    lista.append(get_embed_intro_computacion_pc1())
    lista.append(get_embed_intro_computacion_pc2())
    lista.append(get_embed_intro_computacion_pc3())
    lista.append(get_embed_intro_computacion_pc4())
    lista.append(get_embed_intro_computacion_pc5())
    lista.append(get_embed_intro_computacion_exparcial())
    lista.append(get_embed_intro_computacion_exfinal())
    lista.append(get_embed_intro_computacion_exsusti())
    lista.append(get_embed_intro_computacion_entrada())

    return lista

def get_embed_fundamentos_programacion_pc1():
    embed = discord.Embed(
        title="1ra PC - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_programacion_pc2():
    embed = discord.Embed(
        title="2da PC - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_fundamentos_programacion_pc3():
    embed = discord.Embed(
        title="3ra PC - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_programacion_pc4():
    embed = discord.Embed(
        title="4ta PC - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_programacion_pc5():
    embed = discord.Embed(
        title="5ta PC - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_programacion_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_programacion_exfinal():
    embed = discord.Embed(
        title="Ex. finales - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_programacion_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_programacion_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - fundamentos_programacion",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_fundamentos_programacion_pcs():

    lista = []

    lista.append(get_embed_fundamentos_programacion_pc1())
    lista.append(get_embed_fundamentos_programacion_pc2())
    lista.append(get_embed_fundamentos_programacion_pc3())
    lista.append(get_embed_fundamentos_programacion_pc4())
    lista.append(get_embed_fundamentos_programacion_pc5())
    lista.append(get_embed_fundamentos_programacion_exparcial())
    lista.append(get_embed_fundamentos_programacion_exfinal())
    lista.append(get_embed_fundamentos_programacion_exsusti())
    lista.append(get_embed_fundamentos_programacion_entrada())

    return lista

def get_embed_fisica_2_pc1():
    embed = discord.Embed(
        title="1ra PC - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc2():
    embed = discord.Embed(
        title="2da PC - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_fisica_2_pc3():
    embed = discord.Embed(
        title="3ra PC - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc4():
    embed = discord.Embed(
        title="4ta PC - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_pc5():
    embed = discord.Embed(
        title="5ta PC - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exfinal():
    embed = discord.Embed(
        title="Ex. finales - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_2_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - fisica_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_fisica_2_pcs():

    lista = []

    lista.append(get_embed_fisica_2_pc1())
    lista.append(get_embed_fisica_2_pc2())
    lista.append(get_embed_fisica_2_pc3())
    lista.append(get_embed_fisica_2_pc4())
    lista.append("get_embed_fisica_2_pc5()")
    lista.append(get_embed_fisica_2_exparcial())
    lista.append(get_embed_fisica_2_exfinal())
    lista.append(get_embed_fisica_2_exsusti())
    lista.append(get_embed_fisica_2_entrada())

    return lista

def get_embed_calculo_integral_pc1():
    embed = discord.Embed(
        title="1ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc2():
    embed = discord.Embed(
        title="2da PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_calculo_integral_pc3():
    embed = discord.Embed(
        title="3ra PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc4():
    embed = discord.Embed(
        title="4ta PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_pc5():
    embed = discord.Embed(
        title="5ta PC - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_exfinal():
    embed = discord.Embed(
        title="Ex. finales - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_integral_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - calculo_integral",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_calculo_integral_pcs():

    lista = []

    lista.append(get_embed_calculo_integral_pc1())
    lista.append(get_embed_calculo_integral_pc2())
    lista.append(get_embed_calculo_integral_pc3())
    lista.append(get_embed_calculo_integral_pc4())
    lista.append(get_embed_calculo_integral_pc5())
    lista.append(get_embed_calculo_integral_exparcial())
    lista.append(get_embed_calculo_integral_exfinal())
    lista.append(get_embed_calculo_integral_exsusti())
    lista.append(get_embed_calculo_integral_entrada())

    return lista

def get_embed_algoritmos_1_pc1():
    embed = discord.Embed(
        title="1ra PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_pc2():
    embed = discord.Embed(
        title="2da PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_algoritmos_1_pc3():
    embed = discord.Embed(
        title="3ra PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_pc4():
    embed = discord.Embed(
        title="4ta PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_pc5():
    embed = discord.Embed(
        title="5ta PC - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_algoritmos_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - algoritmos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_algoritmos_1_pcs():

    lista = []

    lista.append(get_embed_algoritmos_1_pc1())
    lista.append(get_embed_algoritmos_1_pc2())
    lista.append(get_embed_algoritmos_1_pc3())
    lista.append(get_embed_algoritmos_1_pc4())
    lista.append("get_embed_algoritmos_1_pc5()")
    lista.append(get_embed_algoritmos_1_exparcial())
    lista.append(get_embed_algoritmos_1_exfinal())
    lista.append(get_embed_algoritmos_1_exsusti())
    lista.append(get_embed_algoritmos_1_entrada())

    return lista


def get_embed_quimica_1_pc1():
    embed = discord.Embed(
        title="1ra PC - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_pc2():
    embed = discord.Embed(
        title="2da PC - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_quimica_1_pc3():
    embed = discord.Embed(
        title="3ra PC - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_pc4():
    embed = discord.Embed(
        title="4ta PC - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_pc5():
    embed = discord.Embed(
        title="5ta PC - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_quimica_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - quimica_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_quimica_1_pcs():

    lista = []

    lista.append(get_embed_quimica_1_pc1())
    lista.append(get_embed_quimica_1_pc2())
    lista.append(get_embed_quimica_1_pc3())
    lista.append(get_embed_quimica_1_pc4())
    lista.append("get_embed_quimica_1_pc5()")
    lista.append(get_embed_quimica_1_exparcial())
    lista.append(get_embed_quimica_1_exfinal())
    lista.append(get_embed_quimica_1_exsusti())
    lista.append(get_embed_quimica_1_entrada())

    return lista



def get_embed_fundamentos_computador_pc1():
    embed = discord.Embed(
        title="1ra PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_pc2():
    embed = discord.Embed(
        title="2da PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_fundamentos_computador_pc3():
    embed = discord.Embed(
        title="3ra PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_pc4():
    embed = discord.Embed(
        title="4ta PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_pc5():
    embed = discord.Embed(
        title="5ta PC - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_exfinal():
    embed = discord.Embed(
        title="Ex. finales - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fundamentos_computador_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - fundamentos_computador",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_fundamentos_computador_pcs():

    lista = []

    lista.append(get_embed_fundamentos_computador_pc1())
    lista.append(get_embed_fundamentos_computador_pc2())
    lista.append(get_embed_fundamentos_computador_pc3())
    lista.append(get_embed_fundamentos_computador_pc4())
    lista.append(get_embed_fundamentos_computador_pc5())
    lista.append(get_embed_fundamentos_computador_exparcial())
    lista.append(get_embed_fundamentos_computador_exfinal())
    lista.append(get_embed_fundamentos_computador_exsusti())
    lista.append("get_embed_fundamentos_computador_entrada()")

    return lista

def get_embed_redes_1_pc1():
    embed = discord.Embed(
        title="1ra PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_pc2():
    embed = discord.Embed(
        title="2da PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_redes_1_pc3():
    embed = discord.Embed(
        title="3ra PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_pc4():
    embed = discord.Embed(
        title="4ta PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_pc5():
    embed = discord.Embed(
        title="5ta PC - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - redes_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_redes_1_pcs():

    lista = []

    lista.append(get_embed_redes_1_pc1())
    lista.append(get_embed_redes_1_pc2())
    lista.append(get_embed_redes_1_pc3())
    lista.append(get_embed_redes_1_pc4())
    lista.append(get_embed_redes_1_pc5())
    lista.append(get_embed_redes_1_exparcial())
    lista.append(get_embed_redes_1_exfinal())
    lista.append(get_embed_redes_1_exsusti())
    lista.append(get_embed_redes_1_entrada())

    return lista


def get_embed_fund_electricidad_magnetismo_pc1():
    embed = discord.Embed(
        title="1ra PC - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fund_electricidad_magnetismo_pc2():
    embed = discord.Embed(
        title="2da PC - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_fund_electricidad_magnetismo_pc3():
    embed = discord.Embed(
        title="3ra PC - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fund_electricidad_magnetismo_pc4():
    embed = discord.Embed(
        title="4ta PC - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fund_electricidad_magnetismo_pc5():
    embed = discord.Embed(
        title="5ta PC - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fund_electricidad_magnetismo_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fund_electricidad_magnetismo_exfinal():
    embed = discord.Embed(
        title="Ex. finales - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fund_electricidad_magnetismo_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fund_electricidad_magnetismo_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - fund_electricidad_magnetismo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_fund_electricidad_magnetismo_pcs():

    lista = []

    lista.append(get_embed_fund_electricidad_magnetismo_pc1())
    lista.append(get_embed_fund_electricidad_magnetismo_pc2())
    lista.append(get_embed_fund_electricidad_magnetismo_pc3())
    lista.append(get_embed_fund_electricidad_magnetismo_pc4())
    lista.append("get_embed_fund_electricidad_magnetismo_pc5()")
    lista.append(get_embed_fund_electricidad_magnetismo_exparcial())
    lista.append(get_embed_fund_electricidad_magnetismo_exfinal())
    lista.append(get_embed_fund_electricidad_magnetismo_exsusti())
    lista.append(get_embed_fund_electricidad_magnetismo_entrada())

    return lista



def get_embed_ecuaciones_diferenciales_pc1():
    embed = discord.Embed(
        title="1ra PC - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_ecuaciones_diferenciales_pc2():
    embed = discord.Embed(
        title="2da PC - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_ecuaciones_diferenciales_pc3():
    embed = discord.Embed(
        title="3ra PC - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_ecuaciones_diferenciales_pc4():
    embed = discord.Embed(
        title="4ta PC - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_ecuaciones_diferenciales_pc5():
    embed = discord.Embed(
        title="5ta PC - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_ecuaciones_diferenciales_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_ecuaciones_diferenciales_exfinal():
    embed = discord.Embed(
        title="Ex. finales - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_ecuaciones_diferenciales_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_ecuaciones_diferenciales_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - ecuaciones_diferenciales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_ecuaciones_diferenciales_pcs():

    lista = []

    lista.append(get_embed_ecuaciones_diferenciales_pc1())
    lista.append(get_embed_ecuaciones_diferenciales_pc2())
    lista.append(get_embed_ecuaciones_diferenciales_pc3())
    lista.append(get_embed_ecuaciones_diferenciales_pc4())
    lista.append(get_embed_ecuaciones_diferenciales_pc5())
    lista.append(get_embed_ecuaciones_diferenciales_exparcial())
    lista.append(get_embed_ecuaciones_diferenciales_exfinal())
    lista.append(get_embed_ecuaciones_diferenciales_exsusti())
    lista.append(get_embed_ecuaciones_diferenciales_entrada())

    return lista


def get_embed_probabilidades_pc1():
    embed = discord.Embed(
        title="1ra PC - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_probabilidades_pc2():
    embed = discord.Embed(
        title="2da PC - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_probabilidades_pc3():
    embed = discord.Embed(
        title="3ra PC - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_probabilidades_pc4():
    embed = discord.Embed(
        title="4ta PC - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_probabilidades_pc5():
    embed = discord.Embed(
        title="5ta PC - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_probabilidades_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_probabilidades_exfinal():
    embed = discord.Embed(
        title="Ex. finales - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_probabilidades_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_probabilidades_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - probabilidades",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_probabilidades_pcs():

    lista = []

    lista.append(get_embed_probabilidades_pc1())
    lista.append(get_embed_probabilidades_pc2())
    lista.append(get_embed_probabilidades_pc3())
    lista.append(get_embed_probabilidades_pc4())
    lista.append("get_embed_probabilidades_pc5()")
    lista.append(get_embed_probabilidades_exparcial())
    lista.append(get_embed_probabilidades_exfinal())
    lista.append(get_embed_probabilidades_exsusti())
    lista.append(get_embed_probabilidades_entrada())

    return lista


def get_embed_poo_pc1():
    embed = discord.Embed(
        title="1ra PC - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_poo_pc2():
    embed = discord.Embed(
        title="2da PC - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_poo_pc3():
    embed = discord.Embed(
        title="3ra PC - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_poo_pc4():
    embed = discord.Embed(
        title="4ta PC - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_poo_pc5():
    embed = discord.Embed(
        title="5ta PC - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_poo_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_poo_exfinal():
    embed = discord.Embed(
        title="Ex. finales - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_poo_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_poo_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - poo",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_poo_pcs():

    lista = []

    lista.append(get_embed_poo_pc1())
    lista.append(get_embed_poo_pc2())
    lista.append(get_embed_poo_pc3())
    lista.append(get_embed_poo_pc4())
    lista.append("get_embed_poo_pc5()")
    lista.append(get_embed_poo_exparcial())
    lista.append(get_embed_poo_exfinal())
    lista.append(get_embed_poo_exsusti())
    lista.append(get_embed_poo_entrada())

    return lista


def get_embed_economia_pc1():
    embed = discord.Embed(
        title="1ra PC - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_economia_pc2():
    embed = discord.Embed(
        title="2da PC - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_economia_pc3():
    embed = discord.Embed(
        title="3ra PC - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_economia_pc4():
    embed = discord.Embed(
        title="4ta PC - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_economia_pc5():
    embed = discord.Embed(
        title="5ta PC - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_economia_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_economia_exfinal():
    embed = discord.Embed(
        title="Ex. finales - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_economia_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_economia_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - economia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_economia_pcs():

    lista = []

    lista.append(get_embed_economia_pc1())
    lista.append(get_embed_economia_pc2())
    lista.append(get_embed_economia_pc3())
    lista.append(get_embed_economia_pc4())
    lista.append(get_embed_economia_pc5())
    lista.append(get_embed_economia_exparcial())
    lista.append(get_embed_economia_exfinal())
    lista.append(get_embed_economia_exsusti())
    lista.append(get_embed_economia_entrada())

    return lista



def get_embed_redes_2_pc1():
    embed = discord.Embed(
        title="1ra PC - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_2_pc2():
    embed = discord.Embed(
        title="2da PC - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_redes_2_pc3():
    embed = discord.Embed(
        title="3ra PC - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_2_pc4():
    embed = discord.Embed(
        title="4ta PC - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_2_pc5():
    embed = discord.Embed(
        title="5ta PC - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_2_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_2_exfinal():
    embed = discord.Embed(
        title="Ex. finales - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_2_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_redes_2_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - redes_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_redes_2_pcs():

    lista = []

    lista.append(get_embed_redes_2_pc1())
    lista.append(get_embed_redes_2_pc2())
    lista.append(get_embed_redes_2_pc3())
    lista.append(get_embed_redes_2_pc4())
    # lista.append(get_embed_redes_2_pc5())
    # lista.append(get_embed_redes_2_exparcial())
    # lista.append(get_embed_redes_2_exfinal())
    # lista.append(get_embed_redes_2_exsusti())
    # lista.append(get_embed_redes_2_entrada())

    return lista

def get_embed_electrotecnia_pc1():
    embed = discord.Embed(
        title="1ra PC - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electrotecnia_pc2():
    embed = discord.Embed(
        title="2da PC - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_electrotecnia_pc3():
    embed = discord.Embed(
        title="3ra PC - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electrotecnia_pc4():
    embed = discord.Embed(
        title="4ta PC - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electrotecnia_pc5():
    embed = discord.Embed(
        title="5ta PC - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electrotecnia_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electrotecnia_exfinal():
    embed = discord.Embed(
        title="Ex. finales - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electrotecnia_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electrotecnia_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - electrotecnia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_electrotecnia_pcs():

    lista = []

    lista.append(get_embed_electrotecnia_pc1())
    lista.append(get_embed_electrotecnia_pc2())
    lista.append(get_embed_electrotecnia_pc3())
    lista.append(get_embed_electrotecnia_pc4())
    lista.append(get_embed_electrotecnia_pc5())
    lista.append(get_embed_electrotecnia_exparcial())
    lista.append(get_embed_electrotecnia_exfinal())
    lista.append(get_embed_electrotecnia_exsusti())
    lista.append(get_embed_electrotecnia_entrada())

    return lista

def get_embed_intro_moderna_pc1():
    embed = discord.Embed(
        title="1ra PC - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_moderna_pc2():
    embed = discord.Embed(
        title="2da PC - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_intro_moderna_pc3():
    embed = discord.Embed(
        title="3ra PC - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_moderna_pc4():
    embed = discord.Embed(
        title="4ta PC - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_moderna_pc5():
    embed = discord.Embed(
        title="5ta PC - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_moderna_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_moderna_exfinal():
    embed = discord.Embed(
        title="Ex. finales - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_moderna_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_intro_moderna_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - intro_moderna",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_intro_moderna_pcs():

    lista = []

    lista.append(get_embed_intro_moderna_pc1())
    lista.append(get_embed_intro_moderna_pc2())
    lista.append(get_embed_intro_moderna_pc3())
    lista.append(get_embed_intro_moderna_pc4())
    lista.append("get_embed_intro_moderna_pc5()")
    lista.append(get_embed_intro_moderna_exparcial())
    lista.append(get_embed_intro_moderna_exfinal())
    lista.append(get_embed_intro_moderna_exsusti())
    lista.append(get_embed_intro_moderna_entrada())

    return lista


def get_embed_analisis_senales_pc1():
    embed = discord.Embed(
        title="1ra PC - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_analisis_senales_pc2():
    embed = discord.Embed(
        title="2da PC - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_analisis_senales_pc3():
    embed = discord.Embed(
        title="3ra PC - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_analisis_senales_pc4():
    embed = discord.Embed(
        title="4ta PC - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_analisis_senales_pc5():
    embed = discord.Embed(
        title="5ta PC - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_analisis_senales_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_analisis_senales_exfinal():
    embed = discord.Embed(
        title="Ex. finales - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_analisis_senales_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_analisis_senales_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - analisis_senales",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_analisis_senales_pcs():

    lista = []

    lista.append(get_embed_analisis_senales_pc1())
    lista.append(get_embed_analisis_senales_pc2())
    lista.append(get_embed_analisis_senales_pc3())
    lista.append(get_embed_analisis_senales_pc4())
    lista.append(get_embed_analisis_senales_pc5())
    lista.append(get_embed_analisis_senales_exparcial())
    lista.append(get_embed_analisis_senales_exfinal())
    lista.append(get_embed_analisis_senales_exsusti())
    lista.append(get_embed_analisis_senales_entrada())

    return lista


def get_embed_calculo_vectorial_pc1():
    embed = discord.Embed(
        title="1ra PC - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_vectorial_pc2():
    embed = discord.Embed(
        title="2da PC - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_calculo_vectorial_pc3():
    embed = discord.Embed(
        title="3ra PC - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_vectorial_pc4():
    embed = discord.Embed(
        title="4ta PC - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_vectorial_pc5():
    embed = discord.Embed(
        title="5ta PC - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_vectorial_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_vectorial_exfinal():
    embed = discord.Embed(
        title="Ex. finales - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_vectorial_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_calculo_vectorial_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - calculo_vectorial",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_calculo_vectorial_pcs():

    lista = []

    lista.append(get_embed_calculo_vectorial_pc1())
    lista.append(get_embed_calculo_vectorial_pc2())
    lista.append(get_embed_calculo_vectorial_pc3())
    lista.append(get_embed_calculo_vectorial_pc4())
    lista.append(get_embed_calculo_vectorial_pc5())
    lista.append(get_embed_calculo_vectorial_exparcial())
    lista.append(get_embed_calculo_vectorial_exfinal())
    lista.append(get_embed_calculo_vectorial_exsusti())
    lista.append(get_embed_calculo_vectorial_entrada())

    return lista


def get_embed_circuitos_1_pc1():
    embed = discord.Embed(
        title="1ra PC - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_circuitos_1_pc2():
    embed = discord.Embed(
        title="2da PC - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_circuitos_1_pc3():
    embed = discord.Embed(
        title="3ra PC - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_circuitos_1_pc4():
    embed = discord.Embed(
        title="4ta PC - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_circuitos_1_pc5():
    embed = discord.Embed(
        title="5ta PC - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_circuitos_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_circuitos_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_circuitos_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_circuitos_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - circuitos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_circuitos_1_pcs():

    lista = []

    lista.append(get_embed_circuitos_1_pc1())
    lista.append(get_embed_circuitos_1_pc2())
    lista.append(get_embed_circuitos_1_pc3())
    lista.append(get_embed_circuitos_1_pc4())
    lista.append(get_embed_circuitos_1_pc5())
    lista.append(get_embed_circuitos_1_exparcial())
    lista.append(get_embed_circuitos_1_exfinal())
    lista.append(get_embed_circuitos_1_exsusti())
    lista.append(get_embed_circuitos_1_entrada())

    return lista

def get_embed_metodos_numericos_pc1():
    embed = discord.Embed(
        title="1ra PC - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_metodos_numericos_pc2():
    embed = discord.Embed(
        title="2da PC - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_metodos_numericos_pc3():
    embed = discord.Embed(
        title="3ra PC - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_metodos_numericos_pc4():
    embed = discord.Embed(
        title="4ta PC - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_metodos_numericos_pc5():
    embed = discord.Embed(
        title="5ta PC - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_metodos_numericos_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_metodos_numericos_exfinal():
    embed = discord.Embed(
        title="Ex. finales - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_metodos_numericos_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_metodos_numericos_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - metodos_numericos",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_metodos_numericos_pcs():

    lista = []

    lista.append(get_embed_metodos_numericos_pc1())
    lista.append(get_embed_metodos_numericos_pc2())
    lista.append(get_embed_metodos_numericos_pc3())
    lista.append(get_embed_metodos_numericos_pc4())
    lista.append(get_embed_metodos_numericos_pc5())
    lista.append(get_embed_metodos_numericos_exparcial())
    lista.append(get_embed_metodos_numericos_exfinal())
    lista.append(get_embed_metodos_numericos_exsusti())
    lista.append(get_embed_metodos_numericos_entrada())

    return lista


def get_embed_etica_filosofia_pc1():
    embed = discord.Embed(
        title="1ra PC - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_etica_filosofia_pc2():
    embed = discord.Embed(
        title="2da PC - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_etica_filosofia_pc3():
    embed = discord.Embed(
        title="3ra PC - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_etica_filosofia_pc4():
    embed = discord.Embed(
        title="4ta PC - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_etica_filosofia_pc5():
    embed = discord.Embed(
        title="5ta PC - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_etica_filosofia_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_etica_filosofia_exfinal():
    embed = discord.Embed(
        title="Ex. finales - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_etica_filosofia_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_etica_filosofia_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - etica_filosofia",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_etica_filosofia_pcs():

    lista = []

    lista.append(get_embed_etica_filosofia_pc1())
    lista.append(get_embed_etica_filosofia_pc2())
    lista.append(get_embed_etica_filosofia_pc3())
    lista.append(get_embed_etica_filosofia_pc4())
    lista.append(get_embed_etica_filosofia_pc5())
    lista.append(get_embed_etica_filosofia_exparcial())
    lista.append(get_embed_etica_filosofia_exfinal())
    lista.append(get_embed_etica_filosofia_exsusti())
    lista.append(get_embed_etica_filosofia_entrada())

    return lista


def get_embed_sistemas_operativos_2_pc1():
    embed = discord.Embed(
        title="1ra PC - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_2_pc2():
    embed = discord.Embed(
        title="2da PC - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_sistemas_operativos_2_pc3():
    embed = discord.Embed(
        title="3ra PC - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_2_pc4():
    embed = discord.Embed(
        title="4ta PC - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_2_pc5():
    embed = discord.Embed(
        title="5ta PC - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_2_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_2_exfinal():
    embed = discord.Embed(
        title="Ex. finales - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_2_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_2_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - sistemas_operativos_2",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_sistemas_operativos_2_pcs():

    lista = []

    lista.append(get_embed_sistemas_operativos_2_pc1())
    lista.append(get_embed_sistemas_operativos_2_pc2())
    lista.append(get_embed_sistemas_operativos_2_pc3())
    lista.append(get_embed_sistemas_operativos_2_pc4())
    lista.append(get_embed_sistemas_operativos_2_pc5())
    lista.append(get_embed_sistemas_operativos_2_exparcial())
    lista.append(get_embed_sistemas_operativos_2_exfinal())
    lista.append(get_embed_sistemas_operativos_2_exsusti())
    lista.append(get_embed_sistemas_operativos_2_entrada())

    return lista

def get_embed_sistemas_operativos_1_pc1():
    embed = discord.Embed(
        title="1ra PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_pc2():
    embed = discord.Embed(
        title="2da PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_sistemas_operativos_1_pc3():
    embed = discord.Embed(
        title="3ra PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_pc4():
    embed = discord.Embed(
        title="4ta PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_pc5():
    embed = discord.Embed(
        title="5ta PC - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_sistemas_operativos_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - sistemas_operativos_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_sistemas_operativos_1_pcs():

    lista = []

    lista.append(get_embed_sistemas_operativos_1_pc1())
    lista.append(get_embed_sistemas_operativos_1_pc2())
    lista.append(get_embed_sistemas_operativos_1_pc3())
    lista.append(get_embed_sistemas_operativos_1_pc4())
    lista.append(get_embed_sistemas_operativos_1_pc5())
    lista.append(get_embed_sistemas_operativos_1_exparcial())
    lista.append(get_embed_sistemas_operativos_1_exfinal())
    lista.append(get_embed_sistemas_operativos_1_exsusti())
    lista.append(get_embed_sistemas_operativos_1_entrada())

    return lista


def get_embed_electromagnetismo_1_pc1():
    embed = discord.Embed(
        title="1ra PC - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electromagnetismo_1_pc2():
    embed = discord.Embed(
        title="2da PC - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_electromagnetismo_1_pc3():
    embed = discord.Embed(
        title="3ra PC - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electromagnetismo_1_pc4():
    embed = discord.Embed(
        title="4ta PC - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electromagnetismo_1_pc5():
    embed = discord.Embed(
        title="5ta PC - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electromagnetismo_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electromagnetismo_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electromagnetismo_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_electromagnetismo_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - electromagnetismo_1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_electromagnetismo_1_pcs():

    lista = []

    lista.append(get_embed_electromagnetismo_1_pc1())
    lista.append(get_embed_electromagnetismo_1_pc2())
    lista.append(get_embed_electromagnetismo_1_pc3())
    lista.append(get_embed_electromagnetismo_1_pc4())
    lista.append("get_embed_electromagnetismo_1_pc5()")
    lista.append(get_embed_electromagnetismo_1_exparcial())
    lista.append(get_embed_electromagnetismo_1_exfinal())
    lista.append(get_embed_electromagnetismo_1_exsusti())
    lista.append(get_embed_electromagnetismo_1_entrada())

    return lista


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def get_embed_cursobase_pc1():
    embed = discord.Embed(
        title="1ra PC - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_cursobase_pc2():
    embed = discord.Embed(
        title="2da PC - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_cursobase_pc3():
    embed = discord.Embed(
        title="3ra PC - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_cursobase_pc4():
    embed = discord.Embed(
        title="4ta PC - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_cursobase_pc5():
    embed = discord.Embed(
        title="5ta PC - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_cursobase_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_cursobase_exfinal():
    embed = discord.Embed(
        title="Ex. finales - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_cursobase_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorio - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_cursobase_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - cursobase",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_cursobase_pcs():

    lista = []

    lista.append(get_embed_cursobase_pc1())
    lista.append(get_embed_cursobase_pc2())
    lista.append(get_embed_cursobase_pc3())
    lista.append(get_embed_cursobase_pc4())
    lista.append(get_embed_cursobase_pc5())
    lista.append(get_embed_cursobase_exparcial())
    lista.append(get_embed_cursobase_exfinal())
    lista.append(get_embed_cursobase_exsusti())
    lista.append(get_embed_cursobase_entrada())

    return lista


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# ///////////////////////////////////////////////////////////////////////////////////////


def get_embed_fisica_1_laboratorios_2019_II():
    embed = discord.Embed(
        title="Laboratorios de Física 1 - 2019-II",
        description=textwrap.dedent(f"""\
            - [LAB N°1_ MEDICIÓN Y ERROR EXPERIMENTAL.docx](https://cdn.discordapp.com/attachments/1384359269570187284/1384359292563357848/Lab_N1__MEDICION_Y_ERROR_EXPERIMENTAL.docx?ex=6852248f&is=6850d30f&hm=70ab2e162258ffcc04430aaf2d9fc5b86c554d3e371bdf816ab03430bf0fcfa4&)
            - [LAB N°2 FIA UNI_ VELOCIDAD INSTANTÁNEA Y ACELERACIÓN.doc](https://cdn.discordapp.com/attachments/1384359269570187284/1384359441343709194/Lab_N2_FIA_UNI__VELOCIDAD_INSTANTANEA_Y_ACELERACION.doc?ex=685224b2&is=6850d332&hm=ef2b96fa937317e7ed0744cfbfcb23e0d4687a2a08d0bdf0866ffcd143ae87ac&)
            - [LAB N°2_ VELOCIDAD INSTANTÁNEA Y ACELERACIÓN.docx](https://cdn.discordapp.com/attachments/1384359269570187284/1384359450520981544/Lab_N2__VELOCIDAD_INSTANTANEA_Y_ACELERACION.docx?ex=685224b5&is=6850d335&hm=483629508bf29b0fef5dca464ab7761e221b0c65a3970292514463091733f70a&)
            - [LAB N°4_ TRABAJO Y ENERGÍA.docx](https://cdn.discordapp.com/attachments/1384359269570187284/1384359467419828245/Lab_N4__TRABAJO_Y_ENERGIA.docx?ex=685224b9&is=6850d339&hm=582a7e3cffbd5e924c2f7258fe9081c99ca94351842da738123b3d60af238191&)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_laboratorios_2020_II():
    embed = discord.Embed(
        title="Laboratorios de Física 1 - 2020-II",
        description=textwrap.dedent(f"""\
            - [Guía de Laboratorio 1 ciclo 2020-2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384370133379711066/Guia_de_Laboratorio_1_ciclo_2020-2.pdf?ex=68522ea8&is=6850dd28&hm=13c6c4cbfb94155de7761a8558864c849249f0a3af667cbac5066458b3814ad7&)
            - [GUIA LABORATORIO 2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384371196820328539/GUIA_LABORATORIO_2.pdf?ex=68522fa5&is=6850de25&hm=89185fe2638b3ac4083596f38b15187c69caf68db48606f9c02bd49d2415bde4&)
            - [Test N°2 Ajuste de datos.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384371226939490304/Test_N2_Ajuste_de_datos.pdf?ex=68522fac&is=6850de2c&hm=9c683cb274bca40420424b46bb639688cf96a66451d0973687d8d7686c010344&)
            - [Guia Laboratorio 3.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384371523678376006/Guia_Laboratorio_3.pdf?ex=68522ff3&is=6850de73&hm=0cffcda31e54a8117fe5fbb9194d230f5c881d95f1feaf23e5775b55784d6f5b&)
            - [Laboratorio 4 Movimiento de un proyectil.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384372361524150312/Laboratorio_4_Movimiento_de_un_proyectil.pdf?ex=685230bb&is=6850df3b&hm=f21584ef798abd62a750c111036b700457d921eb91114864c79e679e039ad979&)
            - [Laboratorio 5 Principio de Conservación de la Energía.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384372361163444265/Laboratorio_5_Principio_de_Conservacion_de_la_Energia.pdf?ex=685230bb&is=6850df3b&hm=f56dfeccf6d400d1cb1cd1705379ef458f8e5c8d48430aad073891e88ce64eef&)
            - [Laboratorio 06 10-02-2021.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384372360706134026/Laboratorio_06_10-02-2021.pdf?ex=685230bb&is=6850df3b&hm=4d5aeff8a9a17759cba5f6845a603a71d2ca2d5a597f1370e63ddb381d4095a5&)
            - [Indicaciones de Laboratorio N°1 BFI01 (Prof. Huallpa).mp4](https://unipe-my.sharepoint.com/personal/junior_veli_m_uni_pe/_layouts/15/stream.aspx?id=%2Fpersonal%2Fjunior%5Fveli%5Fm%5Funi%5Fpe%2FDocuments%2FTODOS%20LOS%20DRIVES%20FIEE%20UNI%2FDrive%201er%20Ciclo%2FBFI01%20F%C3%ADsica%201%2FLaboratorios%202020%2DI%2DII%20%28Virtuales%29%2FLaboratorio%20N%C2%B01%20%28Mediciones%20y%20Propagaci%C3%B3n%20de%20Errores%29%2FIndicaciones%20de%20Laboratorio%20N%C2%B01%20BFI01%20%28Prof%2E%20Huallpa%29%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E9f1ef0c0%2D8f1e%2D461a%2Da151%2Dc208840cbcb6)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_laboratorios_2021_II():

    embed = discord.Embed(
        title="Laboratorios de Física 1 - 2021-II",
        description=textwrap.dedent(f"""\
            - [Exp01Errores.docx (1).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375018586378240/Exp01Errores.docx_1.pdf?ex=68523334&is=6850e1b4&hm=4aef33bda669a26a09536bc3f9c4d0bac40b953dde75e7b12c5fc0bfcd913d5a&)
            - [Exp02 Estadistica (4).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375018032599040/Exp02_Estadistica_4.pdf?ex=68523334&is=6850e1b4&hm=b6079af3e4710bae5fc303d77ead999cd461f75884c3cdd7bdfdbbc357f40620&)
            - [EXp3 Pendulo (2).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375017726283796/EXp3_Pendulo_2.pdf?ex=68523334&is=6850e1b4&hm=cd85cb3954fffe4160f79149c320baacee9be8d65747da79801a67cd1e10244d&)
            - [EXp04 Movimiento Rectilíneo Trucker OK (1).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375016874840104/EXp04_Movimiento_Rectilineo_Trucker_OK_1.pdf?ex=68523334&is=6850e1b4&hm=2f82048e87cfca0b7f1cbc9dae3c1819f92afb8042a624e2bd2c13386ab3036a&)
            - [Exp5 Centro de masa Tracker (1).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375016572981248/Exp5_Centro_de_masa_Tracker_1.pdf?ex=68523334&is=6850e1b4&hm=829a55b0a68f55cc65512820aa0df79e492f36cf7a28c25e69e069594244f849&)
            - [Exp6 Colisiones Tracker.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375015926927360/Exp6_Colisiones_Tracker.pdf?ex=68523334&is=6850e1b4&hm=3d663303efc97dba7e501cc1871fe4652deef38e25c2c90ea7ab9882216f81c6&)
            - [EXp7 Colisiones 2 Tracker.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375015591641148/EXp7_Coliciones_2_Trucker.pdf?ex=68523334&is=6850e1b4&hm=41b1832da785f6dffdbeb081ddc38d1b45befffcd54044b66d2b88baa8ea2d38&)
            - [laboratorio N°4 (Reparado) (1) (5) (1).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375017206317087/laboratorio_N4_Reparado_1_5_1.pdf?ex=68523334&is=6850e1b4&hm=0d81aef0076450716e29822c4cf080b3dd8cc8d5d1fc71e3e1d6379976aa7672&)
            - [Laboratorio de Física N°5.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384375016250150912/Laboratorio_de_Fisica_N5.pdf?ex=68523334&is=6850e1b4&hm=b81f3d378a43044fe5ada2bd5523d028e30b1cc905e228616ade5eb75bc2a4cf&)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_fisica_1_laboratorios_2023_I_pag1():

    embed = discord.Embed(
        title="Laboratorios de Física 1 - 2023-I",
        description=textwrap.dedent(f"""\
            - [Guía de lab 1 y 2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384377554621825074/Guia_de_lab_1_y_2.pdf?ex=68523591&is=6850e411&hm=5a79b0fa5033483d72eb33725bf666793c6f07f5db28c2e991331ae2d2f4b9a4&)
            - [Guía lab 3 .pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384377554999181382/Guia_lab_3_.pdf?ex=68523591&is=6850e411&hm=23923aff2520cb62faa5454a3847465ecde24fe2d96578c5bbf8636ece756ba9&)
            - [Guía lab 4.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384377555326603345/Guia_lab_4.pdf?ex=68523591&is=6850e411&hm=9090d09888b1edc21037dfb59b1a0f1ebfc83a1e7b4886f2575fb77ab15d28a5&)
            - [Guía lab 5 (1).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384377555670270032/Guia_lab_5_1.pdf?ex=68523591&is=6850e411&hm=35780739fb74976db2782855eb53a81a3dab2146bdc8e8fb3288b07ae57eb70c&)
            - [Guía lab 5 (2).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384377556010270720/Guia_lab_5_2.pdf?ex=68523591&is=6850e411&hm=9873b5c85cbc75b039e812ae0f414856b27042ee45b5b025a11fdddc8d98ea58&)
            - [Guía lab 6.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384377556295356478/Guia_lab_6.pdf?ex=68523591&is=6850e411&hm=1ee6f91f03d1333a1db27500c66ae3d83cb8532b3ecc224bd21e5bc459ea4071&)
            - [Estructura de informes.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384377554227429427/Estructura_de_informes.pdf?ex=68523591&is=6850e411&hm=90305bdf526810cac7b2d467a562f8a016edf0175f627abf4f71342a99e4e7c5&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_laboratorios_2023_I_pag2():

    embed = discord.Embed(
        title="Laboratorios de Física 1 - 2023-I",
        description=textwrap.dedent(f"""\
            - [LAB NRO 1 (NOTA 11).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384382691566424184/LAB_NRO_1_NOTA_11.pdf?ex=68523a5a&is=6850e8da&hm=3f87c53cef9d849f8083bfcd3080c6f430cfb3a7c6d667f967b1db8b9e3149c5&)
            - [LAB NRO 2 (NOTA 14).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384382692082319421/LAB_NRO_2_NOTA_14.pdf?ex=68523a5a&is=6850e8da&hm=cbf4e3c8bf1ff6c5104e3385b3bf822a0c4050f5dae48cf594753e9553a8e793&)
            - [LAB NRO 3 (NOTA 15).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384382692509880351/LAB_NRO_3_NOTA_15.pdf?ex=68523a5a&is=6850e8da&hm=ba4ef9bd5bd895c8a6d4ebdfdd72c5d2c0b1e3c2f3d622cc7dabe9acdb8e0f90&)
            - [LAB NRO 4 (NOTA 15).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384382692933501058/LAB_NRO_4_NOTA_15.pdf?ex=68523a5a&is=6850e8da&hm=cdf9fcf03cae6bae9d44960eec137388b2754ce303c16a4ce2f8dbb40b3cccd2&)
            - [LAB NRO 5 (NOTA 15).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384382693491347536/LAB_NRO_5_NOTA_15.pdf?ex=68523a5a&is=6850e8da&hm=0a882ee8e6f0fb4aef37925cb4d014b0a251c487131077114d76b2daddb8e76c&)
            - [LAB NRO 6 (NOTA 12).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384382694095323136/LAB_NRO_6_NOTA_12.pdf?ex=68523a5a&is=6850e8da&hm=cc3ac671acc81b185591389d87db73b67d5b1effaf5abf0b9221e50334c4ae9d&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embeds_fisica_1_labos():

    lista = []

    lista.append(get_embed_fisica_1_laboratorios_2019_II())
    lista.append(get_embed_fisica_1_laboratorios_2020_II())
    lista.append(get_embed_fisica_1_laboratorios_2021_II())
    lista.append(get_embed_fisica_1_laboratorios_2023_I_pag1())
    lista.append(get_embed_fisica_1_laboratorios_2023_I_pag2())

    return lista

def get_embed_fisica_1_pc1_1():
    embed = discord.Embed(
        title="1ra PC - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_pc1_2():
    embed = discord.Embed(
        title="1ra PC - Física 1",
        description=textwrap.dedent(f"""\
            - [PC-1 24-3.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384974935256072224/PC-1_24-3.pdf?ex=685461ec&is=6853106c&hm=99912f8d615daeed34a72f7dba408e72a55193d6c4ff8292e60f5aa9ce80134d&)
            - [PC-1 24-2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384974935679832064/PC-1_24-2.pdf?ex=685461ec&is=6853106c&hm=1c6420dc8e214cd9cfd88ef1857528ec4349b484ce27700d0a63b2b8c9d0b066&)
            - [PC1 BF101 M 23-3.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384975794941726750/PC1_BF101_M_23-3.pdf?ex=685462b9&is=68531139&hm=432d377d91be920c233b7bdfe3182791822495d3ffaefe0af13a1cd43f03983a&)
            - [PC1 BFI01 N 23-3.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384975974902403204/PC1_BFI01_N_23-3.pdf?ex=685462e4&is=68531164&hm=7603daf8b8dd223f82771647ab5f4712071302de9b56bd6e8b75e70a1b80c2b6&)
            - [PC1 BFI01 23-2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384975794664771614/PC1_BFI01_23-2.pdf?ex=685462b9&is=68531139&hm=c1808d00337cf93cb88dad06449df6d92204b6f542bdc94a1911b469e3d8c91f&)
            - [PC-1 23-1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384974936220766318/PC-1_23-1.pdf?ex=685461ec&is=6853106c&hm=cbc06f3b75493c4ddec87edb0f99901b866f3d4d6b6275de0c2c31203be66fe5&)
            - [PC-1 22-2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384974936841388083/PC-1_22-2.pdf?ex=685461ec&is=6853106c&hm=3a11d7373bc3306b076ed2113501f0a20d4d708a3cb16bfefdee936b407d073c&)
            - [PC-1 22-1 MNO.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384974937294377072/PC-1_22-1_MNO.pdf?ex=685461ec&is=6853106c&hm=67d953d583219fdd01565638807fe6ed949e8973f44c2cfcb569d77078c92e53&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_pc1_3():
    embed = discord.Embed(
        title="1ra PC - Física 1",
        description=textwrap.dedent(f"""\
            - [PC-1 21-2 L3 Sol Prob 1,2,3,4 (Prof. Huallpa) Fisica 1.xlsx](https://cdn.discordapp.com/attachments/1384359269570187284/1384973545641214123/PC-1_21-2_L3_Sol_Prob_1234_Prof._Huallpa_Fisica_1.xlsx?ex=685460a0&is=68530f20&hm=7aa983aa0f3474db237eb539d3119fda0e2988e945e0416a6aac97d7fb40cd77&)
            - [PC-1 21-2 L3 (Prof. Huallpa) Fisica 1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384973517883441212/PC-1_21-2_L2_Sol_Prof._Caro__Fisica_1.pdf?ex=6854609a&is=68530f1a&hm=d7d2a950f5e70fed445a3f57fb5c27d61e4eb0b7af1b79026593c1cc13e1eba9&)
            - [PC-1 21-2 L2 Sol (Prof. Caro) Fisica 1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384973517883441212/PC-1_21-2_L2_Sol_Prof._Caro__Fisica_1.pdf?ex=6854609a&is=68530f1a&hm=d7d2a950f5e70fed445a3f57fb5c27d61e4eb0b7af1b79026593c1cc13e1eba9&)
            - [PC-1 21-2 L2 (Prof. Caro) Fisica 1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384973518193688728/PC-1_21-2_L2_Prof._Caro__Fisica_1.pdf?ex=6854609a&is=68530f1a&hm=63e4177fd54521dc134d024887c206c3aa696f3be4e18a9689a7b533710104b2&)
            - [PC-1 21-2 L1 (Prof. Luis Durand) Fisica 1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384973518499741817/PC-1_21-2_L1_Prof._Luis_Durand__Fisica_1.pdf?ex=6854609a&is=68530f1a&hm=dc5aab4824cb9797e1fe8ada78d497c20b905baace7646685435f0b21af11e37&)
            - [PC-1 21-1 L3 (Prof. Huallpa) Fisica 1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384973518864908388/PC-1_21-1_L3_Prof._Huallpa_.Fisica_1.pdf?ex=6854609a&is=68530f1a&hm=778a1415adc680e3bc7958995614b1000c09b7af9df1a5ee838927b83f8114f8&)
            - [PC-1 21-1 L2 (Prof. Durand) Física I.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384973519300853760/PC-1_21-1_L2_Prof._Durand_Fisica_I.pdf?ex=6854609a&is=68530f1a&hm=e59087a9c1ec58be2a642d70e4b7b044a5a1ad961044a9df42ad891c3a563c9d&)
            - [PC-1 21-1 L1 (Prof. Luis Durand) Fisica 1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384973519649243237/PC-1_21-1_L1_Prof._Luis_Durand__.Fisica_1.pdf?ex=6854609a&is=68530f1a&hm=80afd79b0114175ea7b0b0c87b3eeabd1466913519759761fbf078cf3993b798&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed


def get_embed_fisica_1_pc1_4():
    embed = discord.Embed(
        title="1ra PC - Física 1",
        description=textwrap.dedent(f"""\
            - [PC-1 20-2 (Prof. Llamoja).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972709720621166/PC-1_20-2_Prof._Llamoja.pdf?ex=68545fd9&is=68530e59&hm=1fa0302ea46fce5e7feea771ac2a8d08272cb3466b9c0d71f8f50dc169751ae8&)
            - [PC-1 20-1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972710043717703/PC-1_20-1.pdf?ex=68545fd9&is=68530e59&hm=a2d661282a1729c29503bdc3d4ee985233cb394a9fcd70f6dc1b3fa41f2e3190&)
            - [PC-1 19-2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972710400229516/PC-1_19-2.pdf?ex=68545fd9&is=68530e59&hm=c23102cb1e6cc13f9b71e1bfbc2440ab0eacb8e051380228310075a7a2c47fac&)
            - [PC-1 19-1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972710710345801/PC-1_19-1.pdf?ex=68545fd9&is=68530e59&hm=a8be766eb26d6907dd8998ccd67948244b3157509a65b503d3cd9427bf6b1078&)
            - [PC-1 18-2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972710991630489/PC-1_18-2.pdf?ex=68545fd9&is=68530e59&hm=2cb5e169de0239c9d87ddc36b69fa31d6d69229050c532efc365cce47d4334b1&)
            - [PC-1 18-1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972711314329670/PC-1_18-1.pdf?ex=68545fd9&is=68530e59&hm=6972890a13ee28310b0419f5860f3cf09ca213245d83a63efd9bf01b19d6951b&)
            - [PC-1 17-2.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972711696142440/PC-1_17-2.pdf?ex=68545fda&is=68530e5a&hm=d36e3ce9fea0149ea813f311a88478ec309c7a754f22fbcc8d7695ee5da9afd1&)
            - [PC-1 17-1.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384972712061173890/PC-1_17-1.pdf?ex=68545fda&is=68530e5a&hm=307aca3c0f4db749601f5b89317a118fd753ef4610fdc5a9e35d6552c3750b65&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 3. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_pc1():
    
    lista = []

    # lista.append(get_embed_fisica_1_pc1_1()) # [0]
    lista.append(get_embed_fisica_1_pc1_2()) # [1]
    lista.append(get_embed_fisica_1_pc1_3()) # [2]
    lista.append(get_embed_fisica_1_pc1_4()) # [3]

    return lista

def get_embed_fisica_1_pc2():
    embed = discord.Embed(
        title="2da PC - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_fisica_1_pc3():
    embed = discord.Embed(
        title="3ra PC - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed
def get_embed_fisica_1_pc4():
    embed = discord.Embed(
        title="4ta PC - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_exparcial():
    embed = discord.Embed(
        title="Ex. Parciales - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_exfinal():
    embed = discord.Embed(
        title="Ex. finales - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_exsusti():
    embed = discord.Embed(
        title="Ex. sustitutorios - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_entrada():
    embed = discord.Embed(
        title="Pruebas de entrada - Física 1",
        description=textwrap.dedent(f"""\
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed



def get_embeds_fisica_1_pcs():

    lista = []

    lista.append(get_embed_fisica_1_pc1()) # [0]
    lista.append(get_embed_fisica_1_pc2())
    lista.append(get_embed_fisica_1_pc3())
    lista.append(get_embed_fisica_1_pc4())
    lista.append("get_embed_fisica_1_pc5()")
    lista.append(get_embed_fisica_1_exparcial()) # [5]
    lista.append(get_embed_fisica_1_exfinal()) # [6]
    lista.append(get_embed_fisica_1_exsusti()) # [7]
    lista.append(get_embed_fisica_1_entrada()) # [8]

    return lista


def get_embed_fisica_1_clase_caro():
    embed = discord.Embed(
        title="Clases PDF's Prof. Caro",
        description=textwrap.dedent(f"""\
            - [01. Teoria de Errores-JAC.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384933391635583119/01._Teoria_de_Errores-JAC.pdf?ex=68543b3b&is=6852e9bb&hm=3c37db81aa4307b5cc5000f20352aade214b34eef5485035d7d937c328edadb2&)
            - [02. Mov. Curvilineo.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384933391241183372/02._Mov._Curvilineo.pdf?ex=68543b3b&is=6852e9bb&hm=00773f2d32fdf8dfb6dd18f02e78b54058e65d1fad42f8ff5869c7aa8aea4146&)
            - [03. MCL-M2D.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384933390943260783/03._MCL-M2D.pdf?ex=68543b3b&is=6852e9bb&hm=a52cc93f9787b375bf1992183b626e5e106282876f5beef50d662b916f0cfae9&)
            - [04. Mov. Dependientes.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384933390620430478/04._Mov._Dependientes.pdf?ex=68543b3b&is=6852e9bb&hm=c0333b2ef8201cfa30d7d02caeb7945deb81be89b0bb08815c70297fad9c98aa&)
            - [05. Mov. Curvilineo.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384933390305984706/05._Mov._Curvilineo.pdf?ex=68543b3b&is=6852e9bb&hm=0a0a101cb110ac511b23522026583a396fb6f1d2c6f1ff19428600ffa8cfbf8d&)
            - [06. Mov. Relativo.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384935532546756793/06._Mov._Relativo.pdf?ex=68543d39&is=6852ebb9&hm=f8bc5f224066046facbb74ff9ffa5c0add891f7b66bcd25f5c4aef4e4972abe1&)
            - [07. Dinámica-JCA.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384935531938578544/07._Dinamica-JCA.pdf?ex=68543d39&is=6852ebb9&hm=720bc9938b9b74f31bbdec61c9be252841c830f9c8d55ca9868bd76596cf3bbe&)
            - [08. Dinámica SR no I.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384935531544318052/08._Dinamica_SR_no_I.pdf?ex=68543d39&is=6852ebb9&hm=51f2097f96ee24a4ba75e64502a95058e805a4b5573dd4c5c34c78a2292a51e7&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_clase_caro2():
    embed = discord.Embed(
        title="Clases PDF's Prof. Caro",
        description=textwrap.dedent(f"""\
            - [09. Trabajo-Energía.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384935531112038512/09._Trabajo-Energia.pdf?ex=68543d39&is=6852ebb9&hm=3b6c6dde8d60b9823e8ad7e1cdfe26006b235aa14c3cf5a841a00ec5ed54dbaa&)
            - [10. Impulso - Momentum.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384935530315387012/10._Impulso_-_Momentum.pdf?ex=68543d39&is=6852ebb9&hm=7197b1fde81a25d9facbc310776a2618a3d4793c55b729cc37e2ab0f6b2e6613&)
            - [11. Dinamica de CR.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384935529887432825/11._Dinamica_de_CR.pdf?ex=68543d39&is=6852ebb9&hm=29145f11d611c340a6ae32876bf7bbf44bf6d193c00d2e8e1f22036d18be4775&)
            - [12. Hidrostática.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384935528914223247/12._Hidrostatica.pdf?ex=68543d38&is=6852ebb8&hm=556766b941ac4bb44dfee5f1ea09296d59e74a2667ca0f0364bef67e8731aaf7&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_clase_huallpa1():
    embed = discord.Embed(
        title="Clases PDF's - PPT's Prof. Huallpa",
        description=textwrap.dedent(f"""\
            - [Presentación del curso 1.PNG](https://media.discordapp.net/attachments/1384359269570187284/1384948267678175333/Presentacion_de_curso_1.PNG?ex=68544916&is=6852f796&hm=e9017320b2d9a93fed3a1e14dac9fbcbbdda9df8ed363e577909b8acd824ed74&=&format=webp&quality=lossless&width=1423&height=859)
            - [Presentación del curso 2.PNG](https://media.discordapp.net/attachments/1384359269570187284/1384948267422584862/Presentacion_de_curso_2.PNG?ex=68544916&is=6852f796&hm=95a686ea4fe468b3c39ee8e024535351b42e15b83e7c9f87331ca3d7abb283f9&=&format=webp&quality=lossless&width=1304&height=859)
            - [Clase 1. Semana 1. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384943648373997679/Clase_1._Semana_1._Cuaderno_del_Profesor.pdf?ex=685444c8&is=6852f348&hm=faa4577d738049d367d9fa668f8136c3aa20445e4852f9d227658ceb0a88a39e&)
            - [Clase 2. Semana 1. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384943647987863632/Clase_2._Semana_1._Cuaderno_del_Profesor.pdf?ex=685444c8&is=6852f348&hm=7a40d66d90541c1dc88e8a524063b5a0addbae56ce9c3c4fac8a32bcf20e9233&)
            - [Sistema Legal de Unidades y Medidas del Perú.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384943647606177948/Sistema_Legal_de_Unidades_y_Medidas_del_Peru.pdf?ex=685444c8&is=6852f348&hm=e9277e20bbef8b0800fa2a8c7314b6c810a9eb44e769b8ec081ee540fbb65449&)
            - [1 INTRODUCCION FISICA 1.pptx](https://cdn.discordapp.com/attachments/1384359269570187284/1384943707744112752/1_INTRODUCCION_FISICA_1.pptx?ex=685444d6&is=6852f356&hm=9b58c157608b40400e5c0ca42f9ead9056ea1ead3d0ecdafe8ff6aa2ed45ba01&)
            - [2 Errores.pptx](https://cdn.discordapp.com/attachments/1384359269570187284/1384943707345911849/2_Errores.pptx?ex=685444d6&is=6852f356&hm=8dbca63a7e7ab3f3b87c99b52cda2c329d1db68e3618bfdb873737e769038ff3&)
            - [Clase 3. Semana 2. Cuaderno del profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384944457811624089/Clase_3._Semana_2._Cuaderno_del_profesor.pdf?ex=68544589&is=6852f409&hm=78bd5089d9a150e14f31f66e550b6103d9e6d4e9a8352be3d585fc5a2ea48b9d&)
            - [Clase 4. Semana 2. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384944457404780704/Clase_4._Semana_2._Cuaderno_del_Profesor.pdf?ex=68544589&is=6852f409&hm=7f988721643d25558a44b9aa9182b2f8e44eb8a05258dd72dcfa78726e77a1ad&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 1. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_clase_huallpa2():
    embed = discord.Embed(
        title="Clases PDF's - PPT's Prof. Huallpa",
        description=textwrap.dedent(f"""\
            - [Clase 5. Semana 2. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384944457027289229/Clase_5._Semana_2._Cuaderno_del_Profesor.pdf?ex=68544589&is=6852f409&hm=4b3d7279e3fd9a882b051610146a2cea7751ea8e147c4755e5e67fed6c5c7654&)
            - [Clase 6. Semana 3. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384945344428642475/Clase_6._Semana_3._Cuaderno_del_Profesor.pdf?ex=6854465d&is=6852f4dd&hm=0218061c354d6a294e2921163f47564b9a802bb28eca7f69670111a2fd96a1df&)
            - [Clase 7. Semana 3. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384945345028554792/Clase_7._Semana_3._Cuaderno_del_Profesor.pdf?ex=6854465d&is=6852f4dd&hm=26b2e79825c3f7cd903c818ddd783113aeb1cbf0d2d2453b9941d8bdd0809c14&)
            - [Clase Manuscrita 04-12-2020.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384945344739282974/Clase_Manuscrita_04-12-2020.pdf?ex=6854465d&is=6852f4dd&hm=73865052c3d5df79f68f3aece6428c3bf2ce76b253fe89e681428f302d2d2ba4&)
            - [Clase 8. Semana 4. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384945709454983280/Clase_8._Semana_4._Cuaderno_del_Profesor.pdf?ex=685446b4&is=6852f534&hm=dd4ecb68444379b45c169b307af0bbb3735b67f9bacc90c094b6f271969c8917&)
            - [Clase 9. Semana 4. Cuaderno del Profesor.pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384945710298038352/Clase_9._Semana_4._Cuaderno_del_Profesor.pdf?ex=685446b4&is=6852f534&hm=da9f3c14f009bc3b9c744dc1fc4c7399b62e2de63b6f164d0cd4953ddd6e32d9&)
            - [Clase manuscrita 11-12-2020 (Semana 4).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384945709840728186/Clase_manuscrita_11-12-2020.pdf?ex=685446b4&is=6852f534&hm=59a51f716e8e86b02577870448f144dc5eedfc6bac48e57897dcff3a50a89e46&)
            - [Clase manuscrita 18-12-2020 (Semana 5).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384946142386847805/Clase_manuscrita_18-12-2020.pdf?ex=6854471b&is=6852f59b&hm=fc7e003e91c8642631616a7aca0ad102cb27b81e4bd809a4c523d97f8c15122c&)
            - [Clase 25-12-2020 (Semana 6-7).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384946339665809549/Clase_25-12-2020.pdf?ex=6854474a&is=6852f5ca&hm=8beff9bcbefce3053707fe74843d12b7a16d060b831b2debad9291c4badf6ab5&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 2. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_clase_huallpa3():
    embed = discord.Embed(
        title="Clases PDF's - PPT's Prof. Huallpa",
        description=textwrap.dedent(f"""\
            - [Clase 15-01-2021 (Semana 9).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384946729564115025/Clase_15-01-2021.pdf?ex=685447a7&is=6852f627&hm=72a9d487aba25613610e6cfd94cbf4b4305f5ee7448cbad93d7e408a190b1dce&)
            - [Clase 22-01-2021 (Semana 10).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384947038889840764/Clase_22-01-2021.pdf?ex=685447f1&is=6852f671&hm=033f940939aaa1e2516465a4117a17f936e2683dfb61cc525abc585f01f3d8ee&)
            - [Clase 29-01-2021 (Semana 11).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384947413458092032/Clase_29-01-2021.pdf?ex=6854484a&is=6852f6ca&hm=f92baf336b24ba9e51c8fa14638662b57c2ff8211960c7ccdb79ca89718b3234&)
            - [Clase 05-02-21 (Semana 12).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384947413080346744/Clase_05-02-21.pdf?ex=6854484a&is=6852f6ca&hm=d1fc1568c752c5b07e2394697c92829901da307bd4580f56dcb8fc0aa70df7a7&)
            - [Clase 12-02-2021 (Semana 13).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384947412782809139/Clase_12-02-2021.pdf?ex=6854484a&is=6852f6ca&hm=657b4de44984845de46b0043cf83d2b38c684fedfa5907a660f9b6a5f64fa7b2&)
            - [CLASE 19-02-2021 (Semana 14).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384947412409389146/CLASE_19-02-2021.pdf?ex=6854484a&is=6852f6ca&hm=b33fbab398df9ce03bbaeda83bab36caa05065efb5e5f74ffb3284d29bf82104&)
            - [Clase B 19-02-2021 (Semana 14).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384947411788627978/Clase_B_19-02-2021.pdf?ex=6854484a&is=6852f6ca&hm=d12c53a127ff3670bd4a24c821b57f556e9d81cbd0367a9975856ed48e96cb1e&)
            - [Clase 26-02-2021 (Semana 15).pdf](https://cdn.discordapp.com/attachments/1384359269570187284/1384947410865881239/Clase_26-02-2021.pdf?ex=68544849&is=6852f6c9&hm=1fda4867c81de2d735e6f40ddf59b5ed98fe8b860bb8c2130632fd89cdf4a4ed&)
        """),
        color=0x701B13)
    embed.set_footer(text="Página 3. Gracias por usar FIEE-BOT.")
    embed.set_thumbnail(url="https://example.com/fisica_1_laboratorios_thumbnail.png")

    return embed

def get_embed_fisica_1_clase_huallpa():

    lista = []

    lista.append(get_embed_fisica_1_clase_huallpa1()) # [0]
    lista.append(get_embed_fisica_1_clase_huallpa2()) # [1]
    lista.append(get_embed_fisica_1_clase_huallpa3()) # [2]

    return lista


def get_embeds_fisica_1_clases():

    lista = []

    lista.append(get_embed_fisica_1_clase_caro())
    lista.append(get_embed_fisica_1_clase_huallpa1())
    
    return lista


def get_embeds_cursos_pcs_primer_ciclo():

    lista = []

    lista.append(get_embeds_fisica_1_pcs())
    lista.append(get_embeds_calc_diferencial_pcs())
    lista.append(get_embeds_algebra_lineal_pcs())
    lista.append(get_embeds_dibujo_tecnico_pcs())
    lista.append(get_embeds_intro_computacion_pcs())
    lista.append(get_embeds_fundamentos_programacion_pcs())

    return lista


def get_embeds_cursos_pcs_segundo_ciclo():

    lista = []

    lista.append(get_embeds_fisica_2_pcs())
    lista.append(get_embeds_calculo_integral_pcs())
    lista.append(get_embeds_algoritmos_1_pcs())
    lista.append(get_embeds_quimica_1_pcs())
    lista.append(get_embeds_fundamentos_computador_pcs())
    lista.append(get_embeds_redes_1_pcs())
    lista.append(get_embeds_sistemas_operativos_1_pcs())

    return lista

def get_embeds_cursos_pcs_tercer_ciclo():

    lista = []

    lista.append(get_embeds_fund_electricidad_magnetismo_pcs())
    lista.append(get_embeds_ecuaciones_diferenciales_pcs())
    lista.append(get_embeds_probabilidades_pcs())
    lista.append(get_embeds_poo_pcs())
    lista.append(get_embeds_economia_pcs())
    lista.append(get_embeds_redes_2_pcs())

    return lista

def get_embeds_cursos_pcs_cuarto_ciclo():

    lista = []

    lista.append(get_embeds_intro_moderna_pcs())
    lista.append(get_embeds_analisis_senales_pcs())
    lista.append(get_embeds_calculo_vectorial_pcs())
    lista.append(get_embeds_circuitos_1_pcs())
    lista.append(get_embeds_metodos_numericos_pcs())
    lista.append(get_embeds_etica_filosofia_pcs())
    lista.append(get_embeds_sistemas_operativos_2_pcs())

    return lista

def get_embeds_cursos_pcs_quinto_ciclo():

    lista = []

    lista.append(get_embeds_electromagnetismo_1_pcs())


    return lista


def get_pcs_embeds_todos_los_ciclos():

    lista_de_listas = []

    lista_de_listas.append(get_embeds_cursos_pcs_primer_ciclo())
    lista_de_listas.append(get_embeds_cursos_pcs_segundo_ciclo())
    lista_de_listas.append(get_embeds_cursos_pcs_tercer_ciclo())
    lista_de_listas.append(get_embeds_cursos_pcs_cuarto_ciclo())
    lista_de_listas.append(get_embeds_cursos_pcs_quinto_ciclo())

    return lista_de_listas



# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////


def get_embed_and_view_por_curso(ciclo_seleccionado, curso_seleccionado, lab_pc_clase, periodo_o_pc):

    view = PaginaAnteriorPCS_LABS(ciclo_seleccionado, curso_seleccionado, lab_pc_clase) # default


    if lab_pc_clase == 2: # PC y exámenes en general.

        if isinstance(get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][curso_seleccionado][periodo_o_pc], list):
            embed = get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][curso_seleccionado][periodo_o_pc][0]
            view = NavegarPaginas(get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][curso_seleccionado][periodo_o_pc], ciclo_seleccionado, curso_seleccionado, lab_pc_clase)
        else:
            embed = get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][curso_seleccionado][periodo_o_pc]


    if ciclo_seleccionado == 0:  # Primer ciclo
        if curso_seleccionado == 0: # Física 1
            if lab_pc_clase == 1:
                embed = get_embeds_fisica_1_labos()[periodo_o_pc]
                if periodo_o_pc == 3:
                    view = NavegarPaginas([get_embed_fisica_1_laboratorios_2023_I_pag1(), get_embed_fisica_1_laboratorios_2023_I_pag2()], ciclo_seleccionado, curso_seleccionado, lab_pc_clase)
            if lab_pc_clase == 3:
                embed = get_embeds_fisica_1_clases()[periodo_o_pc]
                if periodo_o_pc == 0:  # Clases del prof. Caro
                    view = NavegarPaginas([get_embed_fisica_1_clase_caro(), get_embed_fisica_1_clase_caro2()], ciclo_seleccionado, curso_seleccionado, lab_pc_clase)
                else:
                    view = NavegarPaginas(get_embed_fisica_1_clase_huallpa(), ciclo_seleccionado, curso_seleccionado, lab_pc_clase)


    return embed, view


# /////////////////////////////////////////////////////////////////////////////////////


def opciones_fisica_1_embeds():

    embeds = []

    embeds.append(get_fisica_1_laboratorios_embed())  # [0]
    embeds.append(get_fisica_1_examenes_embed())      # [1]
    embeds.append(get_fisica_1_clases_embed())        # [2]
    embeds.append(get_fisica_1_cuadernos_embed())     # [3]

    return embeds

def opciones_calc_diferencial_embeds():

    embeds = []

    embeds.append("get_calc_diferencial_laboratorios_embed()")  # [0]
    embeds.append(get_calc_diferencial_examenes_embed())  # [1]
    embeds.append(get_calc_diferencial_clases_embed())  # [2]
    embeds.append(get_calc_diferencial_cuadernos_embed())  # [3]

    return embeds

def opciones_algebra_lineal_embeds():
    embeds = []

    embeds.append("get_algebra_lineal_laboratorios_embed()")  # [0]
    embeds.append(get_algebra_lineal_examenes_embed())      # [1]
    embeds.append(get_algebra_lineal_clases_embed())        # [2]
    embeds.append(get_algebra_lineal_cuadernos_embed())     # [3]

    return embeds

def opciones_dibujo_tecnico_embeds():
    embeds = []

    embeds.append("get_dibujo_tecnico_laboratorios_embed()")  # [0]
    embeds.append(get_dibujo_tecnico_examenes_embed())      # [1]
    embeds.append(get_dibujo_tecnico_clases_embed())        # [2]
    embeds.append(get_dibujo_tecnico_cuadernos_embed())     # [3]

    return embeds

def opciones_intro_computacion_embeds():
    embeds = []

    embeds.append("get_intro_computacion_laboratorios_embed()")  # [0]
    embeds.append(get_intro_computacion_examenes_embed())      # [1]
    embeds.append(get_intro_computacion_clases_embed())        # [2]
    embeds.append(get_intro_computacion_cuadernos_embed())     # [3]

    return embeds

def opciones_realidad_nacional_embeds():
    embeds = []

    embeds.append("get_realidad_nacional_laboratorios_embed()")  # [0]
    embeds.append(get_realidad_nacional_examenes_embed())      # [1]
    embeds.append(get_realidad_nacional_clases_embed())        # [2]
    embeds.append(get_realidad_nacional_cuadernos_embed())     # [3]

    return embeds

def opciones_fundamentos_programacion_embeds():
    embeds = []

    embeds.append("get_fundamentos_programacion_laboratorios_embed()")  # [0]
    embeds.append(get_fundamentos_programacion_examenes_embed())      # [1]
    embeds.append(get_fundamentos_programacion_clases_embed())        # [2]
    embeds.append(get_fundamentos_programacion_cuadernos_embed())     # [3]

    return embeds

# /////////////////////////////////////////////////////////////////////////////////////


def opciones_fisica_2_embeds():
    embeds = []

    embeds.append("get_fisica_2_laboratorios_embed()")  # [0]
    embeds.append(get_fisica_2_examenes_embed())      # [1]
    embeds.append(get_fisica_2_clases_embed())        # [2]
    embeds.append(get_fisica_2_cuadernos_embed())     # [3]

    return embeds

def opciones_calculo_integral_embeds():
    embeds = []

    embeds.append("get_calculo_integral_laboratorios_embed()")  # [0]
    embeds.append(get_calculo_integral_examenes_embed())      # [1]
    embeds.append(get_calculo_integral_clases_embed())        # [2]
    embeds.append(get_calculo_integral_cuadernos_embed())     # [3]

    return embeds

def opciones_algoritmos_1_embeds():
    embeds = []

    embeds.append("get_algoritmos_1_laboratorios_embed()")  # [0]
    embeds.append(get_algoritmos_1_examenes_embed())      # [1]
    embeds.append(get_algoritmos_1_clases_embed())        # [2]
    embeds.append(get_algoritmos_1_cuadernos_embed())     # [3]

    return embeds

def opciones_fundamentos_computador_embeds():
    embeds = []

    embeds.append("get_fundamentos_computador_laboratorios_embed()")  # [0]
    embeds.append(get_fundamentos_computador_examenes_embed())      # [1]
    embeds.append(get_fundamentos_computador_clases_embed())        # [2]
    embeds.append(get_fundamentos_computador_cuadernos_embed())     # [3]

    return embeds

def opciones_quimica_1_embeds():
    embeds = []

    embeds.append("get_quimica_1_laboratorios_embed()")  # [0]
    embeds.append(get_quimica_1_examenes_embed())      # [1]
    embeds.append(get_quimica_1_clases_embed())        # [2]
    embeds.append(get_quimica_1_cuadernos_embed())     # [3]
    return embeds

def opciones_redes_1_embeds():
    embeds = []

    embeds.append("get_redes_1_laboratorios_embed()")  # [0]
    embeds.append(get_redes_1_examenes_embed())      # [1]
    embeds.append(get_redes_1_clases_embed())        # [2]
    embeds.append(get_redes_1_cuadernos_embed())     # [3]

    return embeds

def opciones_redaccion_embeds():
    embeds = []

    embeds.append("get_redaccion_laboratorios_embed()")  # [0]
    embeds.append(get_redaccion_examenes_embed())      # [1]
    embeds.append(get_redaccion_clases_embed())        # [2]
    embeds.append(get_redaccion_cuadernos_embed())     # [3]

    return embeds

# /////////////////////////////////////////////////////////////////////////////////////


def opciones_fundamentos_electricidad_magnetismo_embeds():
    embeds = []

    embeds.append("get_fundamentos_electricidad_magnetismo_laboratorios_embed()")  # [0]
    embeds.append(get_fundamentos_electricidad_magnetismo_examenes_embed())      # [1]
    embeds.append(get_fundamentos_electricidad_magnetismo_clases_embed())        # [2]
    embeds.append(get_fundamentos_electricidad_magnetismo_cuadernos_embed())     # [3]

    return embeds

def opciones_ecuaciones_diferenciales_embeds():
    embeds = []

    embeds.append("get_ecuaciones_diferenciales_laboratorios_embed()")  # [0]
    embeds.append(get_ecuaciones_diferenciales_examenes_embed())      # [1]
    embeds.append(get_ecuaciones_diferenciales_clases_embed())        # [2]
    embeds.append(get_ecuaciones_diferenciales_cuadernos_embed())     # [3]

    return embeds


def opciones_probabilidades_embeds():
    embeds = []

    embeds.append("get_probabilidades_laboratorios_embed()")  # [0]
    embeds.append(get_probabilidades_examenes_embed())      # [1]
    embeds.append(get_probabilidades_clases_embed())        # [2]
    embeds.append(get_probabilidades_cuadernos_embed())     # [3]

    return embeds

def opciones_poo_embeds():
    embeds = []

    embeds.append("get_poo_laboratorios_embed()")  # [0]
    embeds.append(get_poo_examenes_embed())      # [1]
    embeds.append(get_poo_clases_embed())        # [2]
    embeds.append(get_poo_cuadernos_embed())     # [3]

    return embeds

def opciones_economia_embeds():
    embeds = []

    embeds.append("get_economia_laboratorios_embed()")  # [0]
    embeds.append(get_economia_examenes_embed())      # [1]
    embeds.append(get_economia_clases_embed())        # [2]
    embeds.append(get_economia_cuadernos_embed())     # [3]

    return embeds

def opciones_redes_2_embeds():
    embeds = []

    embeds.append("get_redes_2_laboratorios_embed()")  # [0]
    embeds.append(get_redes_2_examenes_embed())      # [1]
    embeds.append(get_redes_2_clases_embed())        # [2]
    embeds.append(get_redes_2_cuadernos_embed())     # [3]

    return embeds

# //////////////////////////////////////////////////////////////////

def opciones_electrotecnia_embeds():
    embeds = []

    embeds.append("get_electrotecnia_laboratorios_embed()")  # [0]
    embeds.append(get_electrotecnia_examenes_embed())      # [1]
    embeds.append(get_electrotecnia_clases_embed())        # [2]
    embeds.append(get_electrotecnia_cuadernos_embed())     # [3]

    return embeds

def opciones_intro_moderna_embeds():
    embeds = []

    embeds.append("get_intro_moderna_laboratorios_embed()")  # [0]
    embeds.append(get_intro_moderna_examenes_embed())      # [1]
    embeds.append(get_intro_moderna_clases_embed())        # [2]
    embeds.append(get_intro_moderna_cuadernos_embed())     # [3]

    return embeds

def opciones_analisis_senales_embeds():
    embeds = []

    embeds.append("get_analisis_senales_laboratorios_embed()")  # [0]
    embeds.append(get_analisis_senales_examenes_embed())      # [1]
    embeds.append(get_analisis_senales_clases_embed())        # [2]
    embeds.append(get_analisis_senales_cuadernos_embed())     # [3]

    return embeds

def opciones_calculo_vectorial_embeds():
    embeds = []

    embeds.append("get_calculo_vectorial_laboratorios_embed()")  # [0]
    embeds.append(get_calc_vectorial_examenes_embed())      # [1]
    embeds.append(get_calc_vectorial_clases_embed())        # [2]
    embeds.append(get_calculo_vectorial_cuadernos_embed())     # [3]

    return embeds

def opciones_circuitos_1_embeds():
    embeds = []

    embeds.append("get_circuitos_1_laboratorios_embed()")  # [0]
    embeds.append(get_circuitos_1_examenes_embed())      # [1]
    embeds.append(get_circuitos_1_clases_embed())        # [2]
    embeds.append(get_circuitos_1_cuadernos_embed())     # [3]

    return embeds

def opciones_etica_filosofia_embeds():
    embeds = []

    embeds.append("get_etica_filosofia_laboratorios_embed()")  # [0]
    embeds.append(get_etica_filosofia_examenes_embed())      # [1]
    embeds.append(get_etica_filosofia_clases_embed())        # [2]
    embeds.append(get_etica_filosofia_cuadernos_embed())     # [3]

    return embeds

def opciones_operativos_2_embeds():
    embeds = []

    embeds.append("get_operativos_2_laboratorios_embed()")  # [0]
    embeds.append(get_operativos_2_examenes_embed())      # [1]
    embeds.append(get_operativos_2_clases_embed())        # [2]
    embeds.append(get_operativos_2_cuadernos_embed())     # [3]

    return embeds

def opciones_metodos_numericos_embeds():
    embeds = []

    embeds.append("get_metodos_numericos_laboratorios_embed()")  # [0]
    embeds.append(get_metodos_numericos_examenes_embed())      # [1]
    embeds.append(get_metodos_numericos_clases_embed())        # [2]
    embeds.append(get_metodos_numericos_cuadernos_embed())     # [3]

    return embeds


# /////////////////////////////////////////////////////////////////////////////////////



def opciones_electromagnetismo_1_embeds():
    embeds = []

    embeds.append("get_electromagnetismo_1_laboratorios_embed()")  # [0]
    embeds.append(get_electromagnetismo_1_examenes_embed())      # [1]
    embeds.append(get_electromagnetismo_1_clases_embed())        # [2]
    embeds.append(get_electromagnetismo_1_cuadernos_embed())     # [3]

    return embeds



# /////////////////////////////////////////////////////////////////////////////////////


def get_opciones_primer_ciclo_embeds():

    embeds = []

    embeds.append(opciones_fisica_1_embeds())  # [0]
    embeds.append(opciones_calc_diferencial_embeds())  # [1]
    embeds.append(opciones_algebra_lineal_embeds())  # [2]
    embeds.append(opciones_dibujo_tecnico_embeds())  # [3]
    embeds.append(opciones_intro_computacion_embeds())  # [4]
    embeds.append(opciones_realidad_nacional_embeds())  # [1]
    embeds.append(opciones_fundamentos_programacion_embeds())  # [6]

    return embeds


def get_opciones_segundo_ciclo_embeds():
    embeds = []

    embeds.append(opciones_fisica_2_embeds())  # [0]
    embeds.append(opciones_calculo_integral_embeds())  # [2]
    embeds.append(opciones_algoritmos_1_embeds())  # [1]
    embeds.append(opciones_fundamentos_computador_embeds())  # [3]
    embeds.append(opciones_quimica_1_embeds())  # [4]
    embeds.append(opciones_redes_1_embeds())  # [1]
    embeds.append(opciones_redaccion_embeds())  # [6]

    return embeds

def get_opciones_tercer_ciclo_embeds():
    embeds = []

    embeds.append(opciones_fundamentos_electricidad_magnetismo_embeds())
    embeds.append(opciones_ecuaciones_diferenciales_embeds())
    embeds.append(opciones_probabilidades_embeds())
    embeds.append(opciones_poo_embeds())
    embeds.append(opciones_economia_embeds())
    embeds.append(opciones_redes_2_embeds())

    return embeds


def get_opciones_cuarto_ciclo_embeds():
    embeds = []

    embeds.append(opciones_intro_moderna_embeds())
    embeds.append(opciones_analisis_senales_embeds())
    embeds.append(opciones_calculo_vectorial_embeds())
    embeds.append(opciones_circuitos_1_embeds())
    embeds.append(opciones_metodos_numericos_embeds())
    embeds.append(opciones_etica_filosofia_embeds())
    embeds.append(opciones_operativos_2_embeds())

    return embeds


def get_opciones_todos_los_ciclos_embeds():

    embeds = []

    embeds.append(get_opciones_primer_ciclo_embeds())  # [0]
    embeds.append(get_opciones_segundo_ciclo_embeds())  # [1]
    embeds.append(get_opciones_tercer_ciclo_embeds())
    embeds.append(get_opciones_cuarto_ciclo_embeds())

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
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones

def despliegue_lista_opciones_LAB_NO_CUADERNO():

    opciones = []

    opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones

def despliegue_lista_opciones_NO_LAB():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones

def despliegue_lista_opciones_NO_LAB_NO_PC():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    # opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones

def despliegue_lista_opciones_NO_LAB_NO_PC_NO_CUADERNO():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    # opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

def despliegue_lista_opciones_NO_LAB_NO_PC_NO_CLASE():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    # opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    # opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones
def despliegue_lista_opciones_NO_LAB_NO_CUADERNO():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones



def despliegue_lista_4PCS():

    opciones = []

    opciones.append(discord.SelectOption(label="PC-1", value=1))
    opciones.append(discord.SelectOption(label="PC-2", value=2))
    opciones.append(discord.SelectOption(label="PC-3", value=3))
    opciones.append(discord.SelectOption(label="PC-4", value=4))
    opciones.append(discord.SelectOption(label="Ex. Parcial", value=6))
    opciones.append(discord.SelectOption(label="Ex. Final", value=7))
    opciones.append(discord.SelectOption(label="Ex. Sustitutorio", value=8))
    opciones.append(discord.SelectOption(label="Prueba de entrada", value=9))

    return opciones

def despliegue_lista_5PCS():

    opciones = []

    opciones.append(discord.SelectOption(label="PC-1", value=1))
    opciones.append(discord.SelectOption(label="PC-2", value=2))
    opciones.append(discord.SelectOption(label="PC-3", value=3))
    opciones.append(discord.SelectOption(label="PC-4", value=4))
    opciones.append(discord.SelectOption(label="PC-5", value=5))
    opciones.append(discord.SelectOption(label="Ex. Parcial", value=6))
    opciones.append(discord.SelectOption(label="Ex. Final", value=7))
    opciones.append(discord.SelectOption(label="Ex. Sustitutorio", value=8))
    opciones.append(discord.SelectOption(label="Prueba de entrada", value=9))

    return opciones

def despliegue_lista_4PCS_NO_EXAMEN():

    opciones = []

    opciones.append(discord.SelectOption(label="PC-1", value=1))
    opciones.append(discord.SelectOption(label="PC-2", value=2))
    opciones.append(discord.SelectOption(label="PC-3", value=3))
    opciones.append(discord.SelectOption(label="PC-4", value=4))
    # opciones.append(discord.SelectOption(label="Prueba de entrada", value=8))

    return opciones

def despliegue_lista_5PCS_NO_EXAMEN():

    opciones = []

    opciones.append(discord.SelectOption(label="PC-1", value=1))
    opciones.append(discord.SelectOption(label="PC-2", value=2))
    opciones.append(discord.SelectOption(label="PC-3", value=3))
    opciones.append(discord.SelectOption(label="PC-4", value=4))
    opciones.append(discord.SelectOption(label="PC-5", value=5))
    # opciones.append(discord.SelectOption(label="Prueba de entrada", value=8))

    return opciones




def despliegue_lista_LABS_fisica_1():

    opciones = []

    opciones.append(discord.SelectOption(label="Laboratorios 2019-II", value=1))
    opciones.append(discord.SelectOption(label="Laboratorios 2020-II", value=2))
    opciones.append(discord.SelectOption(label="Laboratorios 2021-II", value=3))
    opciones.append(discord.SelectOption(label="Laboratorios 2023-I", value=4))

    return opciones

def despliegue_lista_CLASES_fisica_1():

    opciones = []

    opciones.append(discord.SelectOption(label="Clases PDF's Prof. Caro", value=1))
    opciones.append(discord.SelectOption(label="Clases PDF's 2020-I-II Prof. Huallpa", value=2))

    return opciones


def despliegue_lista_PCS_LABS_CLASES(ciclo_seleccionado, curso_seleccionado, opcion_elegida):

    if ciclo_seleccionado == 0: # Primer ciclo
        if curso_seleccionado == 0: # Física 1
            despliegue_lista_pcs = despliegue_lista_4PCS()
            despliegue_lista_labs = despliegue_lista_LABS_fisica_1()
            despliegue_lista_clases = despliegue_lista_CLASES_fisica_1()
        if curso_seleccionado == 1: # Cálculo diferencial
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # Álgebra lineal
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: #  Dibujo técnico
            despliegue_lista_pcs = despliegue_lista_5PCS_NO_EXAMEN()
        if curso_seleccionado == 4: # Introducción a la computación
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 5: #  Realidad Nac. Constitución y DD.HH
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 6: # Fundamentos de programación
            despliegue_lista_pcs = despliegue_lista_5PCS_NO_EXAMEN()
    if ciclo_seleccionado == 1: # Segundo ciclo
        if curso_seleccionado == 0: # Física 2
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1: # Cálculo integral
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # Algoritmos y estructuras de datos I
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 3: # Fundamentos de ingeniería del computador
            despliegue_lista_pcs = despliegue_lista_5PCS_NO_EXAMEN()
        if curso_seleccionado == 4: # Química
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 5: # Redes de datos I
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 6: # Redacción y comunicación
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # Sistemas operativos I
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    if ciclo_seleccionado == 2: # Tercer ciclo
        if curso_seleccionado == 0: # Fundamentos de Electricidad y Magnetismo
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1: # Ecuaciones diferenciales
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # Probabilidades y estadística
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 3: # Programación orientada a objetos
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 4: # Economía general
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 5: # Redes de datos II
            despliegue_lista_pcs = despliegue_lista_4PCS()
    if ciclo_seleccionado == 3: # Cuarto ciclo
        if curso_seleccionado == 0: # Introducción a la física moderna
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1: # Análisis de señales y sistemas
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # Cálculo vectorial
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: # Métodos numéricos
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 4: # Circuitos eléctricos I
            despliegue_lista_pcs = despliegue_lista_4PCS() # -------------------- DUDA xd ----------------
        if curso_seleccionado == 5: # Electrotecnia e instalación de redes
            despliegue_lista_pcs = despliegue_lista_4PCS() # -------------------- otra duda --------------
        if curso_seleccionado == 6: # Ética y filosofía
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # Sistemas operativos II
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    if ciclo_seleccionado == 4: 
        if curso_seleccionado == 0: 
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1:
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # 
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: #  
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 4: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() # 
        if curso_seleccionado == 5: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() #
        if curso_seleccionado == 6: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    if ciclo_seleccionado == 5: 
        if curso_seleccionado == 0: 
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1:
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # 
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: #  
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 4: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() # 
        if curso_seleccionado == 5: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() #
        if curso_seleccionado == 6: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    if ciclo_seleccionado == 6: 
        if curso_seleccionado == 0: 
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1:
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # 
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: #  
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 4: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() # 
        if curso_seleccionado == 5: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() #
        if curso_seleccionado == 6: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    if ciclo_seleccionado == 7: 
        if curso_seleccionado == 0: 
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1:
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # 
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: #  
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 4: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() # 
        if curso_seleccionado == 5: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() #
        if curso_seleccionado == 6: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    if ciclo_seleccionado == 8: 
        if curso_seleccionado == 0: 
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1:
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # 
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: #  
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 4: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() # 
        if curso_seleccionado == 5: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() #
        if curso_seleccionado == 6: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    if ciclo_seleccionado == 9: # Electivos
        if curso_seleccionado == 0: 
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 1:
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 2: # 
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 3: #  
            despliegue_lista_pcs = despliegue_lista_5PCS()
        if curso_seleccionado == 4: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() # 
        if curso_seleccionado == 5: # 
            despliegue_lista_pcs = despliegue_lista_4PCS() #
        if curso_seleccionado == 6: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 7: # 
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
    

    if opcion_elegida == 1:
        devolver = despliegue_lista_labs
    if opcion_elegida == 2:
        devolver = despliegue_lista_pcs
    if opcion_elegida == 3:
        devolver = despliegue_lista_clases

    return devolver





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
    
    @discord.ui.button(label="↩️ Regresar", style=discord.ButtonStyle.secondary)
    async def volver(self, interaction: discord.Interaction, button: discord.ui.Button):

        view = NumeroMenuCiclo()
        embed = get_ciclos_embeds()

        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(embed=embed, view=view)


class NumeroMenuOpcionesCurso(discord.ui.View):

    def __init__(self, ciclo_seleccionado, curso_seleccionado):
        super().__init__()

        self.ciclo_seleccionado = ciclo_seleccionado
        self.curso_seleccionado = curso_seleccionado

        if ciclo_seleccionado == 0:  # Primer ciclo

            if curso_seleccionado == 0: # Física 1
                opciones = despliegue_lista_opciones_LAB()

            if curso_seleccionado == 1: # Cálculo diferencial
                opciones = despliegue_lista_opciones_NO_LAB()

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
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()

            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()
            

        if ciclo_seleccionado == 2:  # Tercer ciclo
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()

        if ciclo_seleccionado == 3:  # Cuarto ciclo
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()

        if ciclo_seleccionado == 4:  # Quinto ciclo
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()

        if ciclo_seleccionado == 5:  # Sexto ciclo
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()

        if ciclo_seleccionado == 6:  # Séptimo ciclo
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()

        if ciclo_seleccionado == 7:  # Octavo ciclo
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()

        if ciclo_seleccionado == 8:  # Noveno ciclo
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()

        if ciclo_seleccionado == 9:  # Cursos electivos
            if curso_seleccionado == 0: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 1: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 2: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 3: 
                opciones = despliegue_lista_opciones_NO_LAB_NO_CUADERNO()

            if curso_seleccionado == 4: 
                opciones = despliegue_lista_opciones_NO_LAB()

            if curso_seleccionado == 6:
                opciones = despliegue_lista_opciones_LAB()
                
            if curso_seleccionado == 7:
                opciones = despliegue_lista_opciones_NO_LAB()
            
        
        self.select = discord.ui.Select(
            placeholder="Selecciona una opción.",
            min_values=1,
            max_values=1,
            options=opciones,
        )

        self.select.callback = self.select_callback
        self.add_item(self.select)


    async def select_callback(self, interaction: discord.Interaction):
    
        opcion_elegida = int(self.select.values[0])

        if opcion_elegida == 1: # Laboratorios
            view =  NumeroMenuPCS_LABS_CLASES(self.ciclo_seleccionado, self.curso_seleccionado, opcion_elegida)

        if opcion_elegida == 2:  # Prácticas y exámenes
            view =  NumeroMenuPCS_LABS_CLASES(self.ciclo_seleccionado, self.curso_seleccionado, opcion_elegida)
        
        if opcion_elegida == 3:  # Clases
            view =  NumeroMenuPCS_LABS_CLASES(self.ciclo_seleccionado, self.curso_seleccionado, opcion_elegida)

        if opcion_elegida == 4:  # Cuadernos y libros
            view =  PaginaAnterior(self.ciclo_seleccionado, self.curso_seleccionado)

        embed =  get_opciones_todos_los_ciclos_embeds()[self.ciclo_seleccionado][self.curso_seleccionado][opcion_elegida-1]
        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(view=view, embed=embed)

    @discord.ui.button(label="↩️ Regresar", style=discord.ButtonStyle.secondary)
    async def volver(self, interaction: discord.Interaction, button: discord.ui.Button):

        view = NumeroMenuTodosLosCiclos(self.ciclo_seleccionado)
        embed = get_ciclos_cursos_embeds()[self.ciclo_seleccionado]

        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(embed=embed, view=view)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


class NumeroMenuPCS_LABS_CLASES(discord.ui.View):

    def __init__(self, ciclo_seleccionado, curso_seleccionado, opcion):
        super().__init__()

        self.ciclo_seleccionado = ciclo_seleccionado
        self.curso_seleccionado = curso_seleccionado
        self.opcion = opcion

        opciones = despliegue_lista_PCS_LABS_CLASES(self.ciclo_seleccionado, self.curso_seleccionado, self.opcion)

        if self.opcion == 1:  # Laboratorios
            texto_lista = "Selecciona un periodo."
        if self.opcion == 2:  # Prácticas y exámenes
            texto_lista = "Selecciona una PC o examen."
        if self.opcion == 3: # Clases
            texto_lista = "Selecciona una opción."

        self.select = discord.ui.Select(
            placeholder=texto_lista,
            min_values=1,
            max_values=1,
            options=opciones,
        )

        self.select.callback = self.select_callback
        self.add_item(self.select)

    
    async def select_callback(self, interaction: discord.Interaction):
        
        periodo_o_pc = int(self.select.values[0]) - 1

        embed, view = get_embed_and_view_por_curso(self.ciclo_seleccionado, self.curso_seleccionado, self.opcion, periodo_o_pc)
        
        # embed.set_footer(text="Gracias por usar FIEE-BOT.")
        # embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(view=view, embed=embed)
    

    @discord.ui.button(label="↩️ Regresar", style=discord.ButtonStyle.secondary)
    async def volver(self, interaction: discord.Interaction, button: discord.ui.Button):

        view = NumeroMenuOpcionesCurso(self.ciclo_seleccionado, self.curso_seleccionado)
        embed = get_lista_cursos_suprema_embeds()[self.ciclo_seleccionado][self.curso_seleccionado]

        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(embed=embed, view=view)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


class NavegarPaginas(discord.ui.View):
    def __init__(self, embeds: list[discord.Embed], ciclo_seleccionado, curso_seleccionado, opcion):
        super().__init__()
        self.ciclo_seleccionado = ciclo_seleccionado
        self.curso_seleccionado = curso_seleccionado
        self.opcion = opcion
        self.embeds = embeds
        self.pagina_actual = 0

    async def update_message(self, interaction: discord.Interaction):
        # Deshabilita el botón "anterior" si estamos en la primera página
        self.anterior.disabled = self.pagina_actual == 0
        # Deshabilita el botón "siguiente" si estamos en la última página
        self.siguiente.disabled = self.pagina_actual == len(self.embeds) - 1

        await interaction.response.edit_message(embed=self.embeds[self.pagina_actual], view=self)

    @discord.ui.button(label="← Anterior", style=discord.ButtonStyle.secondary, disabled=True)
    async def anterior(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.pagina_actual -= 1
        await self.update_message(interaction)

    @discord.ui.button(label="Siguiente →", style=discord.ButtonStyle.primary)
    async def siguiente(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.pagina_actual += 1
        await self.update_message(interaction)

    @discord.ui.button(label="↩️ Regresar", style=discord.ButtonStyle.secondary)
    async def volver(self, interaction: discord.Interaction, button: discord.ui.Button):

        view = NumeroMenuPCS_LABS_CLASES(self.ciclo_seleccionado, self.curso_seleccionado, self.opcion)

        embed = get_opciones_todos_los_ciclos_embeds()[self.ciclo_seleccionado][self.curso_seleccionado][self.opcion-1]
        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(embed=embed, view=view)


class PaginaAnterior(discord.ui.View):
    def __init__(self, ciclo_seleccionado, curso_seleccionado):
        super().__init__()

        self.ciclo_seleccionado = ciclo_seleccionado
        self.curso_seleccionado = curso_seleccionado

    @discord.ui.button(label="↩️ Regresar", style=discord.ButtonStyle.secondary)
    async def volver(self, interaction: discord.Interaction, button: discord.ui.Button):

        view = NumeroMenuOpcionesCurso(self.ciclo_seleccionado, self.curso_seleccionado)
        embed = get_lista_cursos_suprema_embeds()[self.ciclo_seleccionado][self.curso_seleccionado]

        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(embed=embed, view=view)


class PaginaAnteriorPCS_LABS(discord.ui.View):
    def __init__(self, ciclo_seleccionado, curso_seleccionado, opcion):
        super().__init__()

        self.ciclo_seleccionado = ciclo_seleccionado
        self.curso_seleccionado = curso_seleccionado
        self.opcion = opcion

    @discord.ui.button(label="↩️ Regresar", style=discord.ButtonStyle.secondary)
    async def volver(self, interaction: discord.Interaction, button: discord.ui.Button):

        view = NumeroMenuPCS_LABS_CLASES(self.ciclo_seleccionado, self.curso_seleccionado, self.opcion)

        embed =  get_opciones_todos_los_ciclos_embeds()[self.ciclo_seleccionado][self.curso_seleccionado][self.opcion-1]
        embed.set_footer(text="Gracias por usar FIEE-BOT.")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

        await interaction.response.edit_message(embed=embed, view=view)


# ///////////////////////////////////////////////////////////////////////////////////////////



# ///////////////////////////////////////////////////////////////////////////////////////////

bot.run("MTM3OTg5MDYyMjQ1Nzk3NDc5NA.G6HXNR.ig6eSs1pb0nKKCaxDoAN46UES8-xrIhF-MxNNA")
