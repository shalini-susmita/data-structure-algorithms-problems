def prime(n,k=2):
	if k==n:
		return True
	if n%k==0:
		return False
	return prime(n,k+1)

print(prime(9))
print(prime(7))