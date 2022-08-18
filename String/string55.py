def haystack(s,h):
	x=0
	for i in range(len(s)-len(h)+1):
		if s[i:i+len(h)]==h:
			x=i

	return x

print(haystack('abhishekabhi', 'abhi'))