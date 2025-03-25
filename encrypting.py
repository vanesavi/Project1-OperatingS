# def logFileCaller(message):
#     command = ["python", "logging.py", "Output.txt"]

#     # Define the stdin content (this simulates user typing)
#     stdin_data = message+".\nQuit"
#     process = subprocess.run(command, input=stdin_data, text=True)



def letterToNum(letter):
    return ord(letter.upper()) - ord('A')

def numToLet(number):
    return chr(number % 26 + ord('A'))


def encrypt(plaintext, key):
    # logFileCaller("[ENCRYPT] "+plaintext)
    plaintext = plaintext.upper()
    key = key.upper()

    encrypted = []
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            plain_num = letterToNum(char)
            key_num = letterToNum(key[key_index % len(key)])
            new_num = (plain_num + key_num) % 26
            encrypted.append(numToLet(new_num))
            key_index += 1
        else:
            encrypted.append(char)
    # logFileCaller("[ENCRYPT] Success: "+"".join(encrypted))
    return ''.join(encrypted)


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    # logFileCaller("[DECRYPTED] "+ciphertext)

    decrypted = []
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            cipher_num = letterToNum(char)
            key_num = letterToNum(key[key_index % len(key)])
            new_num = (cipher_num - key_num) % 26
            decrypted.append(numToLet(new_num))
            key_index += 1
        else:
            decrypted.append(char)
    # logFileCaller("[DECRYPTED] Success: "+"".join(decrypted))
    return ''.join(decrypted)



# logFileCaller("[START] Logging Strated ")

# print(decrypt("NSZOP","HELLO"))