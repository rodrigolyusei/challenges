import hashlib
import hmac
import os
import secrets
import time

flag = os.environ["FLAG"]

iv = secrets.token_bytes(16)
key = secrets.token_bytes(16)
block_size = 16

def pseudo_random_function(counter):
    return hmac.new(key, counter, hashlib.sha256).digest()

def counter(message):
    encrypted = b''

    blocks = [bytes(message[i:i + block_size], 'utf-8') for i in range(0, len(message), block_size)]

    for index, block in enumerate(blocks):
        counter_block = (int.from_bytes(iv, "big") + index + 1).to_bytes(16, 'big')
        prf = pseudo_random_function(counter_block)
        encrypted += bytes(blockbyte ^ prfbyte for blockbyte, prfbyte in zip(block, prf))

    return encrypted

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

        print(log_lines[0].strip().split(";")[0] + " - " + log_lines[0].strip().split(";")[1] + ": " + log_lines[0].strip().split(";")[2])

        print("\nOops... \n")

        for log in log_lines:
            logparts = log.strip().split(";")
            message = counter(logparts[2])

            print(logparts[0] + " - " + logparts[1] + ": " + message.hex())
            time.sleep(0.1)

    print("\nAll logs have been processed.")
    print("Access with the password:")

    text = input()

    if text == password:
        print("\nAccess granted.")
        print("Congratulations! Here is your flag:")
        print(flag)
    else:
        print("\nAccess denied.")