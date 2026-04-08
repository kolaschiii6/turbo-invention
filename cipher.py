def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')

            position = ord(char) - base

            new_position = (position + shift) % 26

            result += chr(base + new_position)
        else:
            result += char

    return result


def rot13_cipher(text):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            position = ord(char) - base
            new_position = (position + 13) % 26
            result += chr(base + new_position)
        else:
            result += char

    return result

if __name__ == "__main__":
    text = input("wpisz text:")

    encrypted = caesar_cipher(text, 3, "encrypt")
    print("Caesar encrypt:", encrypted)

    decrypted = caesar_cipher(encrypted, 3, "decrypt")
    print("Caesar decrypt:", decrypted)

    rot = rot13_cipher(text)
    print("ROT13:", rot)

    print("ROT13 back:", rot13_cipher(rot))


