"""projet test"""
"""importer fichier et split"""
def qcm(fichier): 
	"""fonction qui créer un tableau à partir d'un fichier txt"""
	with open ("qcm.txt","r") as fichier : #ouvrir le fichier txt contenant les questions
		#print (fichier.read())
		id=[] #créer un tableau
		for i in fichier:
			id.append(i) #placer chaque ligne du fichier dans un tableau
		#print("id",id)
		id2=str(id) #mettre le contenu du tableau en str
		#print(type(id2))
		
		id21=id2.replace("[","").replace("'","").replace("]","").replace(",","").replace("\\n",";;") #enlever les éléments en trop et remplacer le retour à la ligne
		
		#print("str",id2)
		#print("strclean",id21)
		#print(type(id21))
		
		x = id21.split(";;") #couper la chaine de caractère
		print("tableau final",x)
		
#qcm("qcm.txt")
           		
#"""projet test"""
#def qcm(fichier):
#	with open ("qcm.txt") as fichier :
#		print ("prout5555555",fichier.read())
		
#qcm("qcm.txt")

"""projet test"""
#def qcm(fichier):
#	with open ("qcm.txt"):
#		fichier= open("qcm.txt","r")
#		print ("prout",fichier.read())
#		txt=[]
		
#		txt=fichier.read().split(";;")
#		print("crotte",txt)
		
#qcm("qcm.txt")

"""projet test"""
#def qcm(fichier):
#	fichier= open("qcm.txt","r")
#	print ("prout",fichier.read())
#	txt=[]
		
#	txt=fichier.read().split(";;")
#	print("crotte",txt)
		
#qcm("qcm.txt")


#fichier = open('qcm.txt')
#for word in fichier.read().split():
#    print(word)
    
    

#		for word in fichier.read().split(";;"):
#			print("00000000000000",word)
			
			
			
			
#def qcm(fichier):
#	with open("qcm.txt","r") as fichier:
#		id=[]
#		for i in fichier:
#			id.append(i)
#	print(id)
	
	#sp=id

	#id=id.split(";;")
	#print(id)
	
		
#qcm("qcm.txt")

#id = "welcome to the jungle"
#print(type(id))
#x = id.split()

#print(x)

#lst = ["o", "l", "y", "g", "r", "i", "m"]
#chn = "".join(lst)
 
#print(chn)


"""projet test"""
"""importer fichier et split"""
#def qcm(fichier):
#	with open ("qcm.txt","r") as fichier :
#		x = fichier.split(";;")
#		print("slpi",x)
		
		
#qcm("qcm.txt")

"""projet test"""
"""importer fichier et split"""
#def qcm(fichier):
#	with open ("qcm.txt","w") as fichier :
#		x=str(fichier)
#		sp=x.split(";;")
#		print(sp)
		
#qcm("qcm.txt")

#fichier=open('qcm.txt', 'r')
#word=fichier.readline()
#print ("jf",word)
"""projet test"""
"""importer fichier et split"""
def qcm(fichier):
	with open ("qcm.txt","r") as fichier :
		#print (fichier.read())
		id=[]
		for i in fichier:
			id.append(i)
		print("id",id)
		id2=str(id)
		#print(type(id2))
		
		id21=id2.replace("[","")
		print(id21)
		id22=id21.replace("'","")
		print(id22)
		id23=id22.replace("]","")
		print(id23)
		id24=id23.replace("\n",";;")
		
		print("str",id2)
		print("strclean",id24)
		print(type(id24))
		#x = id22.split(";;")
		#print("hd",x)
	#quch=[x[0],x[2]]
	#print(quch)
		
		
#qcm("qcm.txt")

"""projet test"""
"""importer fichier et split"""
def qcm(fichier):
	with open ("qcm.txt","r") as fichier :
		#print (fichier.read())
		id=[]
		for i in fichier:
			id.append(i)
		print("crotte",id)
		id2=str(id)
		print("rez",id2)
		x = id2.split(";;")
		print("hd",x)
	quch=[x[0],x[2]]
	print(quch)
		
		
#qcm("qcm.txt")


#y="['jffi;;guf\n']"
#print(type(y))
#s=y.replace("[","").replace("\n",";;")
#print(s)


"""projet test"""
"""importer fichier et split"""
def qcm(fichier):
	with open ("qcm.txt","r") as fichier :
		#print (fichier.read())
		id=[]
		for i in fichier:
			id.append(i)
		print("id",id)
		id2=str(id)
		#print(type(id2))
		
		id21=id2.replace("[","").replace("'","").replace("]","").replace("\\n",";;")
		
		print("str",id2)
		print("strclean",id21)
		print(type(id21))
		
		x = id21.split(";;")
		print("tuple",x)
	quch=[x[0],x[2]]
	print(quch)
		
		
#qcm("qcm.txt")

from random import *
def choixquestions(): 
	"""fonction qui choisie aléatoirement 10 questions"""
	
	choix=[]
	longueur=len(choix)
	while longueur != 10:
		y=randint(0, 30)
		if y not in choix:
			choix.append(y)
	print(choix)
	#quch=[x[0],x[1]]
	#print(quch)
	
#choixquestions()

