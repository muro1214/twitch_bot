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


def get_insane_song(filter=None):
    url = 'http://mirai-yokohama.sakura.ne.jp/bms/data.json'

    res = requests.get(url)
    if not res.status_code == requests.codes.ok:
        return f"Error. status = {res.status_code}"

    jsonData = res.json()

    if filter:
        jsonData = [x for x in jsonData if x['level'] == filter]
    
    if jsonData == []:
        return f"Error. Maybe wrong difficulty?"

    i = random.randrange(len(jsonData))

    return f"★{jsonData[i]['level']} {jsonData[i]['title']}"


@bot.event
async def event_ready():
    print(f"{config.BOT_NAME}(insane) is online.")


@bot.command(name='insane')
async def insane(ctx):
    if ' ' in ctx.content:
        song = get_insane_song(ctx.content.split()[1])
    else:
        song = get_insane_song()

    message = f"Random Select -> [{song}] from {ctx.author.name}"

    await ctx.channel.send(message)


if __name__ == '__main__':
    bot.run()
