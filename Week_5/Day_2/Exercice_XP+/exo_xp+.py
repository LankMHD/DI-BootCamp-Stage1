# exercice 1 : Family

class Family():

	def __init__(self, **kwargs):
		memb=[]
		k=[]
		v=[]
		for key,value in kwargs.items():
			k.append(key)
			v.append(value)
			fam=dict(zip(k,v))
		print(fam)

Family(name="Michael",age=35,gender="Male",is_child=False)
		
