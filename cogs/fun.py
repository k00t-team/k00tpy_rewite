import discord
import asyncio
import io
import json
import traceback
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        await ctx.send('pong!')

    
def setup(bot):
    bot.add_cog(Fun(bot))