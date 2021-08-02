import subprocess
import csv
import time

print("The app is running")
file = open('/storage/emulated/0/DCIM/Python/message.txt','r')
smsmessage  = file.read()

with open('/storage/emulated/0/DCIM/Python/numbers.txt') as csvfile:
	csv_reader = csvfile.readlines()

counter = 0

num = "+525565391232"
subprocess.run(["termux-sms-send", "-n", num, smsmessage])
print("message sent to me")
for number in csv_reader:
	counter += 1
	subprocess.run(["termux-sms-send", "-n", number, smsmessage])
	print("Sent Message " + smsmessage + " to " + number)
	print (counter)
	time.sleep(7)
	if  (counter%10==0): 
		print (counter)
		subprocess.run(["termux-sms-send", "-n", num, smsmessage])
		time.sleep(7)

print("Message sending complete")
