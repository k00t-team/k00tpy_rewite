#import start
import configparser
import io
import asyncio
import discord
import re
import sys
from discord.ext import commands
from re import sub

#import end




#config start
try:
    fh = open('config.ini', 'r').read()
    config = configparser.ConfigParser()
    config.sections()
    config.read('config.ini')
    config.sections()

    token = config['CONFIG']['token']
    prefix = config['CONFIG']['prefix']
    ownerid = config['CONFIG']['adminid']
except FileNotFoundError:
    print('file config.ini are not found')
    print('copy \"config_example.ini\" file and rename to config.ini')
    print('and edit config.ini file')
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
@bot.event
async def on_message(message):
    words = message.content.split(' ')
    command = words[0].lower()
    args = ' '.join(words[1:])
    if not message.author.bot:
        if command == f"{prefix}say":
            await message.channel.send(str(words))
#command handler end

bot.run(token)