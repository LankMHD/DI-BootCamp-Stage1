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
mot=word
for i in mot:
	mot=mot.replace(i+i,i)
print(mot)