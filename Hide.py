from PIL import Image as im
import math
#FOR SOME REASON SPLIT MSG DOESN'T REPORT CORRECTLY THE VALUES OF THE BITS
class Image:#image obj
	def __init__(self,path):
		self.path=path#path to the image
		self.im=im.open(path)#get the image obj from module
		self.colors=list(self.im.getdata())#gets a sequence of pixel values in RGB format so each pixel has 3 values

	def getbits(self):
		l=0
		binari=[]
		for i in self.colors:#loops throught the pixels
			binari.append([])#for every pixel appends a list
			for j in i:#for every 1 of 3 values creates a loop
				intero=int(j)#gets the int values of the 1/3 of the pixel
				j=bin(intero)#then gets the binary

				binari[l].append(j)#puts the binary in a list
			l+=1#keeps count of the number of pixels
		return binari#returns the list of single colors (either R or G or B)

class Messagge:
	def __init__(self, msg):
		self.msg=msg
		self.bit=''.join(format(ord(i), 'b') for i in self.msg)#gets the binary of the msg
		self.length=len(self.msg)#stores the length of the messagge

	def splitmsg(self):
		slots=[]#contains the bits grouped by 2s
		j=0#index for the returned list (incremented hald the times)
		a=0#index for the input list

		nOfGroups=int(math.ceil(len(self.bit)/2))#numer of groups by two
		k=0
		for a in range(nOfGroups):#loops through the list to fill without exceeding it
			slots.append([])#appends a new list (gonna be filled with 2 elements)
			for i in range(2):
				slots[j].append(self.bit[a])#appends at the end of the newly created list a new element from self bit
				print(self.bit[a])
				a+=1#the element from self bit changes everytime where as the element from slots every two
				
			j+=1
		print(slots)
		return slots#return the bits grouped in twos
			




print("Type in a messagge to hide with only ascii: ")
m="UUUU"
print("Type in the path for the image to hide it in: ")
path="image1.jpg"

msg=Messagge(m)
print(msg.bit)
try:
	im=Image(path)
	j=0
	
	#for i in im.colors:
	#	print(i)
	#	print("\n")
	#	print(j)
	#	j=j+1
except IOError as e:
	print(e)

length=(msg.length)*7

msg.splitmsg()

#for i in im.getbits():		
#	for j in i:
		#BL=len(j)