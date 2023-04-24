import asyncio
import os
import discord
from discord.ext import commands

os.system("cls")

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=".", intents=intents, help_command=None)


async def load_all():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(
        f"{ctx.author.mention}, you have successfully reloaded the {extension} extension."
    )


async def main():
    await load_all()
    await bot.start("BOTTOKENHERE")


asyncio.run(main())
