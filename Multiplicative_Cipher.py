#as we all know, a number in Zn have multiply inverse, gcd(a, n) = 1
#function to find UCLN a, b
def UCLN(a, b):
    if(b == 0):
        return a
    return UCLN(b, a % b)

#function to find Multiply inverse   
def multiply_Inverse(a, b):
    if(UCLN(a, b) == 1):
        for i in range(b):
            if (((a * i) % b) == 1):
                return i

#function to encrypt follow Multiplicative Cipher
def encrypt_AdditiveCipher(data, key):
    data_encrypt = ""
    for i in range(len(data)):
        if(data[i].isupper()):
            a = 65 + (((ord(data[i]) - 65) * key) % 26)
            data_encrypt += chr(a)
        else:
            a = 90 + (((ord(data[i]) - 97) * key) % 26)
            data_encrypt += chr(a)
    return data_encrypt

#function to decrypt follow Multipli Cipher 
def decrypt_AdditiveCipher(data, Key):
    data_decrypt = ""
    keyInverse = multiply_Inverse(Key, 26)
    for i in range(len(data)):
        if(data[i].isupper()):
            a = 65 + (((ord(data[i]) - 65) * keyInverse) % 26)
            data_decrypt += chr(a)
        else:
            a = 90 + (((ord(data[i]) - 97) * keyInverse) % 26)
            data_decrypt += chr(a)
    return data_decrypt
if __name__ == '__main__':
    data = input("Enter data need encrypt: data = ")
    Key = int(input("Enter your key: key = "))
    data_encrypt = encrypt_AdditiveCipher(data, Key)
    print("Data after encrypt follow AdditiveCipher: " + data_encrypt)
    data_decrypt = decrypt_AdditiveCipher(data_encrypt, Key)
    print("Data after decrypt follow AdditiveCipher: " + data_decrypt)

 
  
     


