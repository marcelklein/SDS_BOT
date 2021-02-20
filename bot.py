# bot.py
# Example bot https://gist.github.com/FaztTech/e17ea3fde6988f7215301b888ccaaf5c
import os

import discord
from discord import colour
from discord.ext import commands
from dotenv import load_dotenv

# Replace with .env var
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$', description="This is a Helper Bot")


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.command()
async def info(ctx):
    await ctx.send('Hello I am the SDS bot. I was created by my glorious creator Lord Mars')


@bot.command()
async def event(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title='Event name',
        desccription='Event desc',
        colour=discord.Colour.blue()
    )
    embed.set_footer(test='Additional Info')
    await ctx.send(channel, embed=embed)

bot.run(TOKEN)
