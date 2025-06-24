import discord

def despliegue_lista_ciclos():

    opciones = []

    opciones.append(discord.SelectOption(label="1er ciclo", value=1))
    opciones.append(discord.SelectOption(label="2do ciclo", value=2))
    opciones.append(discord.SelectOption(label="3er ciclo", value=3))
    opciones.append(discord.SelectOption(label="4to ciclo", value=4))
    # opciones.append(discord.SelectOption(label="5to ciclo", value=5))
    # opciones.append(discord.SelectOption(label="6to ciclo", value=6))
    # opciones.append(discord.SelectOption(label="7mo ciclo", value=7))
    # opciones.append(discord.SelectOption(label="8vo ciclo", value=8))
    # opciones.append(discord.SelectOption(label="9no ciclo", value=9))
    # opciones.append(discord.SelectOption(label="Electivos", value=10))

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
        # discord.SelectOption(label="Asesorías 1er ciclo", value=8),
    ]
    lista_cursos.append(opciones0)

    opciones1 = [
        discord.SelectOption(label="Fundamentos de Ing. térmica y de fluidos", value=1),
        discord.SelectOption(label="Cálculo integral", value=2),
        discord.SelectOption(label="Algoritmos y estructuras de datos I", value=3),
        discord.SelectOption(label="Química", value=4),
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
