from time import sleep
import datetime
import pyautogui as auto
import pyperclip as cb

def wait():
    sleep(0.1)

def autoType():
    with open(messagesFilePath, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if len(list(filter(lambda item: item in line, "qwertyuiopasdfghjklzxcvbnm"))) == 0:
                continue
            if line == '\n':
                continue
            cb.copy(line.strip())
            if (line[:10] != "**Chapter ") and (line[:8] != "Chapter "):
                auto.click(x=x, y=y)
                wait()
                auto.hotkey("ctrl", 'v')
                wait()
                auto.hotkey("tab")
                wait()
                auto.hotkey("enter")

                sleep(waitingDur)

                auto.click(x=x, y=y)
                wait()
                for i in range(4):
                    auto.hotkey("shift", "tab")
                    wait()
                auto.hotkey("enter")
                wait()
            response = cb.paste()
            with open(outputDestination + "chatGPT responses.md", 'a', encoding="utf-8") as g:
                if (line[:2] == "- "):
                    line = '#' + line[1:]
                g.write(f"# {line}\n{response}\n")
                print(">", line)


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

messagesFilePath = "C:\\Users\\IMAD\\Documents\\my programming interests\\in.txt" #input("Input file path: ")
outputDestination = "C:\\Users\\IMAD\\Documents\\my programming interests\\" #input("Output directory: ")
waitingDur = 60 #int(input("Waiting duration (in seconds) for a response: "))

print('')
print(" - "*10)
input("Open a chatGPT chatting page!")
print(" - "*10)
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
wait()
auto.hotkey("ctrl", 'v')

input("\n>>> D O N E :)")
