from random import choice
from string import ascii_uppercase

def encrypt(key, msg):
    upper = msg.upper()
    encrypted = ""
    keyInc = 0
    i = 0
    while i < len(upper):
        if(upper[i] == " "):
            encrypted += " "
            i += 1
            continue
        else:
            # get ascii number based off encryption char and key char
            asciiNum = (ord(upper[i]) + ord(key[keyInc]))
            # make sure ascii is between CAPITAL letters
            while asciiNum > 90: 
                diff = asciiNum - 90 
                asciiNum = diff + 64
            # convert new ascii number to character
            encryptedLetter = chr(asciiNum)
            encrypted += encryptedLetter
        keyInc += 1
        i += 1
        if keyInc == len(key)-1: keyInc = 0

    return encrypted



def decrypt(key, encrypted):
    decrypted = ""
    keyInc = 0
    i = 0
    while i < len(encrypted):
        # ignores spaces and just creates space in decryption
        if(encrypted[i] == " "):
            decrypted += " "
            i += 1
            continue
        else:
            # get ascii number based off encryption char and key char
            asciiNum = ord(encrypted[i]) - ord(key[keyInc])
            # make sure ascii is between CAPITAL letters
            while asciiNum < 65: 
                diff = asciiNum - 64 
                asciiNum = 90 + diff  
            # convert new ascii number to character
            decryptedLetter = chr(asciiNum)
            decrypted += decryptedLetter
        keyInc += 1
        i += 1
        if keyInc == len(key)-1: keyInc = 0

    return decrypted

def randomKey():
    return ''.join(choice(ascii_uppercase) for i in range(12))


# declare secret message and key
key = randomKey()
key2 = randomKey()
msg = "VIGENERECIPHER"
msg2 = "SECRET TEXT"

# call functions to encrypt and decrypt with key as encryption key
encrypted = encrypt(key,msg)
decrypted = decrypt(key,encrypted)
encrypted2 = encrypt(key2,msg2)
decrypted2 = decrypt(key2,encrypted2)


# print out the original, encrypted and decrypted strings.
print("Key:\t")
print(key)
print("original:\t")
print(msg)
print("encrypted:\t")
print (encrypted)
print("decrypted:\t")
print(decrypted)

print("\nKey2:\t")
print(key2)
print("original 2:\t")
print(msg2)
print("encrypted 2:\t")
print (encrypted2)
print("decrypted 2:\t")
print(decrypted2)
