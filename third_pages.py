import discord

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

def agregar_labs_pcs_clases_2_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Laboratorios", value="Laboratorios de distintos ciclos.", inline=False)
    embed.add_field(name="▸  Prácticas", value="Prácticas y exámenes.", inline=False)
    embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)

    return embed

def agregar_pcs_clases_2_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Prácticas", value="Prácticas y exámenes.", inline=False)
    embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed.add_field(name="▸  Cuadernos", value="Cuadernos del curso.", inline=False)

    return embed

def get_primer_ciclo_embeds():
    embeds = []

    embed1 = discord.Embed(title="📚 Física 1", description="", color=discord.Color.dark_green())
    embed1 = agregar_labs_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo Diferencial", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Cálculo Diferencial BMA01]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Álgebra Lineal", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_2_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Álgebra lineal BMA03]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Dibujo Técnico", description="", color=discord.Color.green())
    embed4 = agregar_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Dibujo Técnico EE250]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Introducción a la computación", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_2_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Introducción a la computación BIC01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Realidad Nac. Constitución y DD.HH", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_2_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Realidad Nac. C. y DD.HH BRN01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Fundamentos de programación", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_2_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Fundamentos de programación CBS01]()", inline=False)
    embeds.append(embed7)

    return embeds


def get_segundo_ciclo_embeds():
    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Ing. térmica y de fluidos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Fundamentos de Ing. térmica y de fluidos BFI05]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo Integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Cálculo Integral BMA02]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Algoritmos y estructuras de datos I BMA09]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Química BQU01]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de Ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_2_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Fundamentos De Ing. del computador EE152]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_2_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Redacción y comunicación BRC01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Redes de Datos I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_2_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Redes de Datos I CBN01]()", inline=False)
    embeds.append(embed7)

    embed8 = discord.Embed(title="📚 Sistemas Operativos I", description="", color=discord.Color.green())
    embed8 = agregar_pcs_clases_campos(embed8)
    embed8.add_field(name="▸  Sílabo", value="[Sílabo de Sistemas Operativos I CBS02]()", inline=False)
    embeds.append(embed8)

    return embeds

def get_tercer_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Fundamentos de Electricidad y Magnetismo", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Fund. Electicidad y Magnetismo BFI03]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Ecuaciones Diferenciales", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Ecuaciones Diferenciales BMA05]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Probabilidades y Estadística", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Probabilidades y Estadística BMA10]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Programación Orientada a Objetos", description="", color=discord.Color.green())
    embed4 = agregar_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Programación Orientada a Objetos BMA15]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Economía General", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_2_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Economía General BEG01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redes de Datos II", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_2_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Redes de Datos II CBN02]()", inline=False)
    embeds.append(embed6)

    return embeds

def get_cuarto_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Introducción a la física moderna", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Intr. Física moderna]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Análisis de señales y sistemas", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Cálculo Vectorial", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Circuitos Eléctricos I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Métodos Numéricos", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Ética y Filosofía", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_2_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Electrotecnia e instalación de redes", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_2_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed7)

    embed8 = discord.Embed(title="📚 Sistemas Operativos II", description="", color=discord.Color.green())
    embed8 = agregar_pcs_clases_campos(embed8)
    embed8.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed8)

    return embeds


def get_quinto_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Mecánica de fluidos y termodinámica", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Procesos estocásticos", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_2_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed2)

    embed4 = discord.Embed(title="📚 Dispositivos y circuitos electrónicos I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed4)

    embed3 = discord.Embed(title="📚 Circuitos eléctricos II", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_2_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed3)

    embed5 = discord.Embed(title="📚 Laboratorio de electrónica I", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_2_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Electromagnetismo I", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_2_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Sistemas de control I", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_2_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed7)


    return embeds

def get_sexto_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Sistemas de comunicaciones I", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Dispositivos y circuitos electrónicos II", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_2_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Laboratorio de electrónica II", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_2_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Electromagnetismo II", description="", color=discord.Color.green())
    embed4 = agregar_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Microcontroladores", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_2_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Sistemas de control II", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_2_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 Ingeniería de Software", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_2_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed7)

    return embeds

def get_septimo_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Protocolos de enrutamiento y arquitectura de redes", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Conversión de energía electromecánica", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_2_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Sistemas de comunicaciones II", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_2_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Fibra óptica", description="", color=discord.Color.green())
    embed4 = agregar_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed7)

    return embeds


def get_octavo_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Formulación y evaluación de proyectos", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Laboratorio de radiocomunicaciones", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_2_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed7)

    return embeds


def get_noveno_ciclo_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 Sistemas de conmutación", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Gestión y seguridad de redes", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_2_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed7)

    return embeds


def get_cursos_electivos_embeds():

    embeds = []

    embed1 = discord.Embed(title="📚 blank", description="", color=discord.Color.dark_green())
    embed1 = agregar_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 blank", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed6 = agregar_pcs_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed6)

    embed7 = discord.Embed(title="📚 blank", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01]()", inline=False)
    embeds.append(embed7)

    return embeds


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