import random
"""
#Exercice 1
def display_message():
	return "J'ai apris les fonctions dans ce cours!"

message=display_message()
print(message)


#Exercice 2
def favorite_book(title):
	return f"Un de mes livres favoris est : < {title} >"
b_t=input("entrez le titre de votre livre favorit : ")
book_title=favorite_book(b_t)
print(book_title)


#Exercice 3

def describe_city(city,country):
	return f"< {city} > is in < {country} >"
cty=input("entrez le nom d'une ville : ")
country="BURKINA FASO"
print(describe_city(cty,country))



#Exercice 4

def nombre():
	nbr1=random.choices(range(1,100))
	nbr2=random.choices(range(1,100))
	if nbr1==nbr2:
		print("============> reussi")
	else:
		print("============> echec")
	return nbr1,nbr2

c=nombre()
print(f" les nombres sont : < {list(c)[0][0]} > et < {list(c)[1][0]} >")

#Exercice 5

def make_shirt(size,text):
	return f" La taille de la chemise est < {size} > et le texte est < {text} >"

# 3.
#shirt=make_shirt(X,Y)
text="J'aime Python"
size="xxxxl"
print(make_shirt(size,text))
# 6.
text="J'aime Python"
size="M"
print(make_shirt(size,text))
# 7.
text="DI_learnig, j'aime"
size="xxl"
print(make_shirt(size,text))



# Exercice 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
l=[]
def  show_magicians(magician_names):
	for magician in magician_names:
		print(f"\t\t {magician}")
	return 0

l.append(show_magicians(magician_names))

print("\n***************************************************************\n")
# 3.
def make_great(magician_names):
	magician_names.append("the Great")
	return magician_names

# 4.
m=make_great(magician_names)
#print(f"{m}\n\n***************************************************************\n")

# 5.
n=show_magicians(magician_names)
"""

#Exercice 7
"""import random
def get_random_temp():
	degre=random.choices(range(-10,41))
	return degre

# 2.
def main():
	temp=get_random_temp()
	if temp[0]<0:
		print("\nBrr, that's freezing ! wear some extra blayers today \n")
	elif temp[0] in range(0,17):
		print("\nQuite chilly! Don't forget your coat \n")
	elif temp[0] in range(17,24):
		print("\n ... \n")
	elif temp[0] in range(24,32):
		print("\n ***  \n")
	elif temp[0] in range(32,41):
		print("\n ---  \n")
	return f"The temperature right now is {temp[0]} degrees Celsius"

"""
#print(main())

# 4.
     # 1.




season=input("entrez la saison : ")
def get_random_temp(season):
	if season.capitalize()=="Hiver":
		deg=random.choices(range(-10,16))
	elif season.capitalize()=="Automne":
		deg=random.choices(range(17,23))
	elif season.capitalize()=="Ete":
		deg=random.choices(range(23,32))
	elif season.capitalize()=="Printemps":
		deg=random.choices(range(32,41))
	return deg
m=get_random_temp(season)
print(f"nous sommes en (au) {season} et la temperature est {float(m[0])} degre Celsius")


