def add(a,b):
	newmat = []
	for i in range(len(a)):
		ls = []
		for p,q in zip( a[i] , b[i]) :
			ls.append(p+q)
		newmat.append(ls)
	return(newmat)

a = eval(input("mat1 "))
b = eval(input('mat2 '))


print(add(a,b))

