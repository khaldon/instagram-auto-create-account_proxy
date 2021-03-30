fake_email = "srfessdfv"
name = "sefsfsr"
paw = "pawpawpawpaw"
i = 1

for i in range(1, 5):
	data  = [""+fake_email+"   "+name+"   "+paw]
	with open("test.txt", "a") as myfile:
	    myfile.write(fake_email+"\n")
	    myfile.write(name+"\n")
	    myfile.write(paw+"\n")
	    myfile.write("------------------------------------------------------------------------------------  \n")