"""projet test"""
"""importer fichier et split"""
def qcm(fichier): 
	"""fonction qui créer un tableau à partir d'un fichier txt"""
	with open ("qcm.txt","r") as fichier : #ouvrir le fichier txt contenant les questions
		#print (fichier.read())
		id=[] #créer un tableau
		for i in fichier:
			id.append(i) #placer chaque ligne du fichier dans un tableau
		#print("id",id)
		id2=str(id) #mettre le contenu du tableau en str
		#print(type(id2))
		
		id21=id2.replace("[","").replace("'","").replace("]","").replace(",","").replace("\\n",";;") #enlever les éléments en trop et remplacer le retour à la ligne
		
		#print("str",id2)
		#print("strclean",id21)
		#print(type(id21))
		
		x = id21.split(";;") #couper la chaine de caractère
		print("tableau final",x)
		
		x1=[x[0],x[1]]
		#print(x1)
		x2=[x[2],x[3]]
		#print(x2)
		x3=[x[4],x[5]]
		x4=[x[6],x[7]]
		x5=[x[8],x[9]]
		x6=[x[10],x[11]]
		x7=[x[12],x[13]]
		x8=[x[14],x[15]]
		x9=[x[16],x[17]]
		x10=[x[18],x[19]]
		x11=[x[20],x[21]]
		x12=[x[22],x[23]]
		x13=[x[24],x[25]]
		x14=[x[26],x[27]]
		x15=[x[28],x[29]]
		x15=[x[30],x[31]]
		x15=[x[32],x[33]]
		x16=[x[34],x[35]]
		x17=[x[36],x[37]]
		x18=[x[38],x[39]]
		x19=[x[40],x[41]]
		x20=[x[42],x[43]]
		x21=[x[44],x[45]]
		x22=[x[46],x[47]]
		x23=[x[48],x[49]]
		x24=[x[50],x[51]]
		x25=[x[52],x[53]]
		x26=[x[54],x[55]]
		x27=[x[56],x[57]]
		x28=[x[58],x[59]]
		#x29=[x[60],x[61]]
		
		final=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28]
		print("voilà",final)
		print(len(final))
		#quch=[]
		#rep=[]
		#longueur=len(x)
		#print(longueur)
		#for i in x:
		#	for i in range(longueur):
		#		quch.append(i)
		#		rep.append(i+1)
		#		print(i)
				#print("questionschoix",quch)
				#print("reponses",rep)
		
#qcm("qcm.txt")

"""projet test"""
"""importer fichier et split"""
def qcm(fichier): 
	"""fonction qui créer un tableau à partir d'un fichier txt"""
	with open ("qcm.txt","r") as fichier : #ouvrir le fichier txt contenant les questions
		#print (fichier.read())
		id=[] #créer un tableau
		for i in fichier:
			id.append(i) #placer chaque ligne du fichier dans un tableau
		#print("id",id)
		id2=str(id) #mettre le contenu du tableau en str
		#print(type(id2))
		
		id21=id2.replace("[","").replace("'","").replace("]","").replace(",","").replace("\\n",";;") #enlever les éléments en trop et remplacer le retour à la ligne
		
		#print("str",id2)
		#print("strclean",id21)
		#print(type(id21))
		
		x = id21.split(";;") #couper la chaine de caractère
		print("tableau final",x)
		
#qcm("qcm.txt")

"""projet test"""

"""importer fichier et split"""
def qcm(fichier): 
	"""fonction qui créer un tableau à partir d'un fichier txt"""
	with open (fichier,"r") as fichier : #ouvrir le fichier txt contenant les questions
		#print (fichier.read())
		id=[] #créer un tableau
		for i in fichier:
			id.append(i) #placer chaque ligne du fichier dans un tableau
		#print("id",id)
		id2=str(id) #mettre le contenu du tableau en str
		#print(type(id2))
		
		id21=id2.replace("[","").replace("'","").replace("]","").replace(",","").replace("\\n",";;").replace('"',"") #enlever les éléments en trop et remplacer le retour à la ligne
		
		#print("str",id2)
		#print("strclean",id21)
		#print(type(id21))
		
		tab = id21.split(";;") #couper la chaine de caractère
		tab.remove('')
		print("tableau final",tab)
		return(tab)
		fichier.close()
		
#qcm("qcm.txt")

def choixquestions(tab):
	"""fonction qui choisie aléatoirement 10 questions"""
	#l = [random.randint(0,60,2) for i in range(10)]
	l=[]
	longueur=len(tab)/2
	#print(longueur)
	while len(l)<10: 
		y=randint(1,longueur)
		#print("y",y)
		#print(tab[2*(y-1)])
		y=2*(y-1)
		if y not in l:
			l.append(y)
	return(l)
	print("hf",l)
	
#choixquestions()

def checkrep(l,tab):
	compteur=0
	print(l)
	for i in range(10):
		print(l[i])
		print("Q",i+1," - ",tab[l[i]],"\n")
		reponsejoueur = "A"
		reponsejoueur=input("Quelle est votre réponse ?")
		if reponsejoueur==tab[l[i]+1]:
			print("Bravo c'est une bonne réponse")
			compteur=compteur+1
		else:
			print("Désolé c'est une mauvaise réponse, la bonne réponse était",tab[l[i]+1])

	print("Vous avez obtenu le score de ",compteur," sur 10")
		
	
def menu():
	tab = qcm("qcm.txt")
	print("essai")
	print (tab)
	l = choixquestions(tab)
	checkrep(l,tab)
	
from random import *	
menu()



