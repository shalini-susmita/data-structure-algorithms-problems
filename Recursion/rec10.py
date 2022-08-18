def gcd(a,b):
	if a==0:
		return b
	if b==0:
		return a
	return gcd(b,a%b)

print(gcd(36,24))
print(gcd(25,36))
print(gcd(35,7))