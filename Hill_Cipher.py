#HILL CIPHER
#It's implemented by NGUYEN QUANG DONG in Group 11

#convert into Keymatrix
def key_Matrix(Key, n):
    full_Key = ([])
    count = 0
    for i in range(n):
        for j in range(n):
            if(count != len(Key)):
                full_Key[i].append(Key[count])
                count = count + 1;
            else:
                count = 0;
                full_Key[i].append(Key[count])
    return full_Key

def print_Matrix(Matrix, n):
    for i in range(n):
        for j in range(n):
            print(Matrix[i][j])
        print()

if __name__ == '__main__':
    Key = "SAD"
    full_Key = key_Matrix(Key, 3)
    print_Matrix(full_Key)