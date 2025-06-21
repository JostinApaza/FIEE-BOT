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