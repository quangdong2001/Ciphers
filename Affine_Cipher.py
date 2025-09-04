# Affine Cipher 
# It's implemented by NGUYEN QUANG DONG in group 11

# The first we must define function to find UCLN to test require of Multiply inverse
def UCLN(a, b):
    if(b == 0):
        return a
    return UCLN(b, a % b)

def multiply_Inverse(a, b):
    if(UCLN(a, b) == 1):
        for i in range(b):
            if((a * i) % b == 1):
                return i

# next if function to find plus_inverse
def plus_Inverse(a, doimain):
    return doimain - a

#function to encrypt
def encrypt_Affine(data, Key):
    data_encrypt = ""
    for i in range(len(data)):
        if(data[i].isupper()):
            a = (((Key[0] * (ord(data[i]) - 65)) + Key[1]) % 26) + 65
            data_encrypt += chr(a)
        else:
            a = (((Key[0] * (ord(data[i]) - 97)) + Key[1]) % 26) + 97
            data_encrypt += chr(a)
    return data_encrypt

#define to decrypt

def decrypt_Affine(data, Key):
    data_decrypt = ""
    multiply_InverseKey = multiply_Inverse(Key[0], 26)
    plus_InverseKey = plus_Inverse(Key[1], 26)
    for i in range(len(data)):
        if(data[i].isupper()):
            a = ((multiply_InverseKey * ((ord(data[i]) - 65) + plus_InverseKey)) % 26) + 65
            data_decrypt += chr(a)
        else:
            a = ((multiply_InverseKey * ((ord(data[i]) - 97) + plus_InverseKey)) % 26) + 97
            data_decrypt += chr(a)
    return data_decrypt

if __name__ == '__main__':
    #data = input("Enter PlainText: PlainText = ")
    #key1 = int(input("Enter Key1: Key1 = "))
    #key2 = int(input("Enter Key2: Key2 = "))
    #Key = [key1, key2]
    Key = [17, 5]
    data_encrypt = encrypt_Affine("VIETNAM", Key)
    print("CipherText is: " + data_encrypt)
    data_decrypt = decrypt_Affine(data_encrypt, Key)
    print("CipherText after decrypt: " + data_decrypt)

