import string
mat="7This$#^Is% Matr3ix#  %"
l=0
while l<(len(mat)-1):
	if mat[l] not in string.ascii_letters and mat[l+1] not in string.ascii_letters:
		mat=mat.replace(mat[l]+mat[l+1]," ")
		for j in mat:
			if j not in string.ascii_letters and j!=" ":
				mat=mat.replace(j,"")
	l=l+1
print(mat)
