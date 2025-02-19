"""projet QCM"""
def qcm(fichier):
	"""fonction qui créer un tableau à partir d'un fichier txt"""
	with open (fichier,"r") as fichier : #ouvrir le fichier txt contenant les questions
		#print (fichier)
		id=[] #créer un tableau
		for i in fichier:
			id.append(i) #placer chaque ligne du fichier dans un tableau
		print("id",id)
		id2=str(id) #mettre le contenu du tableau en str
		#print(type(id2))

		id21=id2.replace("[","").replace("]","").replace(",","").replace("\\n",";;").replace('"',"") #enlever les éléments en trop et remplacer le retour à la ligne

		#print("str",id2)
		#print("strclean",id21)
		#print(type(id21))

		tab = id21.split(";;") #séparer la chaine de caractère dans un tableau
		tab.remove('')
		print("tableau final",tab) #afficher le tableau final contenant les questions et les reponses
		return(tab)
		fichier.close() #fermer le fichier

#qcm("qcm.txt")

def choixquestions(tab):
	"""fonction qui choisie aléatoirement 10 questions"""
	#l = [random.randint(0,60,2) for i in range(10)]
	l=[] #création d'une liste vide
	longueur=len(tab)/2
	#print(longueur)
	while len(l)<10: #le tableau doit contenir 10 valeurs
		y=randint(1,longueur) #choisir les positions des questions choisies aléatoirement
		#print("y",y)
		#print(tab[2*(y-1)])
		y=2*(y-1)
		if y not in l: #evite les doublons
			l.append(y)
	return(l)

#choixquestions()

def checkrep(l,tab):
	compteur=0 #initialiser un compteur pour les points
	#print(l)
	for i in range(10):
		#print(l[i])
		print("Q",i+1," -",tab[l[i]],"\n") #affiche le numéro de la question et la question
		reponsejoueur = "A"
		#reponsejoueur=input("Quelle est votre réponse ?\n") #le joueur entre une réponse
		if reponsejoueur==tab[l[i]+1]:
			print("Bravo c'est une bonne réponse","\n","\n")
			compteur=compteur+1 #le score augmente d'un point a chaque bonne réponse
		else:
			print("Désolé c'est une mauvaise réponse, la bonne réponse était",tab[l[i]+1],"\n","\n")

	print("Vous avez obtenu le score de ",compteur," sur 10") #affiche le score final du joueur


def menu():
	tab = qcm("qcm.txt")
	#print("essai")
	#print (tab)
	l = choixquestions(tab)
	checkrep(l,tab)

from random import *
menu()
