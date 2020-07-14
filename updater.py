from time import sleep
import os, shutil, settings

pythonPath = settings.pythonPath

def copytree(src, dst, symlinks=False, ignore=None):
	for item in os.listdir(src):
		try:
			if("stats.txt" not in item):
				s = os.path.join(src, item)
				d = os.path.join(dst, item)
				if os.path.isdir(s):
					shutil.copytree(s, d, symlinks, ignore)
				else:
					shutil.copy2(s, d)
		except:
			pass

print("Starting updater.")
print("Wating 10 seconds for the main bot to quit.")
sleep(1)
print("Waiting done. All files in the folder: ")
print(os.listdir("./"))
print("Starting preserver")
listOf = os.listdir("./")
keepList = ["update", ".env", ".git", ".gitignore", ".gitattributes", "backup", "keepFiles", "settings.py", "stats.txt"]
for rm in keepList:
	listOf.remove(rm)
print("Files/Folders to delete: ")
print(listOf)
print("Starting deletion...")
for dele in listOf:
	print("Deleting " + dele + "...", end="")
	if(os.path.isdir(dele)):
		shutil.rmtree(dele)
	else:
		os.remove(dele)
	print("[Done]")
print("Starting file moving..", end = "")
copytree("./update/UseLess-Bot/", "./")
print("Done! Letting everything settel for a minute")
sleep(4)
print("Cleaning up")
try:
	shutil.rmtree("./update/")
except Exception as e:
	print("Unable to remove old update folder.")
	print("Error was: " + str(e))
	print("Trying linux way")
	os.system("rm update -R -f")
print("Everything is done!! Restarting bot.")
os.system(pythonPath + " bot.py")