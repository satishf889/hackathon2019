import time

starttime=time.localtime()
for i in range(15):
	if(i==7):
		print(starttime.tm_sec-10)