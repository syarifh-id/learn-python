def shift_cipher(text, shift):
    result = ""
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Calculate the shifted character and handle wrapping with modulo operation
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Calculate the shifted character and handle wrapping with modulo operation
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, keep it as it is
            result += char
            
    return result

# Example usage
text = "Hello, World!"
shift = 5
encrypted_text = shift_cipher(text, shift)
print("Encrypted Text: ", encrypted_text)
