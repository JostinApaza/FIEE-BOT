import discord
import textwrap

def get_ayuda_embed(prefix):

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
