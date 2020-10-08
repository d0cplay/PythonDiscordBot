


import discord
from discord.ext import commands
import modules


class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    #EVENTS


    #COMMANDS
    @commands.group()
    async def ticket(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Please check !help for options")
    #ticketing

    @ticket.command()
    async def create(self, ctx, user: discord.Member):
        modules.db.addUser(user.id, user.name)
        await ctx.send(f"Added {user.mention} to the records")

    @ticket.command()
    async def respond(self, ctx, user: discord.Member):
        modules.db.addUser(user.id, user.name)
        await ctx.send(f"Added {user.mention} to the records")

    @ticket.command()
    async def list(self, ctx, user: discord.Member):
        modules.db.addUser(user.id, user.name)
        await ctx.send(f"Added {user.mention} to the records")

    @ticket.command()
    async def active(self, ctx, user: discord.Member):
        modules.db.addUser(user.id, user.name)
        await ctx.send(f"Added {user.mention} to the records")

    @ticket.command()
    async def delete(self, ctx, user: discord.Member):
        modules.db.addUser(user.id, user.name)
        await ctx.send(f"Added {user.mention} to the records")



def setup(client):
    client.add_cog(Moderation(client))