def caesar_cipher(text, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            position = ord(char) - base
            new_position = (position + shift) % 26
            result += chr(base + new_position)
        else:
            result += char
    return result


def rot13_encrypt(text):
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


def rot13_decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            position = ord(char) - base
            new_position = (position - 13) % 26
            result += chr(base + new_position)
        else:
            result += char
    return result

