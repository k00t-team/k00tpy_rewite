#import start
import configparser
import io
import asyncio
import discord
import re
import json
import sys
from discord.ext import commands
from re import sub

#import end




#config start
try:
    config_j = json.load(open('config.json', 'r'))
    token = config_j['token']
    prefix = config_j['prefix']
    ownerid = config_j['adminid']
except FileNotFoundError:
    print('file config.ini are not found')
    print('copy \"config_example.json\" file and rename to config.json')
    print('and edit config.json file')
    sys.exit()

#config end



#bot creation start
bot = commands.Bot(command_prefix=prefix)
#bot creation end


#bot event handler

@bot.event
async def on_ready():
    print('Bot ready and started!')
    print('prefix: ' + prefix)
    print(f'{bot.user}')



#command handler start

extensions = ['cogs.fun', 'cogs.admin']
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f'{extension} loaded.')
        except Exception as error:
            print(f'{extension} cannot be loaded!\n{error}')#https://www.youtube.com/watch?v=gxKM6J5VmIc&list=PLW3GfRiBCHOiEkjvQj0uaUB1Q-RckYnj9&index=17
#command handler end
bot.run(token, bot=True, reconnect=True)