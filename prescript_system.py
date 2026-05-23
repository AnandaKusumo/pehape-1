import random
import string
import time
import os

CYAN = "\033[36m"
RESET = "\033[0m"

prescripts = [
    "HOLD BREATH FOR 15 SECONDS",
    "STAND FOR 1 MINUTE",
    "DRINK WATER",
    "EAT",
    "GO TO SLEEP",
    "DO HOMEWORK",
    "CODING",
    "ENTERTAIN SELF",
    "DO 20 SQUATS",
    "DO NOTHING FOR THE WHOLE DAY",
    "DO 15 PUSH UPS",
    "WALK AROUND FOR 2 MINUTES",
    "STARE AT THE WALL FOR 15 SECONDS",
    "DO CHORES",
    "CHAT SOMEONE AND TELL THEM NOTHING",
    "WATCH RANDOM VIDEOS"
]

chars = string.ascii_uppercase + string.digits + "!@#$%^&*?.,><"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def scramble_text(text):
    
    length = len(text)

    progress = 0

    while progress < 1:
        output = []

        for i in range(length):
            if random.random() < (progress):
                output.append(text[i])
            else:
                output.append(random.choice(chars))

        
        clear()

        print(CYAN + "\n|| PRESCRIPT ||" + RESET)
        print(CYAN + "".join(output) + RESET)

        progress += 0.04
        time.sleep(0.04)
    
    clear()

    print(CYAN + "\n|| PRESCRIPT ||" + RESET)
    print(CYAN + text + RESET)


command = random.choice(prescripts)

scramble_text(CYAN + "PRESCRIPT RECEIVED." + RESET)
time.sleep(0.7)
scramble_text(command)

print(CYAN + "\n Execute Prescript." + RESET)
print(CYAN + "Type: 'done'" + RESET)

answer = input(CYAN + "> " + RESET)

if answer.lower() == "done":
    scramble_text(CYAN + "CLEAR" + RESET)
else:
    scramble_text(CYAN + "EXECUTION" + RESET)