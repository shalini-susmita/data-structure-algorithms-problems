def is_palindrome(s):
	if s[::-1]==s:
		return True
	return False

def pal(s):
	if is_palindrome(s)==True:
		return 'true'
	for i in range(len(s)):
		if is_palindrome(s[0:i]+s[i+1:len(s)])==True:
			return 'true'
	return 'false'



print(pal('abc'))
print(pal('abca'))