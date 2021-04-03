f = open("/home/user/level09/token")
f_content = list(f.readlines()[0])
for i in range(len(f_content)):
	if ord(f_content[i]) >= i:
		f_content[i]=chr(ord(f_content[i])-i)
print ''.join(f_content)
f.close()
