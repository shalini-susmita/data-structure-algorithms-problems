def f(s):
	for i in range(len(s)//2):
		if s[i]!= s[len(s)-1-i]:
			return False
	return True


def f1(s,x,y):
	s1=s[x:y+1]
	print(f(s1))


x=input()
y=int(input())
for i in range(y):
	a=list(map(int,input().split()))
	f1(x, a[0], a[1])


