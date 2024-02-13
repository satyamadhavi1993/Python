
def create_fibonacci_series(n):
	a = 0
	b = 1
	
	for i in range(n):
		yield a
		a, b = b, a+b

for i in create_fibonacci_series(15):
	print(i)
	