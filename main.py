from time import sleep
import datetime
import pyautogui as auto
import pyperclip as cb

def autoType():
    with open(messagesFilePath, "r") as f:
        for line in f.readlines():
            if len(list(filter(lambda item: item in line, "qwertyuiopasdfghjklzxcvbnm"))) == 0:
                continue
            cb.copy(line)
            auto.click(x=x, y=y)
            sleep(0.1)
            auto.hotkey("ctrl", 'v')
            sleep(0.1)
            auto.hotkey("tab")
            sleep(0.1)
            auto.hotkey("enter")
            sleep(waitingDur)
            auto.click(x=x, y=y)
            sleep(0.1)
            for i in range(4):
                auto.hotkey("shift", "tab")
                sleep(0.1)
            auto.hotkey("enter")
            sleep(0.1)
            print(">", line)
            response = cb.paste()
            with open(outputDestination + "chatGPT responses.md", 'a') as g:
                g.write(f"# {line}\n{response}\n")


"""
1. read lines of a file
	1. request input file path
	2. request output file name and folder
2. record input position
3. start a loop
4. place a message, send the message
5. wait the response to generate
6. copy the response
	1. click on the input
	2. "Ctrl + tab" 3 times
	3. "Enter"
7. add a new header in a results file with the message line and paste the response
	1. how to read the clipboard?
"""

messagesFilePath = input("Input file path: ")
outputDestination = input("Output directory: ")
waitingDur = int(input("Waiting duration (in seconds) for a response: "))

print('')
print("-"*10)
input("Open a chatGPT chatting page!")
print("-"*10)
print('')

for i in range(5):
    sleep(1)
    print(f"Place the mouse on the input field under >{4-i}< seconds", end="\r")

x, y = auto.position()

print("\n\n>>> S T A R T E D <<<\n\n")

with open(outputDestination + "chatGPT responses.md", 'a') as g:
    g.write(f"# {datetime.datetime.now().date()}\n")

try:
    autoType()
except Exception as e:
    print(e)

cb.copy(">>> D O N E :)")
auto.click(x=x, y=y)
sleep(0.1)
auto.hotkey("ctrl", 'v')

input("\n>>> D O N E :)")
