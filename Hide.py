from PIL import Image as im
#Need to calculate the value of the single pixels and then edit them in the image

class Image:#image obj
	def __init__(self,path):
		self.path=path#path to the image
		self.im=im.open(path)#get the image obj from module
		self.colors=list(self.im.getdata())#gets a sequence of pixel values

	def getbits(self):
		l=0
		binari=[]
		for i in self.colors:
			binari.append([])
			for j in i:
				intero=int(j)
				j=bin(intero)
				
				binari[l].append(j)
        	l+=1
		return binari

class Messagge:
	def __init__(self, msg):
		self.msg=msg
		self.bit=''.join(format(ord(i), 'b') for i in self.msg)
		self.lenght=len(self.msg)

print("Type in a messagge to hide with only ascii: ")
m=raw_input()
print("Type in the path for the image to hide it in: ")
path=raw_input()

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

lenght=(msg.lenght)*7

print(im.colors)
#for i in im.getbits():
#	for j in i:
#		print(j)

