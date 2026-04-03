import sys

def encrypt(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
            
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# --- Main Program ---
def main():
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("Encrypted Text:", encrypted_text)
    print("Decrypted Text:", decrypted_text)


if __name__ == "__main__":
    main()