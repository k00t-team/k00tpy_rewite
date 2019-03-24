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
    print(token)
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
@bot.event
async def on_message(message):
    words = message.content.split(' ')
    command = words[0].lower()
    args = ' '.join(words[1:])
#command handler end

bot.run(token)