from exercice_xp import Dog
import random

class PetDog(Dog):
	def __init__(self,name, age, weight,trained=False):
		super().__init__(name, age, weight)
		self.trained=trained


	def train(self):
		print(self.bark())
		self.trained=True

	def play(self,*args):
		t=""
		for nom in args:
			t=t+" "+nom.name
		return f"{self.name} {t} jouent ensemble"

	def do_a_trick(self):
		if self.trained==True:
			action=[f"<< {self.name} >>  does a barrel roll ",f"<< {self.name} >> stands on his back legs",f"<< {self.name} >> shakes your hand",f"<< {self.name} >> plays dead"]
		return random.choice(action)



	
d=PetDog("Bob",7,17)
d1=PetDog("Blacky",10,7)
d2=PetDog("Boby",2,11)
d3=PetDog("Pat",1,6)
"""
d1.train()
"""
#print(Dogs[1].trained)

print("*********************************************")
a=d.play(d1,d2,d3)
print(a)
d.train()
#print(d.trained)
print(d.do_a_trick())

"""d1.do_a_trick()
print("*******")
d.do_a_trick()
print("*******")
d2.do_a_trick()
print("*******")
d3.do_a_trick()"""


		

