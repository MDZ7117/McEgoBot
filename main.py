import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user.name}")

@bot.slash_command(name="ego", description="Voir ton ego")
async def ego(ctx):
    await ctx.respond(f"Ton ego est infini, {ctx.author.name}.")

bot.run(os.getenv("DISCORD_TOKEN"))
