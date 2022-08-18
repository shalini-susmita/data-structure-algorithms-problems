def recursive(n):
	if n>10:
		return 
	print(n)
	recursive(n+1)
		
def recursive2(n):
	if n<0:
		return
	recursive2(n-1)
	print(n)
		


def iterative():
	i=1
	while i<=10:
		print(i)
		i=i+1
# iterative()

recursive(10)
