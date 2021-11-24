import time
from colorama import init, Fore, Back, Style

########################
#####Bryant Vincken#####
########################

avgkcalburned = 560
totalkcalburned = 0
minutes = 0

print(Fore.GREEN + "###############")
print(Fore.GREEN + "Welkom fietsboi")
print(Fore.GREEN + "###############" + Style.RESET_ALL)

while True:
    time.sleep(60.0)
    totalkcalburned += (avgkcalburned / 60 )
    minutes += 1
    print(Fore.BLUE + "Tijd op fiets is " + str(minutes) + " minuten. Totaal aantal kcal verbrand is: " + str(round(totalkcalburned, 1)))
