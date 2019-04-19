# Modular Square Root Operation
# Goal is to learn how to solve x^2 = amodp or r = sqrt(a)modp
# My format is a^m mod p where m = (p+1)/4

a = 273
p = 3571
m = (p + 1)//4
total = a
mString=bin(m)[2:]
counter = 1

#print(mString)

for i in range(1, len(mString)):
    counter+=1
    total *= total
    if(mString[i] == '1'):
        total *= a
#print("Answer is: "+str(total))
#print("Number of Computations: "+str(counter))

A = total%p

print("One possible root is = "+str(A))
copy = A
total = A
for i in range(1, len(mString)):
    counter+=1
    total *= total
    if(mString[i] == '1'):
        total *= A
A = total%p
if A == a:
	print("Square root exists")
else:
	print("Square root does not exist")

A = p-copy
print("Another possible root is = "+str(p-copy))
total = A
for i in range(1, len(mString)):
    counter+=1
    total *= total
    if(mString[i] == '1'):
        total *= A
A = total%p
if A == a:
	print("Square root exists")
else:
	print("Square root does not exist")