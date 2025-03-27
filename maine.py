import discord
from discord.ext import commands
import os
import random
import requests


description= """para que funcione a variable"""



intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='-', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def word(ctx, count=1):
    await ctx.send ("¡Bienvenido al servidor!")

@bot.command()
async def reciclaje(ctx, count=1):
    await ctx.send ("es el proceso de reutilizar materiales y desechos para crear nuevos productos, estos son: "
    "Papel y cartón: Periódicos, revistas, cajas, cuadernos."
    "Plástico: Botellas, envases, bolsas, recipientes de comida.Vidrio → Botellas, frascos, tarros."
    "Metales: Latas de aluminio, latas de acero, envases de conserva."
    "Textiles: Ropa, telas, zapatos."
    "Electrónicos: Teléfonos móviles, computadoras, electrodomésticos pequeños."
    "Orgánicos: Restos de comida, cáscaras de frutas y verduras (para compostaje).")






bot.run("TOKEN")
