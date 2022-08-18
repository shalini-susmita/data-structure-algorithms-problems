dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}

x=(list(dict.values()))
y=0
for i in x:
	y=len(i)+y
print(y)
