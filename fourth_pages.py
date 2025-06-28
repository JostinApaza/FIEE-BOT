import discord
import textwrap

def get_fisica_1_laboratorios_embed():

    embed = discord.Embed(
        title="Laboratorios de Física I",
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

def get_quimica_1_laboratorios_embed():

    embed = discord.Embed(
        title="Laboratorios de Química I",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el periodo.\n
            - Test de laboratorios 2021-II
        """),
        color=0x701B13)
    embed.add_field(name="▸  Guía de Laboratorio de Química 23-1", value="[Guia de Laboratorio de Quimica 23-1.pdf](https://drive.google.com/file/d/1IBXxo0x2exb5xbcizQ1rCsCkFG-PvwW5/view?usp=drive_link)", inline=False)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed


def get_fisica_1_clases_embed():

    embed = discord.Embed(
        title="Clases de Física I",
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
        title="Practicas y exámenes de Física I",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fisica_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Física I",
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
        title="Clases de Cálculo Diferencial.",
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
        title="Practicas y exámenes de Cálculo Diferencial:",
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

def get_calc_diferencial_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Cálculo Diferencial",
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
        title="Practicas y exámenes de Álgebra Lineal:",
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
        title="Practicas y exámenes de Dibujo técnico:",
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
        title="Practicas y exámenes de Introducción a la computación:",
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
        title="Practicas y exámenes de Realidad Nac. Const. y DD.HH:",
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
        title="Practicas y exámenes de Fundamentos de programación:",
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
            - 
            - 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed
def get_fisica_2_examenes_embed():


    embed = discord.Embed(
        title="Practicas y exámenes de Fund. de Ing. térmica y de fluidos:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
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
        title="Clases de Cálculo Integral.",
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
        title="Practicas y exámenes de Cálculo Integral:",
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

def get_calculo_integral_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Cálculo Integral:",
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
        title="Clases de Algoritmos y Estructuras de Datos I.",
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
        title="Practicas y exámenes de Algoritmos y Estructuras de Datos I:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_algoritmos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Algoritmos y Estructuras de Datos I:",
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
        title="Clases de Química.",
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
        title="Practicas y exámenes de Química:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_quimica_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Química:",
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
        title="Clases de Fund. de Ing. del computador.",
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
        title="Practicas y exámenes de Fund. de Ing. del computador:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - PC 1
            - PC 2
            - PC 3
            - PC 4
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_computador_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Fund. de Ing. del computador:",
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
        title="Practicas y exámenes de Redacción y comunicación:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_redaccion_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Redacción y comunicación:",
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
        title="Clases de Redes de Datos I.",
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
        title="Practicas y exámenes de Redes de Datos I:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
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
        title="Practicas y exámenes de Sistemas Operativos I:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - PC 1
            - PC 2
            - PC 3
            - PC 4
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_operativos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Sistemas Operativos I:",
        description=textwrap.dedent(f"""\
            \n
            - [Sistemas operativos 1.pdf](https://drive.google.com/file/d/1w_a106iLivyMDykHIlhjRL6q7D7TXmvS/view?usp=drive_link)
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

# /////////////////////////////////////////////////////////////////////////////////////

def get_fundamentos_electricidad_magnetismo_clases_embed():

    embed = discord.Embed(
        title="Clases de Fund. de Electricidad y Magnetismo",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - -
            - -
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_electricidad_magnetismo_laboratorios_embed():


    embed = discord.Embed(
        title="Practicas y exámenes de Fund. de Electricidad y Magnetismo:",
        description=textwrap.dedent(f"""\
            Selecciona un periodo de la lista.\n
            - Laboratorios 2021-II (Prof. Waters) 
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_electricidad_magnetismo_examenes_embed():


    embed = discord.Embed(
        title="Practicas y exámenes de Fund. de Electricidad y Magnetismo:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_fundamentos_electricidad_magnetismo_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Fund. de Electricidad y Magnetismo",
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
        title="Clases de Ecuaciones Diferenciales",
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
        title="Practicas y exámenes de Ecuaciones Diferenciales:",
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

def get_ecuaciones_diferenciales_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Ecuaciones Diferenciales",
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
        title="Clases de Programación Orientada a Objetos.",
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
        title="Practicas y exámenes de Programación Orientada a Objetos:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
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
        title="Clases de Economía General",
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
        title="Practicas y exámenes de Economía General:",
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

def get_economia_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Economía General:",
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
        title="Clases de Probabilidades y Estadística.",
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
        title="Practicas y exámenes de Probabilidades y Estadística:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_probabilidades_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Probabilidades y Estadística:",
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
        title="Clases de Redes de Datos II.",
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
        title="Practicas y exámenes de Redes de Datos II:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
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
        title="Cuadernos y libros de Redes de Datos II:",
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
        title="Clases de Intr. a la Física Moderna.",
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
        title="Practicas y exámenes de Intr. a la Física Moderna:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_intro_moderna_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Intr. a la Física Moderna:",
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
        title="Clases de Circuitos Eléctricos I.",
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
        title="Practicas y exámenes de Circuitos Eléctricos I:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_circuitos_1_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Circuitos Eléctricos I:",
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
        title="Clases de Cálculo Vectorial.",
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
        title="Practicas y exámenes de Cálculo Vectorial:",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista.\n
            - Prueba de entrada
            - PC 1
            - PC 2
            - PC 3
            - PC 4
            - Examen Parcial
            - Examen Final
            - Examen Sustitutorio
        """),
        color=0x701B13)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")

    return embed

def get_calculo_vectorial_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Cálculo Vectorial:",
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
        title="Clases de Análisis de Señales y Sistemas.",
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
        title="Practicas y exámenes de Análisis de Señales y Sistemas:",
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

def get_analisis_senales_cuadernos_embed():

    embed = discord.Embed(
        title="Cuadernos y libros de Análisis de Señales y Sistemas:",
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
            - Examen Sustitutorio
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
            - Examen Sustitutorio
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
            - Examen Sustitutorio
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
            - Clases PPT's Prof. Arenales 2021-1
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
            - Examen Sustitutorio
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
            - Examen Sustitutorio
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

    embeds.append(get_quimica_1_laboratorios_embed())  # [0]
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

def opciones_sistemas_operativos_1_embeds():
    embeds = []

    embeds.append("get_sistemas_operativos_1_laboratorios_embed()")  # [0]
    embeds.append(get_operativos_1_examenes_embed())      # [1]
    embeds.append(get_operativos_1_clases_embed())        # [2]
    embeds.append(get_operativos_1_cuadernos_embed())     # [3]

    return embeds

# /////////////////////////////////////////////////////////////////////////////////////


def opciones_fundamentos_electricidad_magnetismo_embeds():
    embeds = []

    embeds.append(get_fundamentos_electricidad_magnetismo_laboratorios_embed())  # [0]
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
    embeds.append(opciones_calculo_integral_embeds()) 
    embeds.append(opciones_algoritmos_1_embeds())  
    embeds.append(opciones_quimica_1_embeds()) 
    embeds.append(opciones_fundamentos_computador_embeds())
    embeds.append(opciones_redaccion_embeds())
    embeds.append("opciones_redes_1_embeds()")
    embeds.append(opciones_sistemas_operativos_1_embeds())

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
    embeds.append(opciones_metodos_numericos_embeds())
    embeds.append(opciones_circuitos_1_embeds())
    embeds.append(opciones_electrotecnia_embeds())
    embeds.append(opciones_etica_filosofia_embeds())
    embeds.append(opciones_operativos_2_embeds())

    return embeds

# ///////////////////////////////////////////////////////////////////////////////////////

def get_opciones_todos_los_ciclos_embeds():

    embeds = []

    embeds.append(get_opciones_primer_ciclo_embeds())  # [0]
    embeds.append(get_opciones_segundo_ciclo_embeds())  # [1]
    embeds.append(get_opciones_tercer_ciclo_embeds())
    embeds.append(get_opciones_cuarto_ciclo_embeds())

    return embeds

