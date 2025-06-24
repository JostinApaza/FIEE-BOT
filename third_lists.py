import discord
from discord.ext import commands

def despliegue_lista_opciones_LAB():

    opciones = []

    opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    # opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones

def despliegue_lista_opciones_LAB_NO_CUADERNO():

    opciones = []

    opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    # opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones

def despliegue_lista_opciones_NO_LAB():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    # opciones.append(discord.SelectOption(label="Clases", value=3))
    opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones

def despliegue_lista_opciones_NO_LAB_NO_PC():

    opciones = []

    # opciones.append(discord.SelectOption(label="Laboratorios", value=1))
    # opciones.append(discord.SelectOption(label="Prácticas y exámenes", value=2))
    # opciones.append(discord.SelectOption(label="Clases", value=3))
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
    # opciones.append(discord.SelectOption(label="Clases", value=3))
    # opciones.append(discord.SelectOption(label="Cuadernos y libros", value=4))

    return opciones


# ///////////////////////////////////////////////////////////////////////////////////////


def devolver_terceras_listas(ciclo_seleccionado, curso_seleccionado):
        
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
            opciones = despliegue_lista_opciones_NO_LAB_NO_PC_NO_CLASE()

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
            opciones = despliegue_lista_opciones_LAB_NO_CUADERNO()

        if curso_seleccionado == 4: 
            opciones = despliegue_lista_opciones_NO_LAB_NO_PC_NO_CLASE()

        if curso_seleccionado == 5:
            opciones = despliegue_lista_opciones_NO_LAB_NO_PC_NO_CLASE()

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

        if curso_seleccionado == 5:
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

        if curso_seleccionado == 5:
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

        if curso_seleccionado == 5:
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

        if curso_seleccionado == 5:
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

        if curso_seleccionado == 5:
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

        if curso_seleccionado == 5:
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

        if curso_seleccionado == 5:
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

        if curso_seleccionado == 5:
            opciones = despliegue_lista_opciones_NO_LAB()

        if curso_seleccionado == 6:
            opciones = despliegue_lista_opciones_LAB()
            
        if curso_seleccionado == 7:
            opciones = despliegue_lista_opciones_NO_LAB()
        
    return opciones