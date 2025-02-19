"""projet QCM"""
def qcm(fichier):
	"""fonction qcm qui créer un tableau à partir d'un fichier txt"""
	with open (fichier,"r") as fichier : #ouvrir le fichier txt contenant les 30 questions
		#print (fichier)
		id=[] #créer un tableau vide
		for i in fichier:
			id.append(i) #ajouter chaque ligne du fichier dans le tableau id
		#print("id",id)
		id2=str(id) #mettre le contenu du tableau en str
		#print(type(id2))

		id21=id2.replace("[","").replace("'"," ").replace("]","").replace(",","").replace("\\n",";;").replace('"',"") #enlever les éléments en trop et remplacer le retour à la ligne

		#print("str",id2)
		#print("strclean",id21)
		#print(type(id21))

		tab = id21.split(";;") #séparer la chaine de caractère et la placer dans un tableau
		tab.remove('')
		#print("tableau final",tab) #afficher le tableau final contenant les questions et les réponses
		return(tab)
		fichier.close() #fermer le fichier

#qcm("qcm.txt")

def choixquestions(tab):
	"""fonction choixquestions qui crée un tableau contenant les positions de 10 questions choisies aléatoirement dans le tableau tab de type list"""
	l=[] #création d'un tableau vide
	longueur=len(tab)/2
	#print(longueur)
	while len(l)<10: #le tableau doit contenir 10 valeurs
		y=randint(1,longueur)
		#print("y",y)
		#print(tab[2*(y-1)])
		y=2*(y-1) #choisir les positions des questions choisies aléatoirement
		if y not in l: #évite les doublons
			l.append(y) #ajouter les positions des questions choisies dans le tableau l
	return(l)

#choixquestions()

def checkrep(l,tab):
	compteur=0 #initialiser un compteur à 0 pour les points
	#print(l)
	for i in range(10): #poser 10 questions
		#print(l[i])
		print("Q",i+1," -",tab[l[i]],"\n") #affiche le numéro de la question et la question
		#reponsejoueur = "A" #test avec reponse A imposée
		reponsejoueur=input("Quelle est votre réponse ?\n") #le joueur entre sa réponse
		if reponsejoueur==tab[l[i]+1]: #vérifier si la réponse du joueur est la bonne
			print("Bravo c'est une bonne réponse","\n","\n")
			compteur=compteur+1 #le score augmente d'un point à chaque bonne réponse
		else:
			print("Désolé c'est une mauvaise réponse, la bonne réponse était",tab[l[i]+1],"\n","\n")#afficher la bonne réponse

	print("Vous avez obtenu le score de ",compteur," sur 10") #afficher le score final du joueur


def menu():
	"""fonction menu qui permet de structurer le programme en appelant les différentes fonctions"""
	tab = qcm("qcm.txt")
	#print("essai")
	#print (tab)
	l = choixquestions(tab)
	checkrep(l,tab)

from random import *
menu()#appeler la fonction principale pour démarer le programme
