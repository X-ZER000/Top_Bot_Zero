import discord
from discord.ext import commands
#=====================================EXPLICACIÓN=================================================================================================================================
#intents: 
#Da permisos para que el bot pueda ver cosas dentro del Discord: Ver estados, ver imagenes, ver reacciones, entre otras...
#intents = discord.Intents.all()  
#El discord lo traduce como:
#“Dale todos los permisos permitidos a mi bot”
#Funciona porque el bot tiene acctivos el presence Intent, Server Members Intent y Message Content Intent
#=================================================================================================================================================================================

intents = discord.Intents.all()  

#=====================================EXPLICACIÓN=================================================================================================================================
#Aquí estás creando tu bot.
#Lo estás “definiendo” como un bot que acepta comandos y permisos.
#command_prefix="!" quiere decir que tus comandos empezarán por !
#Ejemplo:
#!hola, !ping, !ayuda
#Puedes cambiar el prefijo cuando quieras.
#intents=intents conecta los permisos que configuraste arriba.
#En español:
#“Crea un bot que use el prefijo ! y que tenga todos los permisos que le di antes.”
#=================================================================================================================================================================================

bot = commands.Bot(command_prefix="¡", intents=intents)

#=====================================EXPLICACIÓN=================================================================================================================================
#Este codigo cumple las funciones de:
#1. Confirmar que tu bot se conectó correctamente a Discord
#Cuando el bot arranca sin errores, este evento se ejecuta una sola vez.
#2. Mostrar en la consola el nombre del bot
#Así puedes verificar que Discord lo reconoció y ya está “vivo”.
#3. Es un evento automático (no un comando)
#No lo activa el usuario; lo activa Discord al iniciar la sesión del bot.
#En pocas palabras:
#Es el mensaje que te dice “todo funciona, tu bot está listo para usarse”
#=================================================================================================================================================================================

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

# ---- MENU PRINCIPAL ----
@bot.command()
async def menu(ctx):
    mensaje = (
        "Bienvenida a la Zona ANWE del conocimiento\n"
        "Elige qué quieres hacer:\n\n"
        "Retos diarios → `!reto`\n"
    )
    await ctx.send(mensaje)


# ---- MENU DE RETOS ----
@bot.command()
async def reto(ctx):
    mensaje = (
        "Elige el área del reto:\n\n"
        "Programación:\n"
        "Python → `!python`\n"
        "Web Nivel 1 → `!web1`\n"
        "Tecnología General → `!tecnologia`\n\n"
        "Escribe uno de los comandos para recibir tu reto."
    )
    await ctx.send(mensaje)


# ---- RETO PYTHON ----
@bot.command()
async def python(ctx):
    reto = (
        "Reto Python #1:\n"
        "Crea un programa que pida tu nombre y muestre un mensaje motivador.\n\n"
        "¿Quieres otro reto? Escribe `!python` de nuevo"
    )
    await ctx.send(reto)


# ---- RETO WEB NIVEL 1 ----
@bot.command()
async def web1(ctx):
    reto = (
        "Reto Web Nivel 1:\n"
        "Crea una página HTML que tenga un título y un párrafo con tu frase favorita.\n\n"
        "¿Otro reto web? → `!web1`"
    )
    await ctx.send(reto)


# ---- RETO TECNOLOGÍA GENERAL ----
@bot.command()
async def tecnologia(ctx):
    reto = (
        "Reto Tecnología General:\n"
        "Investiga qué es una API y escríbelo en una frase corta.\n\n"
        "¿Otro reto? → `!tecnologia`"
    )
    await ctx.send(reto)

# ---- INICIAR BOT ----
bot.run("Your Token")
