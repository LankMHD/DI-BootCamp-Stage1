#Old MacDonal's Farm

class Farm():
	def __init__(self,nom):
		self.nom=nom
		self.animal={}

	def add_animal(self,nom,nombre=1):
		if nom in self.animal.keys():
			self.animal[nom]+=nombre
		else:
			self.animal[nom]=nombre

	def get_info(self):
		chaine=f"{self.nom}'s Farm\n\n"
		for i in self.animal:
			chaine=chaine+f"{i}:{self.animal[i]}\n"
		chaine=chaine+"\n   E-I-E-I-O!"
		return chaine

		#Expand The Farm

	def get_animal_types(self):
		li=[]
		for nom in self.animal:
			li.append(nom)
			li.sort()
		return li

	def get_short_info(self):
		self.get_animal_types()
		message=(f"{self.nom}'s Farm has {self.get_animal_types()[0]}, {self.get_animal_types()[1]} and  {self.get_animal_types()[2]}")
		return message




macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print("********************get animal type*****************************\n")
print(macdonald.get_animal_types())
print("\n*****************get short info*******************************\n")
print(macdonald.get_short_info())
