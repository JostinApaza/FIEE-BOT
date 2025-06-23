import discord # Importa el módulo principal "discord" de la librería discord.py
from discord.ext import commands # Importa el submódulo "commands" desde el submódulo de extensiones discord.ext, que facilita crear comandos para el bot
import textwrap
from first_and_second_pages import get_ciclos_embeds, get_ciclos_cursos_embeds
from third_pages import get_lista_cursos_suprema_embeds
from help_embed import get_ayuda_embed
from first_and_second_lists import despliegue_lista_ciclos, despliegue_lista_cursos
from third_lists import devolver_terceras_listas
from fourth_pages import get_opciones_todos_los_ciclos_embeds
from fifth_pages_primer_ciclo import get_embeds_cursos_labs_pcs_clases_primer_ciclo
from fifth_pages_segundo_ciclo import get_embeds_cursos_labs_pcs_clases_segundo_ciclo
from fifth_pages_tercer_ciclo import get_embeds_cursos_labs_pcs_clases_tercer_ciclo
from fifth_pages_cuarto_ciclo import get_embeds_cursos_labs_pcs_clases_cuarto_ciclo

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

def get_embeds_cursos_pcs_quinto_ciclo():

    lista = []

    lista.append(get_embeds_electromagnetismo_1_pcs())


    return lista

def get_pcs_embeds_todos_los_ciclos():

    lista_de_listas = []

    lista_de_listas.append(get_embeds_cursos_labs_pcs_clases_primer_ciclo())
    lista_de_listas.append(get_embeds_cursos_labs_pcs_clases_segundo_ciclo())
    lista_de_listas.append(get_embeds_cursos_labs_pcs_clases_tercer_ciclo())
    lista_de_listas.append(get_embeds_cursos_labs_pcs_clases_cuarto_ciclo())
    lista_de_listas.append(get_embeds_cursos_pcs_quinto_ciclo())

    return lista_de_listas



# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////


def get_embed_and_view_por_curso(ciclo_seleccionado, curso_seleccionado, lab_pc_clase, periodo_o_pc):

    view = PaginaAnteriorPCS_LABS(ciclo_seleccionado, curso_seleccionado, lab_pc_clase) # default

    if isinstance(get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][lab_pc_clase-1][curso_seleccionado][periodo_o_pc], list):
        embed = get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][lab_pc_clase-1][curso_seleccionado][periodo_o_pc][0]
        view = NavegarPaginas(get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][lab_pc_clase-1][curso_seleccionado][periodo_o_pc], ciclo_seleccionado, curso_seleccionado, lab_pc_clase)
    else:
        embed = get_pcs_embeds_todos_los_ciclos()[ciclo_seleccionado][lab_pc_clase-1][curso_seleccionado][periodo_o_pc]
    

    return embed, view


# ////////////////////////////////////////////////////////////////////////
# /////////////////////                            ///////////////////////
# /////////////////////       FUNCIONES DE         ///////////////////////
# /////////////////////    LISTAS DESPLEGABLES     ///////////////////////
# /////////////////////                            ///////////////////////
# ////////////////////////////////////////////////////////////////////////



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
    opciones.append(discord.SelectOption(label="Prueba de entrada", value=9))

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
        if curso_seleccionado == 3: # Química
            despliegue_lista_pcs = despliegue_lista_4PCS()
        if curso_seleccionado == 4: # Fundamentos de ingeniería del computador
            despliegue_lista_pcs = despliegue_lista_5PCS_NO_EXAMEN()
        if curso_seleccionado == 5: # Redacción y comunicación
            despliegue_lista_pcs = despliegue_lista_4PCS_NO_EXAMEN()
        if curso_seleccionado == 6: # Redes de datos I
            despliegue_lista_pcs = despliegue_lista_4PCS()
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


# ///////////////////////////////////////////////////////////////////////////////////////////

async def show_help(ctx_or_interaction):

    embed = get_ayuda_embed(prefix)

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

        opciones = devolver_terceras_listas(self.ciclo_seleccionado, self.curso_seleccionado)
        
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

bot.run("MTM3OTg5MDYyMjQ1Nzk3NDc5NA.GImQaj.DtnWgE3UF2m9wyTtqBeWGchyCRfROuHbD2pofM")
