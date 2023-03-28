import os
import tarfile

for i in range(1000,0,-1):
	arch = f"{i}.tar"
	#print(arch)
	f = tarfile.open(arch)
	f.extractall()
	f.close()
	os.remove(arch)
