"""
#Defi 1
liste=[]
number= int(input("entrez un nombre : "))
length=int(input("entrez une longueur : "))
for i in range(1,length+1):
	mulpitple=(number*i)
	liste.append(mulpitple)
print(liste)
"""

#Defi 2
word=input("entrez un mot : ")
liste_mot=list(word)
for i in range(len(liste_mot)-1):
	if liste_mot[i-1]==liste_mot[i]:
		liste_mot.pop(i-1)
		print(liste_mot)
mot="".join(liste_mot)
print(mot)