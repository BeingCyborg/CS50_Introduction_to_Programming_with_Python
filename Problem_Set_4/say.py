import cowsay
import sys
if len(sys.argv)==2:
    cowsay.trex('hello, '+ sys.argv[1])

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

list = response.json()
print()
for result in list["results"]:
    print(result["trackName"])



# from pyfiglet import Figlet
# figlet=Figlet()
# print(figlet.getFonts())