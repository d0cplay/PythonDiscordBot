
import discord
from discord.ext import commands
from discord.ext import menus
import modules
from PythonDiscordBot import config

class Confirm(menus.Menu):
    def __init__(self, msg, channel):
        super().__init__(timeout=30.0, delete_message_after=True)
        self.msg = msg
        self.channel = channel 
        self.result = None

    async def send_initial_message(self, ctx, channel):
        return await self.channel.send(self.msg)

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def do_confirm(self, payload):
        self.result = True
        self.stop()

    @menus.button('\N{CROSS MARK}')
    async def do_deny(self, payload):
        self.result = False
        self.stop()

    async def prompt(self, ctx):
        await self.start(ctx, wait=True)
        return self.result


class Core(commands.Cog):
    def __init__(self, client):
        self.client = client


    #Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            modules.db.addUser(member.id, member.name, generateXP())
            await member.send(f">>> Hey {member.mention}, \nWe want to inform you, that {me} is collecting the ammount of messages, your xp and your level and stores this in a database. \nWe do not collect any other personal data \n **If you dont like your data being stored by us, please contact a member of staff and leave the server afterwards.** \nBy staying on the server we assume you have read this and are accepting the storage of named data")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author == self.client.user:
            modules.cmd.log(f"{message.author} @ {message.channel} : {message.content} ")
            modules.db.addMsg(message.author.id)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        modules.db.addGuild(guild)
            
    #Commands
    @commands.command()
    async def register(self, ctx):
        await ctx.message.delete() 
        if ctx.author.top_role == ctx.guild.default_role:
            channel = ctx.author

            embed = discord.Embed(title="About the bot and data collection", description="Your desc here",color=ctx.author.colour)
            embed.add_field(name="Instructions", value="bla", inline=False)
            embed.set_footer(text="Step 1/2")
            message = await channel.send(embed=embed)
            embed = discord.Embed(title="About our server Rules", description="Your desc here",color=ctx.author.colour)
            embed.add_field(name="Instructions", value="bla", inline=False)
            embed.set_footer(text="Step 2/2")
            message = await channel.send(embed=embed)

            confirm = await Confirm('>>> **Please tick \N{WHITE HEAVY CHECK MARK} to accept or ❌ to decline **', channel).prompt(ctx)
            if confirm:
                await channel.send(f">>> Thanks {ctx.author.mention}, welcome to the family!")
                await ctx.author.add_roles(discord.utils.get(ctx.author.guild.roles, name=config["bot"]["roles"]["member"]), reason=f"user has been registered and accepted the terms")
                modules.db.addUser(ctx.author.id,ctx.author.name)
                modules.cmd.log(f"{ctx.author} registered successesful and was added to the records")
            else:
                await channel.send(f">>> Iam sorry {ctx.author.mention} but without accepting to this terms you can not be a member of your server")
        else:
            msg = await ctx.send(f">>> {ctx.author.mention} you are all ready registered")
            await msg.delete(delay=5)


def setup(client):
    client.add_cog(Core(client))    