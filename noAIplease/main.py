import os

flag = os.environ["FLAG"]

MAGIC_WORD = "givemeflag"

if __name__ == "__main__":
    print("Magic word:")
    
    while True:
        text = input()
        if text == MAGIC_WORD:
            print(flag)
            break
        else:
            print("Incorrect! Try again.\n")