"""
# 1.
d={}
word=input("entrez un mot :  ")

# 2.
for l in word:
	ln=[]
	for i in range(len(word)):
		if l==word[i]:
			ln.append(i)
		d.update({l:ln})
print(f"\n votre mot est : {word} \n")
print(d)
"""

# Exercice 2
items_purchase = {
 "Water": "$1",
 "Bread": "$3",
 "TV": "$1000",
 "Fertilizer": "$20",
 "Apple": "$4",
 "Honey": "$3",
 "Fan": "$14",
 "Bananas": "$4",
 "Pan": "$100",
 "Spoon": "$2",
 "Phone": "$999",
 "Speakers": "$300",
 "Laptop": "$5000",
 "PC": "$1200"
}

somme=float(input("entrez la somme dont vous disposez :$ "))
liste_produit=[]
prod_liste=[]
for produit in items_purchase.keys():
	if somme>=float(items_purchase[produit][1:10000]):
		liste_produit.append(produit)

if liste_produit:
	liste_produit.sort()
	for prod in liste_produit:
		prod_liste.append(prod)
	print(f"\n Avec {somme}$ , cette liste vous interessera : \n {prod_liste}")
else:
 print("Nothing !")

