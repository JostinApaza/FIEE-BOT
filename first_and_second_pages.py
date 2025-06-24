import discord
import textwrap

def get_ciclos_embeds():

    embed = discord.Embed(
        title="📚 Repositorio de FIEE-BOT.",
        description=textwrap.dedent(f"""\
            Selecciona una opción de la lista desplegable para seleccionar el ciclo.\n
            - **Primer ciclo**
            - **Segundo ciclo**
            - **Tercer ciclo**
            - **Cuarto ciclo**
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
            - **EE458** - Laboratorio de electrónica II
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
