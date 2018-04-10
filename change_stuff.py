from os import listdir
from os import rename
from random import seed
from random import random

files = listdir("./depression")
seed()

for file in files:
	r = random()
	print("./depression/"+file, "./depression/"+str(r)+".jpg")
	rename("./depression/"+file, "./depression/"+str(r)+".jpg")

files = listdir("./depression")
i = 0
for file in files:
	print("./depression/"+file, "./depression/"+str(i)+".jpg")
	rename("./depression/"+file, "./depression/"+str(i)+".jpg")
	i += 1


a = input()
