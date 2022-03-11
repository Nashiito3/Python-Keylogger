
import pyperclip
import time
import logging

# esto tambien loggea los textos copiados y pegados

log_dir = ""

logging.basicConfig(filename=(log_dir + "logs.txt"))

list = []
while True:
    if pyperclip.paste() != "None":
        value = pyperclip.paste()

        if value not in list:
            list.append(value)

        print(list)

        time.sleep(300)