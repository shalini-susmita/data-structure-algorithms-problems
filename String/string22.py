def unique(r):
	z=r.split(',')
	c, q=[], ''
	for i in z:
		if i not in c:
			c.append(i)
			q=q+i+', '
	return q

print(unique('red,pink,green,red,black,blue,black'))
