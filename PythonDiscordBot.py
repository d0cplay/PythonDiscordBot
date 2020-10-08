#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright © 2019 by Keno "docplay" Hummel.
# All rights reserved. Do not distribute!
# This file is part of the PYBot Project.

import discord
from discord.ext import commands

import os
import asyncio
import time
import json
import random

import modules
from modules import *

version = "1.0dev"

devmode = True


#LAUNCH PROCEDURE
modules.cmd.log("Setting up the bot.. ", 2)

if not os.path.isfile('./bot/database.db'): #checks if database does NOT exist
    modules.db.generate()
    modules.cmd.log(f"Generated Database at ./bot/database.db",4)
else:
    modules.cmd.log(f"Found Database at ./bot/database.db",2)


with open('./bot/config.json') as f: #load config
    config = json.load(f)
    modules.cmd.log(f"Found Config at ./bot/config.json",2)


client = commands.Bot(command_prefix = config["bot"]["prefix"]) #creates bot
#client.remove_command("help")


cogs = config["bot"]["modules"]["active"]   #gets activated cogs
for cog in cogs:    #tries to load cogs
    try:
        client.load_extension(f"modules.{cog}")
        modules.cmd.log(f"automaticaly loaded {cog}", 4)
    except (discord.ClientException, ModuleNotFoundError):
        modules.cmd.log(f"Failed to load {cog}.", 3)

modules.cmd.log(f"launched the bot",4)

#EVENTS
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name= config["bot"]["status"])) #changes bots visuals
    if devmode == False:
        with open(config[bot][avatar], 'rb') as f:
            await client.user.edit(avatar=f.read())

    await client.user.edit(username= str(config["bot"]["display"]))


    if config["bot"]["channels"]["send"] == True:   #If true: sends pinned messages to channels

        #Control Center
        channel = client.get_channel(config["bot"]["channels"]["control"])
        await channel.purge(limit=100)
        message = await channel.send(f">>> You are a community member and want your own channel?\nType **!request <channel name here>** to recive it!")
        await message.pin()
        await channel.purge(limit=1)

        #Support
        channel = client.get_channel(config["bot"]["channels"]["support"])
        await channel.purge(limit=100)
        message = await channel.send(f">>> You are need of some high quality support?\nLet us message our staff members by using **!support <a description of your problem>**\n I'll remove your message instantaneously, so your secrets stay private\nPlease *never* share senistive and/or personal information, especially security releated things, like passwords with us!")
        await message.pin()
        await channel.purge(limit=1)

        #Welcome
        channel = client.get_channel(config["bot"]["channels"]["welcome"])
        await channel.purge(limit=100)
        embed = discord.Embed(title="Welcome to our Discord Server", description="")
        embed.add_field(name="Its your first time here?", value="dont worry, reply to this with !register and we will work things out")
        embed.add_field(name="Game Server:", value="n/a")
        embed.add_field(name="3rd Box_", value="n/a")
        message = await channel.send(content=None, embed=embed)
        await message.pin()
        await channel.purge(limit=1)

        modules.cmd.log("Posted perma Messages",2)



client.run(config["bot"]["token"],
           bot=True, 
           reconnect=True
           )
