import os, shutil

def cleanUp():
	try:
		os.remove("main.py")
	except:
		print("[1/3] Clean up failed")
	try:
		os.remove("spoofClient.py")
	except:
		print("[2/3] Clean up failed!")
	try:
		os.rmdir("screen")
	except:
		print("[3/3] Clean up failed")



def main():
	cleanUp()
	os.system("git clone https://www.github.com/DylanBruner/screen")
	shutil.move("screen/main/spoofClient.py", os.getcwd())
	os.system("sudo python spoofClient.py")

main()