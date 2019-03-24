import discord
import asyncio
import io
import json
import traceback
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='unload')
    async def unloaded(self, ctx, *, extension):   
        config = json.load(
            io.open('config.json', 'r', encoding='utf-8-sig')
        )
        print( config['adminid'] )
        print( ctx.author.id )
        if ctx.author.id in config['adminid']:
            extension = f'cogs.{extension}'
            try:
                self.bot.unload_extension(extension)
            except Exception as e: 
                await ctx.send(f'Не удалось отключить модуль {extension}.\n{e}')
            else:
                embed=discord.Embed(title="Unloaded", description=f"Module {extension} has been unloaded.")
                embed.set_thumbnail(url="https://www.iconfinder.com/icons/1398912/check_circle_correct_mark_success_tick_yes_icon")
                await ctx.send(embed=embed)
        else:
            await ctx.send('Вы не мой админ!')
    
    @commands.command(name='load')
    async def loaded(self, ctx, *, extension):   
        config = json.load(
            io.open('config.json', 'r', encoding='utf-8-sig')
        )
        print( config['adminid'] )
        print( ctx.author.id )
        if ctx.author.id in config['adminid']:
            extension = f'cogs.{extension}'
            try:
                self.bot.load_extension(extension)
            except Exception as e: 
                await ctx.send(f'Не удалось загрузить модуль {extension}.\n{e}')
            else:
                embed=discord.Embed(title="Unloaded", description=f"Module {extension} has been loaded.")
                embed.set_thumbnail(url="https://www.iconfinder.com/icons/1398912/check_circle_correct_mark_success_tick_yes_icon")
                await ctx.send(embed=embed)
        else:
            await ctx.send('Вы не мой админ!')
    
    @commands.command(name='reload')
    async def reload(self, ctx, *, extension): 
        config = json.load(
            io.open('config.json', 'r', encoding='utf-8-sig')
        )
        print( config['adminid'] )
        print( ctx.author.id )
        if ctx.author.id in config['adminid']:
            extension = f'cogs.{extension}'
            try:
                self.bot.unload_extension(extension)
                self.bot.load_extension(extension)
            except Exception as e: 
                await ctx.send(f'Не удалось перезагрузить модуль {extension}.\n{e}')
            else:
                embed=discord.Embed(title="Unloaded", description=f"Module {extension} has been reloaded")
                embed.set_thumbnail(url="https://www.iconfinder.com/icons/1398912/check_circle_correct_mark_success_tick_yes_icon")
                await ctx.send(embed=embed)
        else:
            await ctx.send('Вы не мой админ!')
    
    
def setup(bot):
    bot.add_cog(Admin(bot))