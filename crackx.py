import hashlib
import sys
import time
from colorama import init, Style, Fore
import re
import os

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
 CCCC   RRRRR    AAAAA   CCCC  K   K     X   X
C       R   R   A     A C      K  K       X X
C       RRRRR   AAAAAAA C      KK     -    X
C       R  R    A     A C      K  K       X X
 CCCC   R   R   A     A  CCCC  K   K     X   X
                                              -CRACK X

    """)

print(Fore.RED + Style.BRIGHT + "Hash Cracker -By Faijas")
print(Fore.YELLOW + "----------------------------------------------------")

#  Validate if the given string is a 32-character MD5 hash.


def is_valid_hash(hash_str):

    return bool(re.match(r'^[a-fA-F0-9]{32}$', hash_str))


# loop
while True:
    hash_pass = input(Fore.BLUE + "Enter the hashed password to crack: ")

    if is_valid_hash(hash_pass):
        break
    else:
        print(Fore.RED + "\nInvalid hash format. Please provide a valid 32-character MD5 hash.\n")

# word list choosing

while True:

    print(Fore.YELLOW + "----------------------------------------------------\n")
    if "retry" in locals():
        wl = input(
            Fore.BLUE+"Please enter a valid wordlist name or press enter to use the default:")
    else:
        wl = input(
            Fore.BLUE+"Enter the word list name |Example: wordlist.txt | or if you want to use default word list just press enter:")

    if wl == "":
        wordlist = os.path.join("wordlists", "wordlist.txt")
        print(Fore.GREEN + "\nUsing default wordlist: wordlist.txt\n")
        break
    else:
        path = os.path.join("wordlists", wl)

        if os.path.exists(path):
            wordlist = os.path.join("wordlists", wl)
            print(Fore.GREEN + f"\nUsing custom wordlist: {wl}\n")
            break
        else:
            print(Fore.RED + "\nError: File not found.\n")
            retry = True


spinner = ['|', '/', '-', '\\', '|', '/', '-', '\\']


# crack
def pass_crack(hash_pass, wordlist):

    with open(wordlist, "r", encoding="ISO-8859-1") as file:
        total_lines = sum(1 for line in file)
    with open(wordlist, "r", encoding="ISO-8859-1") as file:
        line_count = 0

        for word in file:
            word = word.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            line_count += 1

            sys.stdout.write(
                f"\r{Fore.BLUE}Checking {line_count}/{total_lines} words... {spinner[line_count % len(spinner)]}")
            sys.stdout.flush()

            time.sleep(0.01)

            if hashed_word == hash_pass:
                sys.stdout.write("\r" + " " * 50)
                sys.stdout.write(
                    Fore.YELLOW + "\r==============================\n")
                sys.stdout.write(Fore.GREEN + f"Password found: {word}\n")
                sys.stdout.write(Fore.GREEN + "Cracking Complete!\n")
                sys.stdout.write(
                    Fore.YELLOW + "==============================\n")
                sys.stdout.flush()
                return word

    return None


found_pass = pass_crack(hash_pass, wordlist)

if found_pass is None:
    sys.stdout.write("\r" + " " * 50)
    print(Fore.RED+"\r\nPassword not found in wordlist.!!!!")
