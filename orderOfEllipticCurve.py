# Finding the order/all points on elliptic curve
# y^2 = x^3 + Ax + B(mod p)

def squareAndMultiply(r, m):
	total = r
	mString = bin(m)[2:]
	for i in range(1, len(mString)):
		total *= total
		if(mString[i] == '1'):
			total *= r
	return(total)

A = 7
B = 15
p = 3571
root1 = 0
root2 = 0
r = 0
m = (p+1)//4
count = 1

for x in range(p):
	r = ((x**3) + (A*x) + B)%p
	total = squareAndMultiply(r, m)
	root1 = total%p
	root2 = p - root1

	if(squareAndMultiply(root1, 2)%p == r and squareAndMultiply(root2, 2)%p == r):
		count = count + 2
		print(str(count) + "   x: " + str(x) + "	r: " + str(r) + "	     root1: " + str(root1) + "		root2: " + str(root2))
print("Order of Elliptic Curve: " + str(count))