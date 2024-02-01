from caesar_cipher.validate_words import validate_words

def encrypt(input, key):
    input_encrypted = ""
    number_of_letters = 26
    base_character_lower = ord('a') #lower and uppercase letters have different ASCII values
    base_character_upper = ord('A')
    
    for char in input:
        if not char.isalpha(): #do not shift non-alphabetic characters
            shifted_char = char
        if char.isalpha():
            if char.isupper(): #account for uppercase and lowercase letters
                base_character = base_character_upper
            else:
                base_character = base_character_lower
            
            relative_char_ord = ord(char) - base_character
            shifted_char_ord = (relative_char_ord + key) % number_of_letters # finds ASCII value relative to base_characer; %number_of_letters to account for key > 26
            shifted_char = chr(shifted_char_ord + base_character)
        
        input_encrypted += shifted_char
    
    return input_encrypted


def decrypt (encrypted_input, key):
    return encrypt(encrypted_input, -key)


def crack(encrypted_input):
    for i in range(26):
        decrypted_input = decrypt(encrypted_input, i)
        if validate_words(decrypted_input): #checks if truthy
            return f"Message cracked: {decrypted_input}"
    return "Unable to crack message. Might be gobbledygook."
