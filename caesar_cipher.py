# Function to encrypt the message using Caesar Cipher
def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    
    return result

# Function to decrypt the message using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main function to interact with the user
def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt a message: ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (0-25): "))
    
    if choice == "encrypt":
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == "decrypt":
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted Message: {decrypted_message}")
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
