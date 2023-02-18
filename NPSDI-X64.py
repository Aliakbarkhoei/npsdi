"""
This program was developed by Aliakbar Zainali and is released under the Apache license for free.
It is an open source program that you can edit and develop. But you have to publish any changes for free on its github repository.
Even if you think you can add a feature to this program in another programming language, you can add it and this program is not limited to Python.
This version of the NVDA speech dictionary improver program and its older versions only includes the Farsi Speech improver, but you can add any language's improver and publish it for free.
"""

# Import the modules.
import os, time

# Dictionary part:

# Get the dictionary path
Path = str(os.getenv('APPDATA'))
DicFile = Path + "\\nvda\\speechDicts\\voiceDicts.v1\\espeak\\espeak-Persian.dic" # If you would like to add another language's speech dictionary, you have to change Filename to your Filename. E.g: if you would like to add French (France) speech dictionary, you have to change this Filename to "espeak-French (France).dic"

# Set the reference file's reference
referenceFile="Ref.txt"

# Open the essential files and read them.
with open(DicFile, "r") as Dic:
	lines_Dic = Dic.readlines()
with open(referenceFile, "r") as reference:
	lines_Ref = reference.readlines()

# open Temp file to write reference content and rewrite it in the destination file. I did this because writing directly to the destination file made an error.
tmp=open("TMP.tmp", "w")
# Create a for loop and check each character. If it does not exist in the destination, write it to the Temp file.
for line in lines_Ref:
	if line not in lines_Dic:
		tmp.write(line)

# Close the temp file to save the written contents and reopen it in readable mode.
tmp.close()

# reopen the Destination file in Appendable mode and Temp file in readable mode.
W=open(DicFile, "a")
t=open("TMP.tmp", "r")

# Append Temp file's content to destination.
W.write(t.read())

# Close the files.
t.close()
W.close()
reference.close()

# Remove the unnecessary files.
os.remove("TMP.tmp")
os.remove("Ref.txt")

# CLDR part:

# Open the essential files; then read the reference and write it in the destination file; then close the files.
CLDR = open(r"c:\Program Files (x86)\nvda\locale\fa\cldr.dic", "w")
with open ("CRef.txt", "r") as CR:
	lines_CR = CR.read()
CLDR.write(lines_CR)
CLDR.close()
CR.close()

# Remove the unnecessary file.
os.remove("CRef.txt")

# Symbels part:

# Open the essential files; then read the reference and write it in the destination file; then close the files.
Symbels = open(r"c:\Program Files (x86)\nvda\locale\fa\symbols.dic", "w")
with open("Symref.txt", "r") as SymRef:
	lines_SymRef = SymRef.read()
Symbels.write(lines_SymRef)
Symbels.close()
SymRef.close()

# Remove the unnecessary file.
os.remove("Symref.txt")

# Print the Success mesage
print("دیکشنری با موفقیت نصب شد.")

# sleep running for three minuts.
time.sleep(3)
print("")
