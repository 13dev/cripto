import string

alphabet = list(string.ascii_lowercase)


def encode(raw_text, k):
    """
    This function will encode the raw_text using cesar algorithm
    :param raw_text: text to be encoded
    :param k: level of shift on alphabet
    :return: return string encoded.
    """
    result = []
    for index, item in enumerate(raw_text):
        # if input letter is not in alphabet
        if not (item in alphabet):
            return 'Char not found.'

        new_position = (alphabet.index(item) + k) % 26
        encoded_letter = alphabet[new_position]
        result.append(encoded_letter)

    result = ''.join(result).upper()
    return result


def decode(encrypted_string, k):
    result = []
    for index, item in enumerate(encrypted_string):
        # if input letter is not in alphabet
        if not (item in alphabet):
            return 'Char not found.'

        # subtract the position of encoded text letter on alphabet with amount of k
        new_position = (alphabet.index(item) - k) % 26
        result.append(alphabet[new_position])

    return ''.join(result).upper()


encoded_text = encode(input("Encode text:").lower(), 3)
print(encoded_text)

decoded_text = decode(input("Decode text:").lower(), 3)
print(decoded_text)
print("\n")
