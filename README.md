# 🏫 FIEE-BOT 🏫

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![Discord.py Version](https://img.shields.io/badge/discord.py-2.0%2B-blue)](https://github.com/Rapptz/discord.py)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Un bot de Discord creado con el fin de servir como repositorio académico de la FIEE-UNI, transparente y de libre disponibilidad utilizando la API de Discord.

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRthy5kvoXKOzuuUpKXllMvUWD7UxBC0r0CEg&s" alt="Preview" width="300"/>
</p>

## ✨ Características principales

- **Sistema de repositorio**: con el comando /menu, puedes mostrar el menú principal con la opción de escoger cualquier curso de distintos ciclos y periodos académicos.
- **Fácil interacción**: Los botones de navegación y las listas desplegables permiten al usuario "desplazarse" con comodidad entre los distintos apartados del repositorio.

## 🛠️ Requisitos e instalación

### Prerrequisitos
- Python 3.8 o superior ([Python.org](https://www.python.org/downloads/release/python-3135/)).
- Una cuenta de Discord, propietaria de una aplicación/bot de Discord.
- Token de tu aplicación de Discord (disponible en [Discord Developers Portal](https://discord.com/developers/)).

### Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/JostinApaza/FIEE-BOT/
2. Instala las dependencias necesarias (discord.py):
   ```bash
   pip install -U discord.py
3. Edita manualmente la última línea del archivo main.py, y posteriormente incluye el token de tu aplicación de Discord:
   ```bash
   bot.run("<Inserta tu token aquí>")
4. Ejecuta la aplicación.
   ```bash
   python main.py
