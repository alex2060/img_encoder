

def point_to_value(a):
	if a=="0":
		return 0
	if a=="1":
		return 1
	if a=="2":
		return 2
	if a=="3":
		return 3
	if a=="4":
		return 4
	if a=="5":
		return 5
	if a=="6":
		return 6
	if a=="7":
		return 7
	if a=="8":
		return 8
	if a=="9":
		return 9
	if a=="a":
		return 10
	if a=="b":
		return 11
	if a=="c":
		return 12
	if a=="d":
		return 13
	if a=="e":
		return 14
	if a=="f":
		return 15
	if a=="g":
		return 16
	if a=="h":
		return 17
	if a=="i":
		return 18
	if a=="j":
		return 19
	if a=="k":
		return 20
	if a=="l":
		return 21
	if a=="m":
		return 22
	if a=="n":
		return 23
	if a=="o":
		return 24
	if a=="p":
		return 25
	if a=="q":
		return 26
	if a=="r":
		return 27
	if a=="s":
		return 28
	if a=="t":
		return 29
	if a=="u":
		return 30
	if a=="v":
		return 31
	if a=="w":
		return 32
	if a=="x":
		return 33
	if a=="y":
		return 34
	if a=="z":
		return 35
	if a=="A":
		return 36
	if a=="B":
		return 37
	if a=="C":
		return 38
	if a=="D":
		return 39
	if a=="E":
		return 40
	if a=="F":
		return 41
	if a=="G":
		return 42
	if a=="H":
		return 43
	if a=="I":
		return 44
	if a=="J":
		return 45
	if a=="K":
		return 46
	if a=="L":
		return 47
	if a=="M":
		return 48
	if a=="N":
		return 49
	if a=="O":
		return 50
	if a=="P":
		return 51
	if a=="Q":
		return 52
	if a=="R":
		return 53
	if a=="S":
		return 54
	if a=="T":
		return 55
	if a=="U":
		return 56
	if a=="V":
		return 57
	if a=="W":
		return 58
	if a=="X":
		return 59
	if a=="Y":
		return 60
	if a=="Z":
		return 61
	if a=="-":
		return 62
	return 63


def value_to_point(a):
	if a==0:
		return "0"
	if a==1:
		return "1"
	if a==2:
		return "2"
	if a==3:
		return "3"
	if a==4:
		return "4"
	if a==5:
		return "5"
	if a==6:
		return "6"
	if a==7:
		return "7"
	if a==8:
		return "8"
	if a==9:
		return "9"
	if a==10:
		return "a"
	if a==11:
		return "b"
	if a==12:
		return "c"
	if a==13:
		return "d"
	if a==14:
		return "e"
	if a==15:
		return "f"
	if a==16:
		return "g"
	if a==17:
		return "h"
	if a==18:
		return "i"
	if a==19:
		return "j"
	if a==20:
		return "k"
	if a==21:
		return "l"
	if a==22:
		return "m"
	if a==23:
		return "n"
	if a==24:
		return "o"
	if a==25:
		return "p"
	if a==26:
		return "q"
	if a==27:
		return "r"
	if a==28:
		return "s"
	if a==29:
		return "t"
	if a==30:
		return "u"
	if a==31:
		return "v"
	if a==32:
		return "w"
	if a==33:
		return "x"
	if a==34:
		return "y"
	if a==35:
		return "z"

	if a==36:
		return "A"
	if a==37:
		return "B"
	if a==38:
		return "C"
	if a==39:
		return "D"
	if a==40:
		return "E"
	if a==41:
		return "F"
	if a==42:
		return "G"
	if a==43:
		return "H"
	if a==44:
		return "I"
	if a==45:
		return "J"
	if a==46:
		return "K"
	if a==47:
		return "L"
	if a==48:
		return "M"
	if a==49:
		return "N"
	if a==50:
		return "O"
	if a==51:
		return "P"
	if a==52:
		return "Q"
	if a==53:
		return "R"
	if a==54:
		return "S"
	if a==55:
		return "T"
	if a==56:
		return "U"
	if a==57:
		return "V"
	if a==58:
		return "W"
	if a==59:
		return "X"
	if a==60:
		return "Y"
	if a==61:
		return "Z"
	if a==62:
		return "-"
	if a==63:
		return "_"

def number_valie(myval):
	array=[0]*6
	if myval>=2**5:
		array[0]=1
		myval=myval-2**5

	if myval>=2**4:
		array[1]=1
		myval=myval-2**4

	if myval>=2**3:
		array[2]=1
		myval=myval-2**3

	if myval>=2**2:
		array[3]=1
		myval=myval-2**2

	if myval>=2**1:
		array[4]=1
		myval=myval-2**1

	if myval>=2**0:
		array[5]=1
		myval=myval-2**0

	return array



