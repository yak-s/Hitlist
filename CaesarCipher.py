def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Enter your choice: ")

        if (choice=='1')or(choice=='2'):
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            if(choice=='1'):
             encryptedText = caesar(text, shift, mode='encrypt')
             print(f"Encrypted message: {encryptedText}\n")
            else:
             decryptedText = caesar(text, shift, mode='decrypt')
             print(f"Decrypted message: {decryptedText}\n")
        
        else:
            print("Exiting the program...")
            break

def caesar(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            if char.isupper() :
                shift_base = ord('A') 
            else:
                shift_base=ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) + shift_base)
            result += shifted_char
        else:
            result += char

    return result

if __name__ == "__main__":
    main()