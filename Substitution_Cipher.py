#Substitution Cipher
#It's implemented by NGUYEN QUANG DONG in group 11
#Substitution Cipher is just simple replace follow given mapping
anphabe_Upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
anphabe_Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

anphabe_UpperCipher = ['E', 'P', 'K', 'O', 'H', 'A', 'T', 'X', 'W', 'R', 'N', 'Y', 'D', 'M', 'B', 'L', 'F', 'U', 'Q', 'Z', 'G', 'J', 'C', 'S', 'I', 'V']
anphabe_LowerCipher = ['e', 'p', 'k', 'o', 'h', 'a', 't', 'x', 'w', 'r', 'n', 'y', 'd', 'm', 'b', 'l', 'f', 'u', 'q', 'z', 'g', 'j', 'c', 's', 'i', 'v']

#define function to encrypt 
def encrypt_SubstitutionCipher(data):
    data_encrypt = ""
    for i in range(len(data)):
        if(data[i].isupper()):
            for j in range(26):
                if(data[i] == anphabe_Upper[j]):
                    data_encrypt += anphabe_UpperCipher[j]
                    break 
        else:
            for j in range(26):
                if(data[i] == anphabe_Lower[j]):
                    data_encrypt += anphabe_LowerCipher[j]
                    break
    return data_encrypt


#define function to decrypt
def decrypt_SubstitutionCipher(data):
    data_decrypt = ""
    for i in range(len(data)):
        if(data[i].isupper()):
            for j in range(26):
                if(data[i] == anphabe_UpperCipher[j]):
                    data_decrypt += anphabe_Upper[j]
                    break
        else:
            for j in range(26):
                if(data[i] == anphabe_LowerCipher[j]):
                    data_decrypt += anphabe_Lower[j]
                    break
    return data_decrypt


if __name__ == '__main__':
    #data = input("Enter PlainText: PlainText = ")
    data_encrypt = encrypt_SubstitutionCipher("LITHUYETMATMA")
    print("PlainText after encrypt: " + data_encrypt)
    data_decrypt = decrypt_SubstitutionCipher(data_encrypt)
    print("CipherText after decrypt: " + data_decrypt)
