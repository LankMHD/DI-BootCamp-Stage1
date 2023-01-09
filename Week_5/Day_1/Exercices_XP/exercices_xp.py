#Exercice 1

class Cat:
	def __init__(self, cat_name, cat_age):
		self.name = cat_name
		self.age = cat_age

cat_1= Cat("Milou",2)
cat_2= Cat("Mouss",5)
cat_3= Cat("Boo",3)

def old_cat(cat1,cat2,cat3):
	m=max(cat1.age,cat2.age,cat3.age)
	if m==cat1.age:
		return f"The oldest cat is  {cat1.name} and is {m} years old."
	elif m==cat2.age:
		return f"The oldest cat is  {cat2.name} and is {m} years old."
	elif m==cat3.age:
		return f"The oldest cat is  {cat3.name} and is {m} years old."

print(f"First cat is {cat_1.name} and have {cat_1.age} old year ")
print(f"Second cat is {cat_2.name} and have {cat_2.age} old year ")
print(f"Third cat is {cat_3.name} and have {cat_3.age} old year ")
print(f"\n {old_cat(cat_1,cat_2,cat_3)}")



#Exercice 2 : dogs

class Dog:
	def __init__(self,name,height):
		self.name=name
		self.height=height