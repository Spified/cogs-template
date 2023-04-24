import discord
import json
import os
import random
import traceback
from discord.ext import commands


class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def ping(self, ctx):
        try:
            await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
        except:
            await ctx.send(
                f"{ctx.author.mention}, you have caused an error with that command. Correct usage: `.help`."
            )
            print(traceback.format_exc())
            return


async def setup(bot):
    await bot.add_cog(general(bot))
