import random
print("*******question 1 \n\n")
chaine=input("entrez une chaine de caractere : ")

while (len(chaine))!=10:
	if (len(chaine))<10:
		print("chaine pas assez longue \n")
		chaine=input("entrez une chaine de caractere : ")
	else:
		print("chaine trop longue \n")
		chaine=input("entrez une chaine de caractere : ")
print("*******question 2 \n\n")
print("La premiere lettre est la est <",chaine[0],"> et la derniere lettre est <",chaine[-1],">\n\n")
print("*******question 3 \n\n")
c=""
for l in chaine:
	c=c+l
	print(c)
	print()
	print()
print("*******question 4\n\n")
m=list(chaine)
random.shuffle(m)
ch="".join(m)
print(ch)
	