import discord

def agregar_pcs_clases_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Prácticas/exámenes", value="Prácticas y exámenes.", inline=False)
    # embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed.add_field(name="▸  Cuadernos y libros", value="Material del curso.", inline=False)

    return embed

def agregar_labs_pcs_clases_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Laboratorios", value="Laboratorios de distintos ciclos.", inline=False)
    embed.add_field(name="▸  Prácticas/exámenes", value="Prácticas y exámenes.", inline=False)
    # embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed.add_field(name="▸  Cuadernos y libros", value="Material del curso.", inline=False)

    return embed

def agregar_labs_pcs_clases_2_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Laboratorios", value="Laboratorios de distintos ciclos.", inline=False)
    embed.add_field(name="▸  Prácticas/exámenes", value="Prácticas y exámenes.", inline=False)
    # embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)

    return embed

def agregar_pcs_clases_2_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Prácticas/exámenes", value="Prácticas y exámenes.", inline=False)
    # embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed.add_field(name="▸  Cuadernos y libros", value="Material del curso.", inline=False)

    return embed

def agregar_pcs_cuadernos_campos(embed: discord.Embed) -> discord.Embed:

    # embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)
    embed.add_field(name="▸  Cuadernos y libros", value="Material del curso.", inline=False)

    return embed

def agregar_clases_campos(embed: discord.Embed) -> discord.Embed:

    embed.add_field(name="▸  Clases", value="Clases del curso PDF's/PPT.", inline=False)

    return embed