def number_to_binary(number):
	arry=[0,0,0,0,0,0]
	if number>=2**5:
		number=number-2**5
		arry[0]=1
	if number>=2**4:
		number=number-2**4
		arry[1]=1
	if number>=2**3:
		number=number-2**3
		arry[2]=1
	if number>=2**2:
		number=number-2**2
		arry[3]=1
	if number>=2**1:
		number=number-2**1
		arry[4]=1
	if number>=2**0:
		number=number-2**0
		arry[5]=1
	return arry



def binary_to_number(arry):
	value=arry[0]*(2**5)+arry[1]*(2**4)+arry[2]*(2**3)+arry[3]*(2**2)+arry[4]*(2**1)+arry[5]*(2**0)
	return value






def encode_list(pix,line):
	offset=20
	array=[0,0,0,0,0,0]
	for y in range(6):
		combo_number=0
		for x in range(offset):
			#print(offset*y+x,pix[line,offset*y+x])
			combo_number=combo_number+pix[line,offset*y+x][0]+pix[line,offset*y+x][1]+pix[line,offset*y+x][2]
		#print(combo_number,combo_number%2,line,x)
		array[y]=combo_number%2
	return value_to_point(binary_to_number(array))






def encode_line(pix,line,letter):
	offset=20
	myarray=number_to_binary(point_to_value(letter))
	for y in range(6):
		combo_number=0
		for x in range(offset):
			#print(offset*y+x,pix[line,offset*y+x])
			combo_number=combo_number+pix[line,offset*y+x][0]+pix[line,offset*y+x][1]+pix[line,offset*y+x][2]
		#print(combo_number)
		#print("new encoding")
		pixale_val= random.randint(0,offset-1)
		latter_val=random.randint(0,2)
		if myarray[y]==1:
			if combo_number%2==0:
				if pix[line,offset*y+pixale_val][latter_val]!=0:
					#print("in here",latter_val)
					if latter_val==0:
						addin=(pix[line,offset*y+pixale_val][0]-1,pix[line,offset*y+pixale_val][1]  ,pix[line,offset*y+pixale_val][2])
					if latter_val==1:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]-1,pix[line,offset*y+pixale_val][2])
					if latter_val==2:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]  ,pix[line,offset*y+pixale_val][2]-1)
				else:
					#print("in heres")
					if latter_val==0:
						addin=(pix[line,offset*y+pixale_val][0]+1,pix[line,offset*y+pixale_val][1]  ,pix[line,offset*y+pixale_val][2])
					if latter_val==1:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]+1,pix[line,offset*y+pixale_val][2])
					if latter_val==2:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]  ,pix[line,offset*y+pixale_val][2]+1)
				
				#print(pix[line,offset*y+pixale_val],addin)
				pix[line,offset*y+pixale_val]=addin
				#print(pix[line,offset*y+pixale_val],line,offset*y+pixale_val)
		if myarray[y]==0:
			if combo_number%2==1:
				latter_val=random.randint(0,2)
				if pix[line,offset*y+pixale_val][latter_val]!=0:
					if latter_val==0:
						addin=(pix[line,offset*y+pixale_val][0]-1,pix[line,offset*y+pixale_val][1]  ,pix[line,offset*y+pixale_val][2])
					if latter_val==1:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]-1,pix[line,offset*y+pixale_val][2])
					if latter_val==2:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]  ,pix[line,offset*y+pixale_val][2]-1)
				else:
					if latter_val==0:
						addin=(pix[line,offset*y+pixale_val][0]+1,pix[line,offset*y+pixale_val][1]  ,pix[lineoffset*y+pixale_val][2])
					if latter_val==1:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]+1,pix[line,offset*y+pixale_val][2])
					if latter_val==2:
						addin=(pix[line,offset*y+pixale_val][0]  ,pix[line,offset*y+pixale_val][1]  ,pix[line,offset*y+pixale_val][2]+1)
				#print(pix[line,offset+pixale_val],addin)
				pix[line,offset*y+pixale_val]=addin
				#print(pix[line,offset+pixale_val],line,offset*y+pixale_val)
	return pix




#print(point_to_value("n"))
#print(number_to_binary(point_to_value("n")))

#print(2**5)

#print(pix[0,0])


from PIL import Image
im = Image.open('Generic-Pill.jpg') # Can be many different formats.
im = im.convert("RGBA")
pix = im.load()
#print(im.size)
import random

data="somethingnew"
gonow=pix
for x in range(len(data)):
	gonow=encode_line(gonow,x,data[x])

#print()

im.save("data_photo.png", "PNG")
print("done")






















