"""
#Exercice 1

class Cat:
	def __init__(self, cat_name, cat_age):
		self.name = cat_name
	
		self.age = cat_age

cat_1= Cat("Milou",2)
cat_2= Cat("Mouss",5)
cat_3= Cat("Boo",3)

def old_cat(p1,p2,p3):
	m=max(p1.age,p2.age,p3.age)
	if m==p1.age:
		return f"The oldest cat is  {p1.name} and is {m} years old."
	elif m==p2.age:
		return f"The oldest cat is  {p2.name} and is {m} years old."
	elif m==p3.age:
		return f"The oldest cat is  {p3.name} and is {m} years old."

print(f"First cat is {cat_1.name} and have {cat_1.age} old year ")
print(f"Second cat is {cat_2.name} and have {cat_2.age} old year ")
print(f"Third cat is {cat_3.name} and have {cat_3.age} old year ")
print(f"\n {old_cat(cat_1,cat_2,cat_3)}")



#Exercice 2 : dogs

class Dog:
	def __init__(self,name,height):
		self.name=name
		self.height=height

	def bark(d):
		return f"{d.name} goes woof !"

	def jump(d):
		return f"{d.name} jumps {d.height*2} cm high !"
print("\n\tDavids_dog")
Davids_dog=Dog("Rex",50)
print(Dog.bark(Davids_dog))
print(Dog.jump(Davids_dog))

print("\n\tSarahs_dog")
Sarahs_dog=Dog("Teacup",20)
print(Dog.bark(Sarahs_dog))
print(Dog.jump(Sarahs_dog))

print("")
print("\tBigges dog \n")
m=max(Davids_dog.height,Sarahs_dog.height)
if m==Davids_dog.height:
	print(Davids_dog.name)
else:
	print(Sarahs_dog.name)

"""


#Exercice 3 Who’s The Song Producer?

class Song:
	def __init__(self,lyrics):
		self.lyrics=lyrics
	
	#@staticmethod
	def sing_me_a_song(self):
		for i in self.lyrics:
			print(i)
		
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()



