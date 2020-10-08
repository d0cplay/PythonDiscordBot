

import discord
from discord.ext import commands
import modules


class Sample(commands.Cog):
    def __init__(self, client):
        self.client = client


    #EVENTS


    #COMMANDS
    @commands.group()
    async def manage(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Please check !help for options")
    #manage/db
    @manage.group()
    async def db(self, ctx):
        if ctx.invoked_subcommand is Control.db:   
            await ctx.send("Please check !help for options")#
    @db.command()
    async def add(self, ctx, user: discord.Member):
        modules.db.addUser(user.id, user.name)
        await ctx.send(f"Added {user.mention} to the records")



def setup(client):
    client.add_cog(Sample(client))