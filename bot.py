import os, sys, json, git
import requests
import discord
import settings 

print(sys.version)

TOKEN = settings.token

botCommander = ["TheGreydiamond#6512"]

client = discord.Client()

def logToDC(message, channel = "none"):
	print(message)
	if(channel != "none"):
		channel.send(message)

def updateBot(channel = "none"):
	logToDC("Starting update", channel=channel)
	loFi = open("version.json", "r")
	processString = ""
	for elm in loFi.readlines():
		processString += elm
	jsonPro = json.loads(processString)
	localVersion = jsonPro["version"]
	## Now query the remote version
	req = requests.get("https://raw.githubusercontent.com/TheGreyDiamond/UseLess-Bot/master/version.json")
	reFi = req.text
	jsonremo = json.loads(reFi)
	remoteVersion = jsonremo["version"]
	## Now check if there is a new version
	localVersionPart = localVersion.split(".")
	remoteVersionPart = remoteVersion.split(".")

	## Check if there is a Major update
	updateAvaiable = False
	if(int(remoteVersionPart[0]) > int(localVersionPart[0])):
		updateAvaiable = True
	## Check for minor update
	if(int(remoteVersionPart[1]) > int(localVersionPart[1])):
		updateAvaiable = True
	## Check for BUgfix update
	if(int(remoteVersionPart[2]) > int(localVersionPart[2])):
		updateAvaiable = True
	
	print("--Version--")
	print(f'Local version is {localVersion}')
	print(f'Remote version is {remoteVersion}')
	if(updateAvaiable):
		logToDC("There is a newer version avaiable. Downloading update..", channel=channel)

		git.Git("update/").clone("https://github.com/TheGreyDiamond/UseLess-Bot.git")
		logToDC("Download done.", channel=channel)
	else:
		logToDC("There is no newer version avaiable", channel=channel)



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord! Iam on {len(client.guilds)} guilds!')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if(len(message.content) != 0):
		if(message.content[0] == "?"):
			print("Bot command registered")
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
				await message.channel.send("This is my help page! You can do ?random to get a useless fact. You can use ?stats to get some stats!x")
			if("stats" in processed):
				f = open("stats.txt", "r")
				await message.channel.send(f'I have served **{f.readlines()[0]}** useless facts. And Iam on **{len(client.guilds)}** guilds.')
				f.close()
			if("stop" in processed):
				print(message.author)
				if(str(message.author) in botCommander):
					await message.channel.send(f'I will quit now. Goodbye :wave:')
					exit()
				else:
					await message.channel.send("You're not allowed to do that. :warning:")
#client.run(TOKEN)
updateBot()