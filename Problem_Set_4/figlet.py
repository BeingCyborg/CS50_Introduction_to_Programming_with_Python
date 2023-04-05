from pyfiglet import Figlet

figlet = Figlet()
import sys

if len(sys.argv) == 1:
    str = input("Input: ")
    print(figlet.renderText(str))
elif len(sys.argv) == 3 and sys.argv[1]=="-f" and sys.argv[2] in figlet.getFonts():
    str = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(str))
else:
    print('Invalid usage')
    sys.exit

