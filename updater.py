from time import sleep
import os, shutil

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

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