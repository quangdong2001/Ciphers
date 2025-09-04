#Vigenere_Cipher
#It's implemented by NGUYEN QUANG DONG in Group 11

#function to find plus Inverse
def plus_Inverse(a, doimain):
    return doimain - a

#function to encrypt follow Vigenere_Cipher
def encrypt_Vigenere(data, Key):
    data_encrypt = ""
    full_Key = list(Key)
    if(len(data) == len(Key)):
        full_Key = Key
    else:
        count = len(Key)
        flag = False 
        while True:
            for i in range(len(Key)):
                if(count != len(data)):
                    full_Key.append(Key[i])
                    count = count + 1
                else:
                    flag = True
                    break
            if (flag == True):
                break
    for i in range(len(data)):
        if(data[i].isupper() & full_Key[i].isupper()):
            a = (((ord(data[i]) - 65) + (ord(full_Key[i]) - 65)) % 26) + 65
            data_encrypt += chr(a)
        elif(data[i].islower() & full_Key[i].islower()):
            a = (((ord(data[i]) - 97) + (ord(full_Key[i]) - 97)) % 26) + 97
            data_encrypt += chr(a)
        elif(data[i].isupper() & full_Key[i].islower()):
            a = (((ord(data[i]) - 65) + (ord(full_Key[i]) - 97)) % 26) + 65
            data_encrypt += chr(a)
        else:
            a = (((ord(data[i]) - 97) + (ord(full_Key[i]) - 65)) % 26) + 97
            data_encrypt += chr(a)
    return data_encrypt   


#function to decrypt follow Vigenere Cipher
def decrypt_Vigenere(data, Key):
    data_decrypt = ""
    full_Key = list(Key)
    if(len(data) == len(Key)):
        full_Key = Key
    else:
        count = len(Key)
        flag = False 
        while True:
            for i in range(len(Key)):
                if(count != len(data)):
                    full_Key.append(Key[i])
                    count = count + 1
                else:
                    flag = True
                    break
            if (flag == True):
                break
    for i in range(len(data)):
        if(data[i].isupper() & full_Key[i].isupper()):
            a = 65 + (((ord(data[i]) - 65) + plus_Inverse(ord(full_Key[i]) - 65, 26)) % 26)
            data_decrypt += chr(a)
        elif(data[i].islower() & full_Key[i].islower()):
            a = 97 + (((ord(data[i]) - 97) + plus_Inverse(ord(full_Key[i]) - 97, 26)) % 26)
            data_decrypt += chr(a)
        elif(data[i].isupper() & full_Key[i].islower()):
            a = 65 + (((ord(data[i]) - 65) + plus_Inverse(ord(full_Key[i]) - 97, 26)) % 26)
            data_decrypt += chr(a)
        else:
            a = 97 + (((ord(data[i]) - 97) + plus_Inverse(ord(full_Key[i]) - 65, 26)) % 26)
            data_decrypt += chr(a)
    return data_decrypt

if __name__ == '__main__':
    #data = input("Enter PlainText: PlainText = ")
    #Key = input("Enter Key: Key = ")
    data_encrypt = encrypt_Vigenere("ILOVELITHUYETMATMA", "HAPPY")
    print("PlainText after encrypt is: " + data_encrypt)
    data_decrypt = decrypt_Vigenere(data_encrypt, "HAPPY")
    print("CipherText after decrypt is: " + data_decrypt)


