from time import sleep

speed_seconds = 1 # default 1

mins = int(input("How many minutes?: "))
secs = int(input("How many seconds?: "))

while True:
	if secs != 1:
		if mins >= 1: 
			secs = secs - 1
		else:
			secs = secs - 1
		print(str(mins)+ " min " + str(secs) + " sek")
	else:
		if mins >= 1:
			mins = mins - 1
			secs = secs + 60
		else:
			print("Done")
			break
	sleep(speed_seconds)
