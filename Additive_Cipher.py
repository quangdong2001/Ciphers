# ADDITIVE CIPHER
# It's implemented by NGUYEN QUANG DONG in Group 11.

# the first we need to find plus inverse
# function to find plus inverse

def plus_Inverse(Key, doimain):
    return doimain - Key

#the next we create function to encrypt PlaintText
def encrypt_AdditiveCipher(data, Key):
    data_encrypt = ""
    for i in range(len(data)):
        if(data[i].isupper()):
            a = 65 + (((ord(data[i]) + Key) - 65) % 26)
            data_encrypt += chr(a)
        else:
            a = 90 + (((ord(data[i]) + Key) - 90) % 26)
            data_encrypt += chr(a)
    return data_encrypt
        
#next we create function to decrypt CipherText follow AdditiveCipher type
def decrypt_AdditiveCipher(data, Key):
    data_decrypt = ""
    plus_InverseKey = plus_Inverse(Key, 26)
    for i in range(len(data)):
        if(data[i].isupper()):
            a = 65 + (((ord(data[i]) + plus_InverseKey) - 65) % 26)
            data_decrypt += chr(a)
        else:
            a = 90 + (((ord(data[i]) + plus_InverseKey) - 90) % 26)
            data_decrypt += chr(a)
    return data_decrypt

# function main

if __name__ == '__main__':
    #data = input("Enter your PlainText: PlainText = ")
    #key = int(input("Enter your key: key = "))
    data_encrypt = encrypt_AdditiveCipher("VIETNAM", 5)
    print("PlainText after encrypt: " + data_encrypt)
    data_decrypt = decrypt_AdditiveCipher(data_encrypt, 5)
    print("CipherText after decrypt: " + data_decrypt)

