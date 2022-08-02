import discord
from discord.ext import commands

TOKEN = ("MTAwMjE4OimportDAyODM5MzA1MDE5Mg.GtvMVt.pNRVAitXeJ0sbV5_pe68gq36bOryocFtYuky_4")

bot = commands.Bot(command_prefix=('!'))
bot.remove_command( 'help' )

@bot.event
async def on_ready():
    print("Я запущен!")

@bot.command()
async def hello(ctx):
    embed = discord.Embed(
        title="Привет всем!",    
    )
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, arg):
  await ctx.send(arg)

bot.run(TOKEN)
