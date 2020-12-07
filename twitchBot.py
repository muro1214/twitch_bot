# -*- coding: utf-8 -*-

import requests
import json
import random
from twitchio.ext import commands

import config

bot = commands.Bot(
    irc_token=config.OAUTH,
    client_id=config.CLIENT_ID,
    nick=config.BOT_NAME,
    prefix=config.BOT_PREFIX,
    initial_channels=[config.CHANNEL]
)

bms_list = [{'url': 'http://mirai-yokohama.sakura.ne.jp/bms/data.json', 'prefix': '★'},
            {'url': 'https://stellabms.xyz/sl/score.json', 'prefix': 'sl'},
            {'url': 'https://stellabms.xyz/st/score.json', 'prefix': 'st'}
            ]


def random_select(bms, filter=None):
    res = requests.get(bms['url'])
    if not res.status_code == requests.codes.ok:
        return f"Error. status = {res.status_code}"

    jsonData = res.json()

    if filter:
        jsonData = [x for x in jsonData if x['level'] == filter]
    
    if jsonData == []:
        return f"Error. Maybe wrong difficulty?"

    i = random.randrange(len(jsonData))

    return f"{bms['prefix']}{jsonData[i]['level']} {jsonData[i]['title']}"


async def channel_send(ctx, bms):
    if ' ' in ctx.content:
        song = random_select(bms, ctx.content.split()[1])
    else:
        song = random_select(bms)

    message = f"Random Select -> [{song}] from {ctx.author.name}"

    await ctx.channel.send(message)


@bot.event
async def event_ready():
    print(f"{config.BOT_NAME}(insane) is online.")


@bot.command(name='insane')
async def insane(ctx):
    await channel_send(ctx, bms_list[0])


@bot.command(name='sl')
async def satellite(ctx):
    await channel_send(ctx, bms_list[1])


@bot.command(name='st')
async def stella(ctx):
    await channel_send(ctx, bms_list[2])


if __name__ == '__main__':
    bot.run()
