import os, sys
import requests
import discord
print(sys.version)
f = open(".env","r")
TOKEN = f.readlines()[0]
f.close()

botCommander = ["TheGreydiamond#6512"]

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if(len(message.content) != 0):
		if(message.content[0] == "?"):
			print("Bot command registerd")
			processed = message.content[1:]
			if("random" in processed):
				req = requests.get('https://crazyapi.tk/api-v1/RandomFact.php')
				await message.channel.send(req.text)
				f = open("stats.txt","r+")
				temp = f.readlines()[0]
				temp = int(temp) + 1
				f.seek(0,0)
				f.write(str(temp))
				print("!!!" + str(temp))
				f.close()
			if("help" in processed):
				await message.channel.send("This is my help page! You can do ?random to get a useless fact.")
			if("stats" in processed):
				f = open("stats.txt", "r")
				await message.channel.send(f'I have served **{f.readlines()[0]}** useless facts.')
				f.close()
			if("stop" in processed):
				print(message.author)
				if(str(message.author) in botCommander):
					await message.channel.send(f'I will quit now. Goodbye :wave:')
					exit()
				else:
					await message.channel.send("You're not allowed to do that. :warning:")
client.run(TOKEN)