def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
                shifted = chr((ord(char) - start + shift) % 26 + start)
            else:
                start = ord('a')
                shifted = chr((ord(char) - start + shift) % 26 + start)

            result += shifted
        else:
            # Preserve spaces and other non-letter characters
            result += char

    return result

def caesar_decipher(ciphertext, shift):
    result = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
                original = chr((ord(char) - start - shift) % 26 + start)
            else:
                start = ord('a')
                original = chr((ord(char) - start - shift) % 26 + start)

            result += original
        else:
            # Preserve spaces and other non-letter characters
            result += char

    return result

def letter_frequency(text):
    frequencies = {}

    # Initialize each letter's count to 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        frequencies[letter] = 0

    # Count letters in the text
    for char in text.lower():
        if char.isalpha():
            frequencies[char] += 1

    return frequencies

def main():
    print("=== Caesar Cipher Program ===")

    # Get user input
    message = input("Enter a message: ")

    while True:
        try:
            shift = int(input("Enter a shift value: "))
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Encrypt message
    encrypted = caesar_cipher(message, shift)

    # Analyze letter frequencies
    frequencies = letter_frequency(encrypted)

    # Decrypt message
    decrypted = caesar_decipher(encrypted, shift)

    # Display results
    print("\n=== Results ===")
    print("Original Message:")
    print(message)

    print("\nCiphered Message:")
    print(encrypted)

    print("\nLetter Frequencies:")
    for letter in frequencies:
        if frequencies[letter] > 0:
            print(f"{letter}: {frequencies[letter]}")

    print("\nDeciphered Message:")
    print(decrypted)

if __name__ == "__main__":
    main()