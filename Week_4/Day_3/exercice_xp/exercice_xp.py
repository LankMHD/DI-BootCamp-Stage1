"""
#Exercice 1

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dictionnaire=dict(zip(keys,values))
print(dictionnaire)
print(dictionnaire["Ten"])


#Exercice 2 : cinemax

tranch_1=range(3)
tranch_2=range(3,12)
tranch_3=range(12,100000)
liste_nom=[]
liste_age=[]
l1=[]
l2=[]
l3=[]
i=0
nom=""
#	2. 3.
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
for key in list(family):
	if family[key] in tranch_1:
		print(f"{key} paie 0 $")
	elif family[key] in tranch_2:
		print(f"{key} paie 10 $")
	elif family[key] in tranch_3:
		print(f"{key} paie 15 $")
# 4. impression de la facture finale
print(f"\n=======facture : {10*2+15*2} $")

#	5.
accord=input("**********tape OK pour commencer et autre chose pour arreter : ")

print("========================== ")
while accord.capitalize()=="Ok":
	nom=input("entrez le nom d'une personne : ")
	age=int(input("entrez l'age de la personne : "))
	print("========================== ")
	accord=input("**********tape OK pour continuer : ")
	print("========================== ")
	liste_nom.append(nom)
	liste_age.append(age)
famille=dict(zip(liste_nom,liste_age))
for key in liste_nom:
	if famille[key] in tranch_1:
		print(f"{key} paie 0 $")
		l1.append(famille[key])
	elif famille[key] in tranch_2:
		print(f"{key} paie 10 $")
		l2.append(famille[key])
	elif famille[key] in tranch_3:
		print(f"{key} paie 15 $")
		l3.append(famille[key])
prix_total=0*len(l1)+10*len(l2)+15*len(l3)
print(f"\n\t la famille paie au total : {prix_total} $")



# Exercice 3 : Zara

#2. creation du dictionnaire
brand={"name":"Zara","creation_date": 1975,"creator_name": "Amancio Ortega Gaona","type_of_clothes": ["men","women", "children", "home"],"international_competitors": ["Gap", "H&M", "Benetton"],"number_stores": 7000,"major_color":[{"France": "blue"},{
"Spain": "red"},{"US": ["pink", "green"]}]}

#3. changement du number_stores en 2
brand.update({"number_stores":2})
#print(brand)

#4.
cl=brand["type_of_clothes"] 
print(f"Les clients de zara son : {cl}")

#5.
brand.update({"country_creation":"Spain"})

#6.
if "international_competitors" in list(brand):
	brand["international_competitors"].append("Desigual")
print(brand)

#7.
del(brand["creation_date"])

#8.
a=brand["international_competitors"][2]
print(a)
print("*****")
#9.
b=brand["major_color"][2]["US"][1]
print(b)

#10.
print(len(brand))
print("******")


#11. 
print(f"les clés de 'brand' sont : {list(brand)}")

print("********")
#12. 
more_on_zara={"creation_date":1975,"number_stores":10000}

#13. 
brand.update(more_on_zara)

#14.
d=brand["number_stores"]
print(d)

# on remarque qu'à la place de 2 on voit 10000
"""

#Exercice 4 : les personnages Disney
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
mini=int(input("entrez le plus petit chiffre que vous desirez : "))

chiffre=list(range(mini,mini+5))
#	1.
for i in chiffre:
	disney_users_A=dict(zip(users,chiffre))
print(disney_users_A)
print()
#	2.
for j in chiffre:
	disney_users_B=dict(zip(chiffre,users))
print(disney_users_B)
print()
#	3.
users.sort()
for k in chiffre:
	disney_users_C=dict(zip(users,chiffre))
print(disney_users_C)

#	4.
#		4.1
users_i=[]
for nom in users:
	list(nom)
	if "i" in list(nom):
		users_i.append(nom)
		chiffre_1=range(len(users_i))
print(dict(zip(users_i,chiffre_1)))

#	4.2
users_j=[]
for nom in users:
	if  list(nom)[0]=="M" or list(nom)[0]=="P":
		users_j.append(nom)
		chiffre_2=range(len(users_j))
print(dict(zip(users_j,chiffre_2)))