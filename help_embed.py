import discord
import textwrap

def get_ayuda_embed(prefix):

    embed = discord.Embed(
        title="Lista de comandos de FIEE-BOT.",
        description=textwrap.dedent(f"""\
            El prefix configurado para este servidor es `f!`.\n
            Aquí tienes una lista de los comandos disponibles:
            - `{prefix}help`: Muestra este mensaje de ayuda.
            - `{prefix}menu`: Muestra el menú de navegación principal, de todo el material disponible.
            - `{prefix}creditos`: Muestra los créditos y agradecimientos de FIEE-BOT, además del repositorio en GitHub.
        """),
        color=0x701B13  # Color del borde del embed (hexadecimal)
    )
    embed.add_field(name="Versión", value="1.0", inline=False)
    embed.add_field(name="Autores", value="Jostin Apaza, Martin Puicon, Fernando Perez, Banderley Gutierrez", inline=False)
    embed.set_footer(text="Gracias por usar FIEE-BOT.")  # Pie de página del embed
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s")  # opcional

    return embed
