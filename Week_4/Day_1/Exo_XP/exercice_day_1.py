"""
#exercice 1 Hello word
print("Hello word \n"*4)
print()

#exercice 2
print((99**3)*8)
print()

#exercice 3 prédication des resultat

>>>5 < 3
False

>>>3 == 3
True

>>>3=="3"
False

>>>"3">3
Erreur de type

>>>"Hello"=="hello"
False


#exercice 4 La marque de mon ordinateur

computer_brand="LENOVO"
print("La marque de mon ordinateur est ","<"+computer_brand+">","ordinateur")
print()

#exercice 5 mes informations

name="Mahomed LANKOANDE"
age=22
shoe_size=44
Info="Je suis Mahomed LANKOANDE j'ai 22 ans et ma pointure es 44."
print(Info)
print()

#exercice 6 A & B

a=int(input("a= "))
b=int(input("b= "))
if a>b:
	print("Hello word")
else :
	print("__")


#exercice 7 Impair & Pair

n=int(input("entrez un nombre : "))
if n==0:
	print("<",n,">","n'est ni pair ni impair")
elif n%2==0:
	print("<",n,">", "est un nombre pair")

else:
	print("<",n,">","est un nombre impair")


#exercice 8 

nom=input("entrez votre nom :")
if nom.capitalize()=="Mahomed":
	print("Nous avons le meme nom","*--"+nom.capitalize()+"--*")
else:
	print("Nous n'avons pas le meme nom.")
"""

#exercice 9	

taille=float(input("Entrez votre taille en pouce(1 pouce=2.54cm) : "))
if (taille*2.54)>=145.0:
	print("votre taille en cm est",(taille*2.54),".")
	print("Vous etes assez grand pour rouler!")
else:
	print("votre taille en cm est",(taille*2.54),".")
	print("Vous devez grandir un peu plus pour rouler!")