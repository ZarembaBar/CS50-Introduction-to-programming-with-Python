from pyfiglet import Figlet
import random
import sys


figlet = Figlet()
figlet.getFonts()


if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False
else:
    sys.exit("Invalid usage")

if isRandomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    font = random.choice(figlet.getFonts())

text = input("Input: ")

print(f"Output: {figlet.renderText(text)}")
