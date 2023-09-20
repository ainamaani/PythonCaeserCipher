# Function to encrypt a plaintext using the Caesar cipher
def encrypt_caesar(plaintext, key):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = key % 26  # Calculate the effective shift amount (wrap-around)
            if char.islower():  # Check if the character is lowercase
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
                # Encrypt the lowercase character
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
                # Encrypt the uppercase character
        else:
            encrypted_char = char  # Character is not a letter, leave it unchanged
        encrypted_text += encrypted_char
    return encrypted_text

# Function to decrypt a Caesar cipher ciphertext
def decrypt_caesar(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = key % 26  # Calculate the effective shift amount (wrap-around)
            if char.islower():  # Check if the character is lowercase
                decrypted_char = chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
                # Decrypt the lowercase character
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
                # Decrypt the uppercase character
        else:
            decrypted_char = char  # Character is not a letter, leave it unchanged
        decrypted_text += decrypted_char
    return decrypted_text

# Main function to run the Caesar cipher program
def caesercipher():
    while True:
        choice = input("Choose an option (encrypt/decrypt/quit): ").lower()
        if choice == "encrypt":
            plaintext = input("Enter the plaintext: ")
            if not plaintext:
                print("Please enter something as the plaintext.\n")
                continue  # Continue the loop to re-enter plaintext
            
            key_str = input("Enter the shift value/key: ")
            if not key_str:
                print("Please enter the shift value/key.\n")
                continue
            
            try:
                key = int(key_str)  # Convert the input to an integer
            except ValueError:
                print("Invalid input. Please enter a valid integer for the shift value/key.\n")
                continue  # Handle the case where a non-integer input is provided
            
            encrypted_text = encrypt_caesar(plaintext, key)
            print("\nEncrypted text:", encrypted_text, "\n")
        elif choice == "decrypt":
            ciphertext = input("Enter the ciphertext: ")
            if not ciphertext:
                print("Please enter something as the ciphertext.\n")
                continue  # Continue the loop to re-enter ciphertext
            
            key_str = input("Enter the shift value/key: ")
            if not key_str:
                print("Please enter the shift value/key.\n")
                continue
            
            try:
                key = int(key_str)  # Convert the input to an integer
            except ValueError:
                print("Invalid input. Please enter a valid integer for the shift value/key.\n")
                continue  # Handle the case where a non-integer input is provided
            
            decrypted_text = decrypt_caesar(ciphertext, key)
            print("\nDecrypted text:", decrypted_text, "\n")
        elif choice == "quit":
            break
        else:
            print("Invalid option. Please choose 'encrypt', 'decrypt', or 'quit'.\n")

#Call the Caesercipher function when the program is run
caesercipher()

