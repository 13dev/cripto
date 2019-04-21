import string, re


def handle_plain_text(string):

    pstring = list()
    offset = 0
    # len of string is odd?
    if len(string) % 2 != 0:
        offset = 1

    for item in range(1, len(string) + offset, 2):
        p1 = string[item-1]

        if item >= len(string):
            p2 = 'x'
        else:
            p2 = string[item]

        pstring.append([p1, p2])

    new_pstring = []

    for (index, item) in enumerate(pstring):
        if pstring[index][0] == pstring[index][1]:
            # if the letters are the same
            new_pstring.append([pstring[index][1], 'x'])
            new_pstring.append([pstring[index][1], 'x'])
            continue

        new_pstring.append(item)

    return new_pstring


def generate_matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]


def remove_duplicates(text):
    return ''.join(sorted(set(text), key=text.index))

def findposition(matrix, letter):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == letter:
                return row,col


def encrypt(text, key):
    encrypt_text = []

    for row in range(len(text)):
        (x1, y1) = findposition(key, text[row][0])
        (x2, y2) = findposition(key, text[row][1])

        if x1 == x2:
            # same row
            # if is on limit get the first position
            if y1 == 4:
                y1 = -1
            if y2 == 4:
                y2 = -1
            encrypt_text.append(key[x1][y1 + 1])
            encrypt_text.append(key[x2][y2 + 1])

        elif y1 == y2:
            #same col
            if x1 == 4:
                x1 = -1
            if x2 == 4:
                x2 = -1

            encrypt_text.append(key[x1 + 1][y1])
            encrypt_text.append(key[x2 + 1][y2])

        else:
            encrypt_text.append(key[x1][y2])
            encrypt_text.append(key[x2][y1])
    return ''.join(encrypt_text).upper()


def decrypt(text, key):

    decrypted_text = []

    for row in range(len(text)):
        (x1, y1) = findposition(key, text[row][0])
        (x2, y2) = findposition(key, text[row][1])

        if x1 == x2:
            # same row
            # if is on limit get the first position
            if y1 != 0:
                y1 -= 1
            else:
                y1 = -1

            if y2 != 0:
                y2 -= 1
            else:
                y2 = -1

            decrypted_text.append(key[x1][y1])
            decrypted_text.append(key[x2][y2])

        elif y1 == y2:
            #same col
            if x1 != 0:
                x1 -= 1
            else:
                x1 = -1

            if x2 != 0:
                x2 -= 1
            else:
                x2 = -1

            decrypted_text.append(key[x1][y1])
            decrypted_text.append(key[x2][y2])

        else:
            decrypted_text.append(key[x1][y2])
            decrypted_text.append(key[x2][y1])
    return ''.join(decrypted_text).upper()


key = input("Input a key:").lower()
plain_text = list(input("input a text to encrypt:").lower())


plain_text = handle_plain_text(plain_text)

key = remove_duplicates(key)
matrix = generate_matrix(5, 5, 0)
alphabet = string.ascii_lowercase

# matrix_value will be the key + (alphabet - key chars)
matrix_value = list(key + re.sub('['+key+']', '', alphabet))

# fill the matrix with the matrix_value
count = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        matrix[row][col] = matrix_value[count]
        count += 1

print('KEY:')
for item in range(len(matrix)):
    print(matrix[item])

print()

encrypted_text = encrypt(plain_text, matrix)
print('Encrypted text: ' + encrypted_text)

plain_text = handle_plain_text(encrypted_text.lower())

decrypted_text = decrypt(plain_text, matrix)

print('Decrypted text: ' + decrypted_text)
