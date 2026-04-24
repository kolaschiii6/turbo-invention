from cipher import caesar_cipher, rot13_encrypt, rot13_decrypt
def main():
    print("=== Text Encryption CLI ===")
    print("1. Caesar encrypt")
    print("2. Caesar decrypt")
    print("3. ROT13 encrypt")
    print("4. ROT13 decrypt")
    choice = input("Choose option (1-4): ")
    text = input("Enter text: ")
    if choice == "1":
        shift = int(input("Shift: "))
        result = caesar_cipher(text, shift, mode="encrypt")
    elif choice == "2":
        shift = int(input("Shift: "))
        result = caesar_cipher(text, shift, mode="decrypt")
    elif choice == "3":
        result = rot13_encrypt(text)
    elif choice == "4":
        result = rot13_decrypt(text)
    else:
        print("Invalid choice")
        return
    print("Result:", result)
if __name__ == "__main__":
    main()
