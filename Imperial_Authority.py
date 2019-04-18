import discord
from discord.ext import commands
from discord.ext.commands import bot
from keep_alive import keep_alive
import os
import asyncio
import time


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
    
client = MyClient()


'''
@bot.command()
async def on_ready():
    print(chalk.green("Ready to go!"))
    print(chalk.blue(f"Serving: {len(bot.guilds)} guilds."))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Active!"))

'''
bot = commands.Bot(command_prefix="HRE:", status=discord.Status.online, activity=discord.Game(name="Preaching the one true faith"))

imperial_authority = 0.00

@bot.event
async def on_ready():
        print("I'm in")
        print(bot.user)


@bot.command()
async def authority(ctx):
        await ctx.channel.send('Current Imperial Authority is 0.0. \n 20.0 is needed to enact Prima Nocta')

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
    name = f"{member.name}#{member.discriminator}"
    #status = member.status
    #joined = member.joined_at
    #role = member.top_role
    await ctx.channel.send(f"name is {name}")


'''
@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
    name = f"{member.name}#{member.discriminator}"
    #status = member.status
    #joined = member.joined_at
    #role = member.top_role
    print('debug statement')
    await ctx.channel.send(f"name is {name}")

'''
#keep_alive()
#bot.run('NTY2ODE3OTU3MDQxNDA1OTUz.XLK7AQ.4n3zpKbal_3npEhTBgUNK7xpfU0')
bot.login(process.env.token)

