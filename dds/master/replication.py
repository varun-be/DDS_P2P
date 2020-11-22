import time
file_set = set()

def replication(l):
	global file_set
	for x in l.values():
		for i in range(len(x)-1):
			file_set.add(x[i])
	print("File set is")
	print(file_set)
	return file_set
