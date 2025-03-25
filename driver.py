# driver.py
import subprocess
import encryption
import sys

global filename
global passwordHistory
passwordHistory = set()
password = False

# Expect one argument: the filename to pass to logging.py

if len(sys.argv) != 2:
    sys.exit("Usage: python driver.py <filename>")

filename = sys.argv[1]


#INITIALIZES NEW LOG FILE AND REMOVES OLD LOGS
fileTmp = open(filename, "a+")
fileTmp.close()
user_inputs = """!INIT_COMMENT!
QUIT
"""
# Run logging.py and pass the filename as argument
subprocess.run(["python", "logging.py", filename],
                input=user_inputs,
                text=True)

#Easy to call function to call to write to file
def writeToFile(textToWrite):
    user_inputs = textToWrite+"""\nQUIT\n"""
    subprocess.run(["python", "logging.py", filename],
                input=user_inputs,
                text=True)

# Run logging.py and pass the filename as argument
def displayMenu():
    print("-" * 50)
    print("{:^50}".format("Menu"))
    print("-" * 50)
    print()
    print("password - set the password for encryption/decryption")
    print("encrypt  - encrypt a string")
    print("decrypt  - decrypt a string")
    print("history  - show history")
    print("quit     - quit program")
    print()
    print("-" * 50)

def isValidLetterStr(prompt):
    while True:
        testStr = input("Please enter your "+prompt+" string: ")

        if testStr.isalpha():
            return testStr.upper()
        else:
            print("Please ensure your selected "+prompt.lower()+" only contains letters.")


def savedPasswordMenu():
    passwordOptions = list(passwordHistory)  # convert to list for indexing

    print("-" * 40)
    print("{:^40}".format("History"))
    print("-" * 40)

    for i, item in enumerate(passwordOptions, start=1):
        print(f"{i}. {item}")
    
    go_back_option = len(passwordOptions) + 1
    print(f"{go_back_option}. <GO BACK>")
    print("-" * 40)

    while True:
        user_input = input("Select a saved password by number: ")

        if user_input.isdigit():
            selection = int(user_input)
            if 1 <= selection <= len(passwordOptions):
                print(f"You selected: {passwordOptions[selection - 1]}")
                return passwordOptions[selection - 1]
            elif selection == go_back_option:
                newPassword = isValidLetterStr("password")
                passwordHistory.add(newPassword)
                return(newPassword)

        print("Invalid input. Please enter a number from the list.")



def passwordSelect():
    while True:
        if len(passwordHistory) > 0:
            recoverPassword = input("Would you like to use a passkey saved in history> (y/n)").strip().upper()
            if recoverPassword == "Y":
              return(savedPasswordMenu())

            elif recoverPassword == "N":
                newPassword = isValidLetterStr("password")
                passwordHistory.add(newPassword)
                return(newPassword)
            else:
                print("ERROR: Please ensure that you input only Y OR N.")

        else:
                newPassword = isValidLetterStr("password")
                passwordHistory.add(newPassword)
                return(newPassword)


def extract_encryption_outputs():
    results = []

    with open(filename, "r") as file:
        for line in file:
            if "[ENCRYPT]" in line or "[DECRYPT]" in line:
                words = line.strip().split()
                if words:  # ensure there's at least one word
                    results.append(words[-1])  # get the last word
    return results


def encryptDecryptMenu(CryptionType):
    # Extract lines with [ENCRYPT] or [DECRYPT]
    results = []
    with open(filename, "r") as file:
        for line in file:
            if "[ENCRYPT]" in line or "[DECRYPT]" in line:
                words = line.strip().split()
                if words:
                    results.append(words[-1])  # grab last word

    # Display the menu
    print("-" * 50)
    print("{:^50}".format("HISTORY ENCRYPTIONS/DECRYPTIONS"))
    print("-" * 50)

    for i, item in enumerate(results, start=1):
        print(f"{i}. {item}")

    go_back_option = len(results) + 1
    print(f"{go_back_option}. <GO BACK>")
    print("-" * 50)

    # Input loop
    while True:
        user_input = input("Select an item by number: ")
        if user_input.isdigit():
            selection = int(user_input)
            if 1 <= selection <= len(results):
                print(f"You selected: {results[selection - 1]}")
                return results[selection - 1]
            elif selection == go_back_option:
                newCrypt = isValidLetterStr(CryptionType)

                return(newCrypt)
        print("Invalid input. Please enter a valid number.")

def showHistory():
    # Extract [ENCRYPT] and [DECRYPT] lines
    results = []
    with open(filename, "r") as file:
        for line in file:
            if "[ENCRYPT]" in line or "[DECRYPT]" in line:
                words = line.strip().split()
                if words:
                    results.append(words[-1])

    # Display menu
    print("-" * 50)
    print("{:^50}".format("HISTORY ENCRYPTIONS/DECRYPTIONS"))
    print("-" * 50)

    for i, item in enumerate(results, start=1):
        print(f"{i}. {item}")

    print("-" * 50)
    input("Press Enter to return...")



def EncryptionDecryptionSelect(CryptionType):
    while True:
        recoverCryption = input("Would you like to use a ENCRYPTION / DECRYPTION saved in history> (y/n))").strip().upper()
        if recoverCryption == "Y":
            return(encryptDecryptMenu(CryptionType))

        elif recoverCryption == "N":
            newCrypt = isValidLetterStr(CryptionType)
            return(newCrypt)
        else:
            print("ERROR: Please ensure that you input only Y OR N.")





quitProgram = False
while quitProgram == False:
    displayMenu()
    userSelect = input().strip().upper()

    if userSelect == "PASSWORD":
        writeToFile("[SET_PASSWORD] Setting passkey.")
        password = passwordSelect()
        writeToFile("[SET_PASSWORD] Success.")
        print("Current Password is: "+password)
        
    elif userSelect == "ENCRYPT":
        if password == False:
            print("ERROR: No Passkey set, please set passkey before trying to attempting to ENCRYPT")
        else:
            strToCrypt = EncryptionDecryptionSelect("ENCRYPTION")
            writeToFile("[ENCRYPT] "+strToCrypt)
            cryptedStr = encryption.encrypt(strToCrypt,password)
            print("Result : "+ cryptedStr)
            writeToFile("[ENCRYPT] Success: "+cryptedStr)

            input("Press enter to continue....")



        # isValidLetterStr("enctryption")
    elif userSelect == "DECRYPT":
        if password == False: 
            print("ERROR: No Passkey set, please set passkey before trying to attempting to DECRYPT")
        else:
            strToCrypt = EncryptionDecryptionSelect("DECRYPTION")
            writeToFile("[DECRYPT] "+strToCrypt)
            cryptedStr = encryption.decrypt(strToCrypt,password)
            print("Result : "+cryptedStr)
            writeToFile("[DECRYPT] Success: "+cryptedStr)
            input("Press enter to continue....")

    elif userSelect == "HISTORY":
        showHistory()
        pass
    elif userSelect == "QUIT":
        quit()
    else:
        print("ERROR: Input not recognized please ensure the input is one of the following (PASSWORD,ENCRYPT,DECRYPT,HISTORY,QUIT)")