import discord
from discord.ext import commands
import requests
import os

bot = commands.Bot(command_prefix='get ')

@bot.command()
async def repeat(ctx, arg):
  await ctx.send(arg)
# 1 for panda images
@bot.command()
async def panda(ctx):
   response = requests.get('https://some-random-api.ml/animal/panda')
   data = response.json()
   myEmbed = discord.Embed(title = "*PANDA*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['image'])
   await ctx.send(embed = myEmbed)
# 2 for cat images    
@bot.command()
async def cat(ctx): 
   response = requests.get('http://aws.random.cat/meow')
   data = response.json()
   myEmbed = discord.Embed(title = "*meoww*", description = 'cutiee', colour= discord.Color.blurple())
   myEmbed.set_image(url=data['file'])
   await ctx.send(embed = myEmbed)
# 3 for dog images   
@bot.command()
async def dog(ctx):
   response = requests.get('https://dog.ceo/api/breeds/image/random')
   data = response.json()
   myEmbed = discord.Embed(title = "*Boww!*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['message'])
   await ctx.send(embed = myEmbed) 
# 4 for shiba images    
@bot.command()
async def shiba(ctx):
   response = requests.get('http://shibe.online/api/shibes')
   data = response.json()
   myEmbed = discord.Embed(title = "*Shibaaa*" , colour= discord.Color.random())
   myEmbed.set_image(url=data[0])
   await ctx.send(embed = myEmbed)  
# 5 for bunny images   
@bot.command()
async def bunny(ctx):
   response = requests.get('https://api.bunnies.io/v2/loop/random/?media=gif,png')
   data = response.json()
   myEmbed = discord.Embed(title = "*Carrots plzz*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['media']['gif'])
   await ctx.send(embed = myEmbed) 
# 6 for bird images
@bot.command()
async def bird(ctx):
   response = requests.get('https://some-random-api.ml/img/birb')
   data = response.json()
   myEmbed = discord.Embed(title = "*toTheMoon*", description = 'flap flap', colour= discord.Color.random())
   myEmbed.set_image(url=data['link'])
   await ctx.send(embed = myEmbed)
# 7 for fox images
@bot.command()
async def fox(ctx):
   response = requests.get('https://randomfox.ca/floof/')
   data = response.json()
   myEmbed = discord.Embed(title = "*fox served*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['image'])
   await ctx.send(embed = myEmbed) 
# 8 for rat images
@bot.command()
async def rat(ctx):
   response = requests.get('https://rat-api-image.herokuapp.com/rat/get')
   data = response.json()
   myEmbed = discord.Embed(title = "*no cat can catch me*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['img'])
   await ctx.send(embed = myEmbed) 
# 9 for wink gifs
@bot.command()
async def wink(ctx):
   response = requests.get('https://some-random-api.ml/animu/wink')
   data = response.json()
   myEmbed = discord.Embed(title = "*wink wink*" , colour= discord.Color.random())
   myEmbed.set_image(url=data['link'])
   await ctx.send(embed = myEmbed)        
  

bot.run(os.getenv('api_token'))