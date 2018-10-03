#Task 3
def am(f):
	file=open(f)    #open the file
	a=[]            # create an empty list
	for line in file:
		line=line.strip()
		for i in line.split():
			if i=="global_access" or i=="fw-management_access_in":  #checks  if gaccess list  and fw mgmt
				a.append(line) #appends only on the above condition
	return a
f="running-config.cfg"
print(am(f))
