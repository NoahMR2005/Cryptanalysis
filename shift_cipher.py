# define the key to be used for encryption and decryption. the keyspace is very small, only 26 keys for the english alphabet.
# the specific cryptosystem with k=3 is called the Caesar Cipher since Julius Caeser reportedly used it to encrypt messages.
k = 11

# define the code to translate english characters to integer values
code = {"a": 0, "b": 1, "c": 2, "d": 3,
        "e": 4, "f": 5, "g": 6, "h": 7,
        "i": 8, "j": 9, "k": 10, "l": 11,
        "m": 12, "n": 13, "o": 14, "p": 15,
        "q": 16, "r": 17, "s": 18, "t": 19,
        "u": 20, "v": 21, "w": 22, "x": 23,
        "y": 24, "z": 25}

# also need another dict for converting the other way (faster lookup)
reverse_code = {}

for key, value in code.items():
    reverse_code[value] = key

# message must be all lowercase and only the 26 letters of the alphabet (no punctuation)
# N.B. the input message can have spaces included, but the output message will not include spaces
message = "do not drink the kool aid"

# write a function to take the original message and create a list where each item is a letter and spaces are omitted completely from the list
def chunk_message(message):
    chunks = []
    for i in message:
        if i == " ":
            pass
        else:
            chunks.append(i)
    return chunks

# convert the aforementioned list from characters to integers according to the "code" dictionary
def chars_to_nums(chunks):
    new_message = [code.get(i, i) for i in chunks]
    return new_message

# inverse of the previous function, used for decoding the message
def nums_to_chars(num_chunk):
    recovered_message = [reverse_code.get(i, i) for i in num_chunk]
    return recovered_message

# converts the list of characters to a string so that the message can be output as a string for easier reading
def list_to_string(list_message):
    recovered_string = ""
    for i in list_message:
        recovered_string += str(i)
    return recovered_string

# encrypt the input x by 'shifting' by the key value
def encrypt(x, k):
    return (x + k) % 26

# decrypt the encrypted value y by undoing the shift in the encrypt function
def decrypt(y, k):
    return (y - k) % 26

# utilize the 'encrypt' function to iterate through a list and encrypt each entry
def encrypt_message(plaintext, k):
    cipher_text = []
    for i in plaintext:
        cipher_text.append(encrypt(i, k))
    return cipher_text

# utilize the 'decrypt' function to iterate through a list and decrypt each entry
def decrypt_message(ciphertext, k):
    plain_text = []
    for i in ciphertext:
        plain_text.append(decrypt(i, k))
    return plain_text

def main_encrypt(message, k):
    m = chunk_message(message)
    m2 = chars_to_nums(m)
    e = encrypt_message(m2, k)
    e_letters = nums_to_chars(e)
    e_letters_string = list_to_string(e_letters)
    return e_letters_string

def main_decrypt(cipher_text, k):
    m0 = chunk_message(cipher_text)
    m20 = chars_to_nums(m0)
    d = decrypt_message(m20, k)
    d_letters = nums_to_chars(d)
    d_letters_string = list_to_string(d_letters)
    return d_letters_string


if __name__ == "__main__":  
    encrypted = main_encrypt(message, k)
    print(encrypted)
    print(main_decrypt(encrypted, k))

