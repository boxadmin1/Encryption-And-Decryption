BASE64_CHARS="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def to_base64(data_bytes):
    bits = 0
    bit_count = 0
    output = ""
    for byte in data_bytes:
        bits = (bits << 8) | byte
        bit_count += 8
        while bit_count >= 6:
            bit_count -= 6
            index = (bits >> bit_count) & 0x3F
            output += BASE64_CHARS[index]
    if bit_count > 0:
        index = (bits << (6 - bit_count)) & 0x3F
        output += BASE64_CHARS[index]
    while len(output) % 4 != 0:
        output += '='
    return output

def from_base64(s):
    bits = 0
    bit_count = 0
    output = []
    s = s.rstrip('=')
    for c in s:
        index = BASE64_CHARS.find(c)
        if index == -1:
            raise ValueError("Invalid character in base64 string")
        bits = (bits << 6) | index
        bit_count += 6
        if bit_count >= 8:
            bit_count -= 8
            byte = (bits >> bit_count) & 0xFF
            output.append(byte)
    return bytes(output)

def vigenere_encrypt(text,key):
    result = []
    key_length = len(key)
    for i in range(len(text)):
        t = ord(text[i])
        k = ord(key[i % key_length])
        result.append(chr((t + k) % 256))
    return ''.join(result)

def vigenere_decrypt(text,key):
    result = []
    key_length = len(key)
    for i in range(len(text)):
        t = ord(text[i])
        k = ord(key[i % key_length])
        result.append(chr((t - k) % 256))
    return ''.join(result)

def xor_encrypt(text,key):
    result = []
    key_length = len(key)
    for i in range(len(text)):
        result.append(chr(ord(text[i]) ^ ord(key[i % key_length])))
    return ''.join(result)

def pseudo_shuffle(text,key):
    text_list = list(text)
    key_sum = 0
    for c in key:
        key_sum += ord(c)
    for i in range(len(text_list)-1,0,-1):
        j = (key_sum + i*7) % (i+1)
        text_list[i], text_list[j] = text_list[j], text_list[i]
    return ''.join(text_list)

def pseudo_unshuffle(text,key):
    text_list = list(text)
    key_sum = 0
    for c in key:
        key_sum += ord(c)
    for i in range(1,len(text_list)):
        j = (key_sum + i*7) % (i+1)
        text_list[i], text_list[j] = text_list[j], text_list[i]
    return ''.join(text_list)

def encrypt(plaintext,key):
    step1 = vigenere_encrypt(plaintext,key)
    step2 = xor_encrypt(step1,key)
    step3 = pseudo_shuffle(step2,key)
    step4_bytes = step3.encode('latin1')
    return to_base64(step4_bytes)

def decrypt(ciphertext,key):
    step4_bytes = from_base64(ciphertext)
    step3 = step4_bytes.decode('latin1')
    step2 = pseudo_unshuffle(step3,key)
    step1 = xor_encrypt(step2,key)
    plaintext = vigenere_decrypt(step1,key)
    return plaintext

def main():
    while True:
        mode = input("Choose mode - (E)ncrypt or (D)ecrypt (Q to quit): ").strip().upper()
        if mode == 'Q':
            print("Exiting.")
            break
        if mode not in ('E','D'):
            print("Invalid mode, please enter E, D, or Q.")
            continue
        key = input("Enter key: ")
        if not key:
            print("Key cannot be empty.")
            continue
        if mode == 'E':
            plaintext = input("Enter plaintext to encrypt: ")
            encrypted = encrypt(plaintext,key)
            print("Encrypted text:")
            print(encrypted)
        else:
            ciphertext = input("Enter ciphertext to decrypt: ")
            try:
                decrypted = decrypt(ciphertext,key)
                print("Decrypted text:")
                print(decrypted)
            except Exception as e:
                print("Failed to decrypt. Possible wrong key or invalid ciphertext.")

if __name__=="__main__":
    main()
