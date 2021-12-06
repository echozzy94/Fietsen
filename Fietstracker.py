import time
from colorama import init, Fore, Back, Style

########################
#####Bryant Vincken#####
########################

avgkcalburned = 560
totalkcalburned = 0
minutes = 0
seconds = 0
hours = 0
totalminutes = 0
totalhours = 0

print(Fore.GREEN + "###############")
print(Fore.GREEN + "Welkom fietsboi")
print(Fore.GREEN + "###############" + Style.RESET_ALL)

while True:
    time.sleep(1.0)
    totalkcalburned += (avgkcalburned / 60 / 60)
    seconds += 1     
    if seconds == 60:
        seconds = 0
        minutes += 1
        with open('minutes.txt', 'r') as f:
            totalminutes = f.read()
        with open('minutes.txt', 'w') as f:
            f.write(str(minutes))
    if minutes == 60:
        seconds = 0
        minutes = 0
        hours +=1
        with open('hours.txt', 'r') as f:
            totalhours = f.read()
        with open('hours.txt', 'w') as f:
            f.write(str(hours))     

    print(Fore.BLUE + "Tijd op fiets is " + str(minutes) + " minuten en " + str(seconds) + " seconden. Totaal aantal kcal verbrand is: " + str(round(totalkcalburned, 1)))
    if minutes != 0 and minutes % 5 == 0:
        print(Fore.GREEN + "Lekker bezig fietsboi, je bent al " + str(minutes) + " minuten bezig!" + Style.RESET_ALL)
