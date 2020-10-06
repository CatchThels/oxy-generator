ver = 1.0
max = 0
save = False
onlyhits = False
wrong = 0
hits = 0
names = False

import getpass

print("Hello, " + getpass.getuser() + ".")

import requests, sys, string, random
from lxml.html import fromstring
from colorama import init, Fore
init()

def setTitle(title):
	try:
		sys.stdout.write("\x1b]2;" + title + "\x07")
	except:
		pass

setTitle("OxyGenerator - Loading...")

def getFileName(title):
	if title.__contains__("Скачать файл "): # Russian language
		file_name = title.replace("Скачать файл ", "").replace(" на Oxy.Cloud", "")
	if title.__contains__("Download the file"): # English language
		file_name = title.replace("Download the file ", "").replace(" on Oxy.Cloud", "")
	if title.__contains__("Завантажити файл "): # Ukraine language
		file_name = title.replace("Завантажити файл ", "").replace(" на Oxy.Cloud", "")
	if title.__contains__("Descargar el archivo de "): # Spain language
		file_name = title.replace("Descargar el archivo de ", "").replace(" en la Oxy.Cloud", "")
	if title.__contains__("Laden Sie die "): # German language
		file_name = title.replace("Laden Sie die ", "").replace(" auf Oxy.Cloud", "")

	return file_name





print(Fore.GREEN + "- OxyCloud links generator: " + str(ver) + " -" + Fore.RESET)
print("by katch.")

for arg in sys.argv:
	if arg.__contains__("--max"):
		max = sys.argv[sys.argv.index("--max") + 1]
		print("Max amount of generated links: " + Fore.YELLOW + max + Fore.RESET)
	if arg.__contains__("--save"):
		save = True
	if arg.__contains__("--onlyhits"):
		onlyhits = True
	if arg.__contains__("--names"):
		names = True
if max == 0 and onlyhits == True:
	print(Fore.YELLOW + "Ignored parametrs: --onlyhits. Because max amount of links is unlimited." + Fore.RESET)

if save == True:
	open("oxylinks.txt", "a").close()
	
if int(max) == 0:
	i = 0
	while True:
		link = "https://oxy.st/d/" + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()
		sys.stdout.write("- [" + str(i) + "]: Checking: " + Fore.YELLOW + link + Fore.RESET + ": ")
		req = requests.get(link)
		tree = fromstring(req.content)
		title = tree.findtext('.//title')
		try:
			if title.startswith("Oxy"):
				print(Fore.RED + "Failed" + Fore.RESET)
				wrong+=1
			else:
				print(Fore.GREEN + "Working!" + Fore.RESET + " (" + getFileName(title) + ")")
				hits+=1
				if save == True:
					with open("oxylinks.txt", "a", encoding="utf-8") as file:
						file.write(link)
						if names == False:
							file.write("\n")
						else:
							file.write(" | " + getFileName(title) + "\n")
			i+=1
		except AttributeError:
			print(Fore.MAGENTA + "Locked\a" + Fore.RESET)
			wrong+=1
		setTitle("Total: Hits: " + str(hits) + "   Fails: " + str(wrong))
else:
	i = 0
	while i < int(max):
		link = "https://oxy.st/d/" + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()
		sys.stdout.write("- [" + str(i) + "/" + max + "]: Checking: " + Fore.YELLOW + link + Fore.RESET + ": ")
		req = requests.get(link)
		tree = fromstring(req.content)
		title = tree.findtext('.//title')
		try:
			if title.startswith("Oxy"):
				if onlyhits == False:
					i+=1
				print(Fore.RED + "Failed" + Fore.RESET)
				wrong+=1
			else:
				print(Fore.GREEN + "Working!" + Fore.RESET + " (" + getFileName(title) + ")")
				i+=1
				hits+=1
				if save == True:
					with open("oxylinks.txt", "a", encoding="utf-8") as file:
						file.write(link)
						if names == False:
							file.write("\n")
						else:
							file.write(" | " + getFileName(title) + "\n")
		except AttributeError:
			print(Fore.MAGENTA + "Locked\a" + Fore.RESET)
			wrong+=1
			if onlyhits == False:
				i+=1
		setTitle("Total: Hits: " + str(hits) + "   Fails: " + str(wrong))