def alpha(p):
	if 48<=ord(p)<=57:
		return p
	a=ord(p)-96
	return str(a)

def string_sum(d):
	c=0
	for i in d:
		c=c+int(i)
	return c

def alpha1(c,k):
	while k!=0:
		q=''
		for i in c:
			q=q+alpha(i)
		c=str(string_sum(q))
		k=k-1
	return int(c)	
print(alpha1('iiii', 1))
print(alpha1('leetcode', 2))
print(alpha1('zbax', 2))