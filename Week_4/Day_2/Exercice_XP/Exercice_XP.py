"""
#Exercice 1: sets

my_fav_numbers={1,2,3,4,7,10,33,41,99,110,100,9,12,15}
print("1. creation de l'ensemble")
print(f" l'ensemble de mes nombres preferes est : {my_fav_numbers} \n")

print("2. ajout de 2 nouveau numeros à l'ensemble")
my_fav=list(my_fav_numbers)
my_fav.extend([45,50])
print(set(my_fav))
print()
print("3. suppression du dernier element")
my_fav.remove(my_fav[-1])
print(set(my_fav))
print()

print("4. creation de l'ensemble de mon ami")
friend_fav_numbers={6,9,77,61,34,175,342}
print(f"l'ensemble des nombres preferes de mon ami est : {friend_fav_numbers}\n")

print("5. contatenation des deux l'ensembles")
friend_fav=list(friend_fav_numbers)
our_fav_numbers=my_fav+friend_fav
print(f"l'ensemble de nos nombbres preferes est : {set(our_fav_numbers)}")


#Exercice 2 : Tuple

Non, car les Tuples sont non modifiables.


#Exercice 3 : Liste

basket=["Banana","Apples","Oranges","Blueberries"]

print("1. suppression de 'Banana'")
basket.remove(basket[0])
print(f" la nouvelle liste est : {basket} \n")

print("2. suppression de 'Myrtilles'")
print("Myrtilles n'est pas dans basket donc on aura un message d'erreur de valeur \n")

print("3. ajout de 'Kiwi' dans la liste")
basket.append("Kiwi")
print(f"la nouvelle liste est : {basket} \n")

print("4. ajout de 'Apples' au debut de la liste")
basket.insert(0, "Apples")
print(basket)
print()
print("5. nombre de 'Apples' dans la liste")
n_Apples=basket.count("Apples")
print(f"il ya {n_Apples} 'Apples' dans la liste \n")

print("6. vider la liste")
basket.clear()
print(basket)

print("7. impression de la liste")
print(basket)



#Exercice 4 : les flotteurs

1. un float est un nombre réel
	la difference entre un float et un int est que les float peuvent etre ecrit avec une virgure alors que les int sont des entiers relatifs

2. Oui, en faisant une convertion des int ou str en float
	par exemple : >>>age=26
				  >>>float(age)
				  26.0
				  >>>age="26"
				  >>>float(age)
				  26.0

3. liste=(1.5,2,2.5,3,3.5,4,4.5,5)



#Exercice 5 : boucle for

print("1. impression des toutes les valeurs entre 1 et 20\n")
for i in range(1,21):
	print(i)

print()
print("2. impression des nombres pairs entre 1 et 20 \n")
for i in range(1,21):
	if i%2==0:
		print(i)


#Exercice 6 : boucle while

nom=input("entrez votre nom : ")
while nom.capitalize()!="Mahomed":
	nom=input("entrez votre nom : ")
print()
print("******** nom correct ********")
"""

#Exercice 7: fruits preferes

print("1. fruits preferes")
fruit_pref=input("entrez votre(vos) fruit(s) prefere(s) (N.B: mettez juste un espace entre les fruits) : ")
print(f'\tvotre(vos) fruit(s) est(sont) : {fruit_pref}\n')

print("2. stockage dans un liste")
print(list(fruit_pref))
liste=fruit_pref.split(" ")
print(liste)
print()
print("3. choix")
choix=input("entrez le nom de n'importe quel fuit : ")
if choix in liste:
	print("Vous avez choisi un de vos fruits preferes! \n Prennez plaisir! \n")
else:
	print("Vous avez choisi un nouveau fruit.\n J'espere que vous appreciez!")

"""

#Exercice 8 : commande de pizza

liste_graniture=[]
graniture=""
print("1. boucle")

while graniture.capitalize()!="Quitter":
	graniture=input("entrez vos differentes graniture de ici(N.B: entrez 'Quitter' pour arreter votre liste de granitures) : ")
	print("Cette graniture sera ajoutée aux précédentes!")
	liste_graniture.append(graniture)
	q=""
	for q in liste_graniture:
		if q.capitalize()=="Quitter":
			liste_graniture.remove(q)
			print(liste_graniture)
			prix_total=10+2.5*len(liste_graniture)
			print(f"le prix total est : {prix_total}")


#Exercice 9 : Cinémax
famille=[]
l1=[]
l2=[]
l3=[]
age=0
tranch_1=range(3)
tranch_2=range(3,12)
tranch_3=range(12,1000)
while age!=-1:
	age=int(input("entrez l'age de chaque personne voulant un billet (N.B: mettez -1 pour arreterla liste de la famille) : "))
	famille.append(age)
for age in famille:
	if age in tranch_2:
		l2.append(age)
	elif age in tranch_3:
		l3.append(age)
	elif age in tranch_1:
		l1.append(age)
prix_total=0*len(l1)+10*len(l2)+15*len(l3)
famille.remove(-1)
print(famille)
print(f"nombre total de billets : {len(famille)}\n prix total :{prix_total}")


#Exercice 10 : cammande sandwich

sandwich_orders=["Tuna sandwich","Avocado sandwich","Egg sandwich","Sabih sandwich","Pastrami sandwich"]
finished_sandwches=[]
for i in range(len(sandwich_orders)):
	sandwich_prepare=sandwich_orders.pop(0)
	finished_sandwches.append(sandwich_prepare)
	print(f" J'ai fait ton : {finished_sandwches[i]}")



#Exercice 11: sandwich orders #2
sandwich_orders=["Tuna sandwich","Pastrami sandwich","Avocado sandwich","Pastrami sandwich","Egg sandwich","Sabih sandwich","Pastrami sandwich"]
finished_sandwches=[]
print("==================La charcuterie n'a plus de Pastrami\n")
while "Pastrami sandwich" in sandwich_orders:
	sandwich_orders.remove("Pastrami sandwich")
print("sandwich_orders : \n",sandwich_orders)
print()
for i in range(len(sandwich_orders)):
	sandwich_prepare=sandwich_orders.pop(0)
	finished_sandwches.append(sandwich_prepare)
print(f" finished_sandwches : \n{finished_sandwches}")

"""
