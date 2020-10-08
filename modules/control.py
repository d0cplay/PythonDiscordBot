
import discord
from discord.ext import commands
import modules


class Control(commands.Cog):
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
    @db.command()
    async def register(self, ctx):
        modules.db.addGuild(ctx.guild)
        await ctx.send(f"Added this guild to the records")

    #manage/cogs
#    @manage.group()
#    async def cogs(self, ctx):
#        if ctx.invoked_subcommand is Control.cogs:  # Possibly self.cogs instead, but I'm not sure.  
#            await ctx.send("Please check !help for options")
#    @cogs.command()
#    async def load(self, ctx, cog):
#        self.client.load_extension(cog)
#        modules.cmd.log(f"{ctx.author.name} loaded {cog}", 4)
#        await ctx.send(f"loaded {cog}")
#    @cogs.command()
#    async def unload(self, ctx, cog):
#        self.client.unload_extension(cog)
#        modules.cmd.log(f"{ctx.author.name} unloaded {cog}", 4)
#        await ctx.send(f"unloaded {cog}")
#    @cogs.command()
#    async def reload(self, ctx, cog):
#        self.client.unload_extension(cog)
#        self.client.load_extension(cog)
#        modules.cmd.log(f"{ctx.author.name} reloaded {cog}", 4)
#        await ctx.send(f"reloaded {cog}")
     

def setup(client):
    client.add_cog(Control(client))