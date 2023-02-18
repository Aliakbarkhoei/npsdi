"""
This program was developed by Aliakbar Zainali and is released under the Apache license for free.
It is an open source program that you can edit and develop. But you have to publish any changes for free on its github repository.
Even if you think you can add a feature to this program in another programming language, you can add it and this program is not limited to Python.
This version of the NVDA speech dictionary improver program and its older versions only includes the Farsi Speech improver, but you can add any language's improver and publish it for free.
"""

# Import the modules.
import urllib3, time, os, webbrowser

# Check if install file is exist; If yes remove it.
if (os.path.isfile("NPSDI-X64.py")):
	os.remove("NPSDI-X64.py")
if (os.path.isfile("NPSDI-X86.py")):
	os.remove("NPSDI-X86.py")
else:
	pass

#Open the essential files.
Path = str(os.getenv('APPDATA'))
DicFile = Path + "\\nvda\\speechDicts\\voiceDicts.v1\\espeak\\espeak-Persian.dic" # If you have added another language's speech dictionary, you have to change Filename to your Filename. E.g: if you have added French (France) speech dictionary, you have to change this Filename to "espeak-French (France).dic"
UninstallFile="r.unins"
Temp="w.tmp"

# Open other essential files and read them.
with open(UninstallFile, "r") as Un:
	lines_Un = Un.readlines()
with open(DicFile, "r") as Dic:
	lines_Dic = Dic.readlines()

# Get the users desktop location.
desktop = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') )
SHName = "کنسولِ بهبود دهندۀ دیکشنریِ گفتارِ NVDA.lnk" # Program's shortcut name.
Absolute=desktop+"\\"+SHName

# Console main:

c = input("برای باز کردنِ وبسایتِ ما، کلید B را وارد کنید.\n برای لغوِ نصبِ این برنامه، کلید U را وارد کنید. \n برای ارسالِ واژه به ما، کلید W را وارد کنید. \n برای بررسی بروزرسانی، کلید D را وارد کنید. \n \n \n Enter B to open our website. \n Enter U to uninstall This program.\n Enter W to send the word to us. \n Enter D to check for updates.\n")

# Check which character entered by user.

# Uninstall part:

# check if user entered "U":
if c == "U" or c == "u" or c == "ع":
	UI = input("آیا از لغوِ نصبِ این دیکشنریِ گفتار مطمئنید؟ تمامیِ واژه‌های افزوده‌شده توسط این دیکشنری حذف خواهند شد. برای تأیید، کلید Y را وارد کنید. \n Are you sure about uninstalling this program? All words added by this dictionary will be deleted. Write Y and press enter to confirm.")
	if UI == "Y" or UI =="y" or UI == "غ":
# Check If Destination file has any content or not.
		if os.path.getsize(DicFile) > 3:
# Open temp file.
			Write=open(Temp, "w")
# Create a For loop and check if the character in the reference is present in the destination. If it doesn't exist, overwrite it in the destination (because when we opened it as a writable file, we deleted all the contents of the destination, but our changes weren't saved yet).
			for line in lines_Dic:
				if line not in lines_Un:
					Write.write(line)
				else:
					pass
			Write.close() # closed the file.
# Open essential files; Read the temp; write it to destination; close the files; remove the unnecessary files and print the success mesage.
			W=open(DicFile, "w")
			R=open("w.tmp", "r")
			r=R.read()
			W.write(r)
			R.close()
			os.remove("w.tmp")
			Un.close()
			os.remove("r.unins")
			print("لغوِ‌نصب با موفقیت انجام شد. تمامیِ واژگانِ وارد‌شده توسط این برنامه حذف شدند.")
			time.sleep(4)
# if  destination file is les than 3b (empty): close the file; check if the shortcut file does exist; if yes remove it and print "This program has been uninstalled before that.
		else:
				Un.close()
				os.remove("R.unins")
				if os.path.isfile(Absolute):
					os.remove(Absolute)
				print("این دیکشنریِ گفتار قبلاً لغوِ‌نصب شده‌است.")
				time.sleep(4)
# else if user entered another character instead of y: exit.
	else:
		print("Exited")
		time.sleep(2)
		print("")

# Send word part:

# if user entered "W":
elif c == "W" or c=="w" or c=="ص":
	print("شما در حال انتقال به صفحۀ ارسالِ واژه می‌باشید. توجه نمایید که در این مرحله اتصال به شبکۀ اینترنت ضروریست. \n با سپاس از همکاری ارزشمندتان. \n\n\nYou are being redirected to the word submission page. Note that an internet connection is necessary at this stage. \n Thank you for your valuable cooperation. \n\n")
	time.sleep(9)
	webbrowser.open("https://blindcity.ir/Send-Word", new=2)
	time.sleep(2)
	print("")

# Website part:

# check if user entered "B":
elif c=="B" or c=="b" or c=="ذ":
	webbrowser.open("https://blindcity.ir", new=2)
	time.sleep(2)
	print("")

# Update part:

elif c=="D" or c=="d" or c=="ی" or c=="ي":
# Try to open the version page; then read the data. if data is it's version, pass. else redirect to the download page.
	try:
		http = urllib3.PoolManager()
		resp = http.request("GET", "https://blindcity.ir/Ver.htm")
		if str(resp.data) == "b\'2.1.2\'":
			print("نرم‌افزار شما هم‌اکنون بروز است!\n Your program is up to date now!")
			time.sleep(3)
		elif str(resp.data) != "b\'2.1.2\'":
			I=input("نسخۀ جدیدی از این دیکشنری موجود است. \n " + str(resp.data) +"\n برای دانلود آن، حرف D را وارد کرده و کلید اینتر را بفشارید: \nA new version of this dictionary is available. \n " + str(resp.data) + "\n To download it, enter the letter D and press enter: \n")
			if I=="D" or I=="d" or I=="ی" or I=="ي":
				webbrowser.open("https://blindcity.ir/dic", new=2)
			else:
				pass
	except:
		print("احتمالا در اتصال شما به اینترنت مشکلی وجود دارد. لطفا اتصال خود را بررسی نمایید.\nThere is probably a problem with your internet connection. Please check your connection.")
		time.sleep(5)

time.sleep(1)
print("Exited")
