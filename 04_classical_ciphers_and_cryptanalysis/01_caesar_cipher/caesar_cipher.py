def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            x = ord(ch) - ord('A')
            new_x = (x + key) % 26
            result += chr(new_x + ord('A'))

        elif ch.islower():
            x = ord(ch) - ord('a')
            new_x = (x + key) % 26
            result += chr(new_x + ord('a'))

        else:
            result += ch

    return result


message = "HELLO WORLD"
key = 3

ciphertext = encrypt(message, key)

print(ciphertext)
