import os
import sys

from tkinter import*
from tkinter import messagebox
from tkinter.simpledialog import askstring

root = Tk()
root.geometry("500x500")



cypher = { 'a' : 'D' , 'b' : 'K' , 'c' : 'V' , 'd' : 'Q' , 'e' : 'F' ,
	'f' : 'I' , 'g' : 'B' , 'h' : 'J' , 'i' : 'W' , 'j' : 'P' , 'k' : 'E' ,
	'l' : 'S' , 'm' : 'C' , 'n' : 'X' , 'o' : 'H' , 'p' : 'T' , 'q' : 'M' ,
	'r' : 'Y' , 's' : 'A' , 't' : 'U' , 'u' : 'O' , 'v' : 'L' , 'w' : 'R' ,
	'x' : 'G' , 'y' : 'Z' , 'z' : 'N' }

decypher = { 'A' : 's' , 'B' : 'g', 'C' : 'm' ,'D' : 'a' , 'E' : 'k' ,
'F' : 'e' , 'G' : 'x' , 'H' : 'o' , 'I' : 'f' , 'J' : 'h', 'K' : 'b' ,
'L' : 'v' , 'M' : 'q' , 'N' : 'z' , 'O' : 'u' , 'P' : 'j', 'Q' : 'd' ,
'R' : 'w' , 'S' : 'l' , 'T' : 'p' , 'U' : 't' , 'V' : 'c', 'W' : 'i' ,
'X' : 'n' , 'Y' : 'r' , 'Z' : 'y' }

def M1(letter):
	text1 = chr(ord(letter) - 3)			# takes individual letter then turns into ASCII value then subs 3 reassigns to text1
	if(text1.islower()):
		if(ord(text1) < ord('a')):			# checks to see if wraparound is needed
			text1 = chr(ord(text1) + 26)	# wraps letter back into ascii letter assigns letter to text1
	else:
		if(ord(text1) < ord('A')):
			text1 = chr(ord(text1) + 26)
	return text1

def M2(letter):
	return cypher[letter.lower()]				# preforms cipher with cypher dictionary

def M3(letter):
	text2 = chr(ord(letter) + 5)		# takes indivitual letter then turns into ASCII value then adds 5 reassigns to text2
	if(text2.islower()):
		if(ord(text2) > ord('z')):			# cheks to see if wraparound is needed
			text2 = chr(ord(text2) - 26)	# wraps letter back into ASCII letter assigns letter to text2
	else:
		if(ord(text2) > ord('Z')):
			text2 = chr(ord(text2) - 26)
	return text2

def DM1(letter):
	text3 = chr(ord(letter) + 3)		# does the reverse of M1
	if(text3.islower()):
		if(ord(text3) > ord('z')):
			text3 = chr(ord(text3) - 26)
	else:
		if(ord(text3) > ord('Z')):
			text3 = chr(ord(text3) - 26)
	return text3

def DM2(letter):
	return decypher[letter.upper()]		# preforms cipher with decypher dictionary

def DM3(letter):
	text4 = chr(ord(letter) - 5)		# does the reverse of M3
	if(text4.islower()):
		if(ord(text4) < ord('a')):
			text4 = chr(ord(text4) + 26)
	else:
		if(ord(text4) < ord('A')):
			text4 = chr(ord(text4) + 26)
	return text4

def Encription():
	toDo = askstring("Encrypt","Please enter the name of the file to encrypt:")
	File = askstring("File", "Please enter the destination file name: ")
	In = (open(toDo, 'r'))
	OutFile = (open(File, 'w'))
	for line in In:						# grabs code line by line
		line2 = line.rstrip('\n')		# strips off the new line char
		toCode = line2.split(' ')		# splits the line into words
		x = 0
		for word in toCode:
			for i in word:
				if(x % 3 == 0):			#if else satement to force the rotation of M1,M2,M3
					code0 = M1(i)
					OutFile.write(code0)
				elif(x % 3 == 1):
					code1 = M2(i)
					OutFile.write(code1)
				elif(x % 3 == 2):
					code2 = M3(i)
					OutFile.write(code2)
				x += 1
			OutFile.write(' ')
	msg = messagebox.showinfo("Success!", "File encrypted successully!")
	In.close()
	OutFile.close()

def Decription():
	toDo = askstring("Decrypt","Please enter the name of the file to decript:")
	File = askstring("File", "Please enter destination file name:")
	In = open(toDo, 'r')
	OutFile = open(File, 'w')
	for line in In:
		line3 = line.rstrip('\n')
		toCode = line3.split(' ')
		x = 0
		for word in toCode:
			for i in word:
				if(x % 3 == 0):
					code0 = DM1(i)
					OutFile.write(code0)
				elif(x % 3 == 1):
					code1 = DM2(i)
					OutFile.write(code1)
				elif(x % 3 == 2):
					code2 = DM3(i)
					OutFile.write(code2)
				x +=1
			OutFile.write(' ')
	msg = messagebox.showinfo("Success!", "File decrypted successully!")
	In.close()
	OutFile.close()

def Quit():
	msg = messagebox.showinfo("Goodbye!", "Have a nice day!")
	root.quit()

var = StringVar()
label = Message(root, textvariable = var)
var.set("Hello! Please press a button to continue.")

Forward = Button(text = "Encrypt", command = Encription)
Back = Button(text = "Decypher", command = Decription)
Leave = Button(text = "Exit", command = Quit)

Forward.place(relx = 0.4 , rely = 0.4)
Back.place(relx = 0.6 , rely = 0.4)
Leave.place(relx = 0.5 , rely = 0.5)
label.place(relx = 0.5 , rely= 0.0)

root.mainloop()
