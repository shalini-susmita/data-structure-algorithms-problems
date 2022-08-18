def unique_string(s):
	a=''
	for i in s:
		if i not in a:
			a=a+i
	return True if len(a)==len(s) else False
	


def unique_substring(p):
	j=0
	for i in range(len(p)-2):
		if unique_string(p[i:i+3])==True:
			j=j+1
	return j

print(unique_substring('xyz'))
print(unique_substring('aababcabc'))