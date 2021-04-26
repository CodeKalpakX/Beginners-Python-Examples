import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run("token")