def get_primer_ciclo_embeds():
    embeds = []

    embed1 = discord.Embed(title="📚 Física 1", description="", color=discord.Color.dark_green())
    embed1 = agregar_labs_pcs_clases_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Física BFI01](https://drive.google.com/file/d/1u9Kc6HUYG4jbyEjMXRnTXYo_J8IOXsjB/view?usp=drive_link)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo Diferencial", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Cálculo Diferencial BMA01](https://drive.google.com/file/d/18KZZ0qCxScf_qc8-0ajq_KmrI3dMV8YJ/view?usp=drive_link)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Álgebra Lineal", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_2_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Álgebra Lineal BMA03](https://drive.google.com/file/d/1QDBQ-cInc4nidCzOAm_lG2dEQD42A0JA/view?usp=drive_link)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Dibujo Técnico", description="", color=discord.Color.green())
    embed4 = agregar_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Dibujo Técnico EE250](https://drive.google.com/file/d/1BXUuFeW7h0ata8KvNKrpolzMN20wNCcI/view?usp=drive_link)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Introducción a la computación", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_2_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Introducción a la computación BIC01](https://drive.google.com/file/d/12AHzG4pgZK5Uo_22rApVycQMuoYPHERl/view?usp=drive_link)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Realidad Nac. Constitución y DD.HH", description="", color=discord.Color.green())
    embed6 = agregar_pcs_cuadernos_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Realidad Nac. C. y DD.HH BRN01](https://drive.google.com/file/d/1RuS9yRktUdVMXSTk3_PlWbZUseSk0h4T/view?usp=drive_link)", inline=False)
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
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Fundamentos de Ing. térmica y de fluidos BFI05](https://drive.google.com/file/d/1IXW9TUdP4vD7-cZD5l-19921BLgiAYPG/view?usp=drive_link)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Cálculo Integral", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Cálculo Integral BMA02](https://drive.google.com/file/d/1YvmR7Me4dzSrL9oF6BWgjheTEKzU7TEz/view?usp=drive_link)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Algoritmos y estructuras de datos I", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Algoritmos y Estructuras de Datos I BMA09](https://drive.google.com/file/d/12I6FnyzpmSqXHLHoPRFg_Y0Z2HQdG4Oi/view?usp=drive_link)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Química I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Química BQU01](https://drive.google.com/file/d/1ZZ90XGEnpoD4vHIw2WNA2o7JWqR3LRj7/view?usp=drive_link)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Fundamentos de Ingeniería del computador", description="", color=discord.Color.green())
    embed5 = agregar_pcs_cuadernos_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Fundamentos De Ing. del computador EE152](https://drive.google.com/file/d/1IXW9TUdP4vD7-cZD5l-19921BLgiAYPG/view?usp=drive_link)", inline=False)
    embeds.append(embed5)

    embed6 = discord.Embed(title="📚 Redacción y comunicación", description="", color=discord.Color.green())
    embed6 = agregar_pcs_cuadernos_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Redacción y Comunicación BRC01]()", inline=False)
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
    embed1 = agregar_labs_pcs_clases_2_campos(embed1)
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Fund. Electicidad y Magnetismo BFI03](https://drive.google.com/file/d/1s5xkVYiXKsmC5YkJ0ypDeydAH7vD4t2u/view?usp=drive_link)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Ecuaciones Diferenciales", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Ecuaciones Diferenciales BMA05](https://drive.google.com/file/d/1OCy8mYTPQ8sn2SZl6gIyw3ZjIYaK2VFq/view?usp=drive_link)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Probabilidades y Estadística", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Probabilidades y Estadística BMA10](https://drive.google.com/file/d/1Hf9VM9xfgBiD6oOmmYdFSsEuG1zIxErr/view?usp=drive_link)", inline=False)
    embeds.append(embed3)

    embed4 = discord.Embed(title="📚 Programación Orientada a Objetos", description="", color=discord.Color.green())
    embed4 = agregar_pcs_clases_2_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Programación Orientada a Objetos BMA15](https://drive.google.com/file/d/1Zi82ZMDsbjAoLC8B-kMPEIGCQjQ8tILx/view?usp=drive_link)", inline=False)
    embeds.append(embed4)

    embed5 = discord.Embed(title="📚 Economía General", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_2_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Economía General BEG01](https://drive.google.com/file/d/1F00hAILcsDxMDffPpX5kXZSX2IXzVrj3/view?usp=drive_link)", inline=False)
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
    embed1.add_field(name="▸  Sílabo", value="[Sílabo de Intr. Física moderna](https://drive.google.com/file/d/17N7fM17H6BHiHm1OtVPoYptEfDmMs7kb/view?usp=drive_link)", inline=False)
    embeds.append(embed1)

    embed2 = discord.Embed(title="📚 Análisis de Señales y Sistemas", description="", color=discord.Color.orange())
    embed2 = agregar_pcs_clases_campos(embed2)
    embed2.add_field(name="▸  Sílabo", value="[Sílabo de Análisis de Señales y Sistemas EE410](https://drive.google.com/file/d/1Kr917lBcyVsUhJAGcn6h1MVIQGseyXR9/view?usp=drive_link)", inline=False)
    embeds.append(embed2)

    embed3 = discord.Embed(title="📚 Cálculo Vectorial", description="", color=discord.Color.green())
    embed3 = agregar_pcs_clases_campos(embed3)
    embed3.add_field(name="▸  Sílabo", value="[Sílabo de Cálculo Vectorial BMA07](https://drive.google.com/file/d/1F8LdvAhiZ7MV1Bnj-FM6AKM7oHWmN1e6/view?usp=drive_link)", inline=False)
    embeds.append(embed3)

    embed5 = discord.Embed(title="📚 Métodos Numéricos", description="", color=discord.Color.green())
    embed5 = agregar_pcs_clases_campos(embed5)
    embed5.add_field(name="▸  Sílabo", value="[Sílabo de Métodos Numéricos BMA18](https://drive.google.com/file/d/1aEen5u861yB5dI3hlRodwAnmcVqkrNFU/view?usp=drive_link)", inline=False)
    embeds.append(embed5)

    embed4 = discord.Embed(title="📚 Circuitos Eléctricos I", description="", color=discord.Color.green())
    embed4 = agregar_labs_pcs_clases_campos(embed4)
    embed4.add_field(name="▸  Sílabo", value="[Sílabo de Circuitos Eléctricos I EE320](https://drive.google.com/file/d/1mDNMXv08GJ9ZtQS_Z0kPLTl_8m8sOuvS/view?usp=drive_link)", inline=False)
    embeds.append(embed4)

    embed7 = discord.Embed(title="📚 Electrotecnia e Instalación de redes", description="", color=discord.Color.green())
    embed7 = agregar_pcs_clases_2_campos(embed7)
    embed7.add_field(name="▸  Sílabo", value="[Sílabo de Electrotecnia e Instalación de redes](https://drive.google.com/file/d/1eysHHVBHaa13Iee-IJBBIWUEOfSjyrpY/view?usp=drive_link)", inline=False)
    embeds.append(embed7)

    embed6 = discord.Embed(title="📚 Ética y Filosofía política", description="", color=discord.Color.green())
    embed6 = agregar_clases_campos(embed6)
    embed6.add_field(name="▸  Sílabo", value="[Sílabo de Ética y Filosofía BEF01](https://drive.google.com/file/d/1W2d6B2mmQikuE0Qz-UEUrtavrYF_9fwE/view?usp=drive_link)", inline=False)
    embeds.append(embed6)

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