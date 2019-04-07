import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import requests
import os
import sqlite3

print("Connecting...")

client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
	print("Logged in as:\n{}/{}#{}\n----------".format(client.user.id, client.user.name, client.user.discriminator))
	await client.change_presence(activity=discord.Game(name="with metal currently"))

@client.command()
async def startgtn(ctx, message: discord.Message = None):
	embed=discord.Embed(color=0x4A90E2)
	embed.add_field(name="I'm thinking of a new number:", value="Guess the number and i'll tell you if it's higher or lower then your guess!", inline=False)
	embed.set_footer(text="It's between 1 and 1000  | Currently in beta | Developed by Metal#0110")
	await ctx.send(embed=embed)
	number = random.randint(1,1000)
	while True:
		guess = await client.wait_for("message", check=lambda message: message.author == ctx.author)
		if guess.content.lstrip("-").lstrip(".").isdigit() == True:
			if int(guess.content) > number:
				embed=discord.Embed(color=0x00ffff)
				embed.add_field(name="Lower:", value="It's lower than **{}**".format(guess.content), inline=False)
				await ctx.send(embed=embed)
			
			if int(guess.content) < number:
				embed=discord.Embed(color=0x00ffff)
				embed.add_field(name="Higher:", value="It's higher than **{}**".format(guess.content), inline=False)
				await ctx.send(embed=embed)
			
			if int(guess.content) == number:
				await ctx.send(ctx.author.mention)
				embed=discord.Embed(color=0x00ff40)
				embed.add_field(name="{} Guessed correctly.".format(ctx.author), value="I was thinking of the number {}".format(number), inline=False)
				await ctx.send(embed=embed)
				break
		else:	
			if guess.content == "quit" or guess.content == "exit" and ctx.author == guess.author:
				break
			else:
				continue

client.run(str(os.environ.get("BOT_TOKEN")))
