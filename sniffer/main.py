import os
import time

#flag = os.environ["FLAG"]

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

    with open('logs') as log_file:
        log_lines = log_file.readlines()
        password = log_lines[-1].split(";")[2]

        for log in log_lines:
            logparts = log.strip().split(";")
            print(logparts[0] + " - " + logparts[1] + ": " + logparts[2])
            time.sleep(0.1)

    print("\nAll logs have been processed.")
    print("Access with the password:")

    text = input()

    if text == password:
        print("\nAccess granted.")
    else:
        print("\nAccess denied.")