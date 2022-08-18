def is_susbstring(stri_ng, idx, substring):
	if stri_ng[idx:idx+len(substring)]==substring:
		return True
	else:
		return False


def sub_string(string, substring):
	x=0
	for i in range(len(string)):
		if is_susbstring(string, i, substring):
			x=x+1
	return x



