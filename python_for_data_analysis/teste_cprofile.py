def soma(a,b):
	if ((a+b) > b * 100):
		return a+b
	return soma(a+b, b)
for i in range(10000):
	x = soma(i, i+37)
	if (x%2 !=0):
		print x
