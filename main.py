import os
import requests
from time import sleep
import optparse

red     = "\033[1;31m"
yellow  = "\033[1;33m"
green   = "\033[1;32m"
cyan    = "\033[1;36m"
magenta = "\033[1;35m"

parser = optparse.OptionParser()
parser.add_option("-u", dest="url", help="url to brute")
parser.add_option("-w", dest="wordlist", help="wordlist to use")
(options, arguments) = parser.parse_args()
url      = options.url
wordlist = options.wordlist

os.system("clear")
sleep(1.5)

file  = open(wordlist, "r")
read  = file.read()
words = read.splitlines()

print(cyan,"===================================")
print(cyan,"[+] Alvo:    ", url)
print(cyan,"[+] Wordlist:", wordlist)
print(cyan,"===================================")

try:
	for word in words:
		uri = f"http://{url}/{word}"
		request = requests.get(uri)
		if request.status_code == 200:
			print(green,"[200] ==>", uri)
		if request.status_code == 301:
			print(magenta,"[301] ==>", uri)
		if request.status_code == 403:
			print(red,"[403 ==>", uri)
except:
	print(red, "[!] Não foi possível se conectar a", url)
