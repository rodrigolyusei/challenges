import os
import time
import csv

#flag = os.environ["FLAG"]

MAGIC_WORD = "givemeflag"

if __name__ == "__main__":
    print("Starting...")

    time.sleep(1)
    
    print('''
========================================
               █▄▀█▄ █▄▀█▄            
▄█▀▀▀ ██▀█▄ ▀▀ ██▄▄  ██▄▄  ▄█▀█▄ ▄█▀▀▄
 ▀▀█▄ ██ ██ █▄ ██    ██    ██▀▀  ██   
▀▀▀▀  ▀▀ ▀▀ ▀▀ ▀▀    ▀▀     ▀▀▀  ▀▀   
========================================
    ''')

    print("Logs are being monitored:\n")

    time.sleep(1)

    with open('logs') as logs:
        for log in logs:
            print(log.strip())