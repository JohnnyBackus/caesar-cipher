def encrypt(input, key):
    encrypted_input = ""
    number_of_letters = 26
    base_character_lower = ord('a')
    base_character_upper = ord('A')
    
    for char in input:
        if not char.isalpha():
            shifted_char = char
        if char.isalpha():
            if char.isupper():
                base_character = base_character_upper
            else:
                base_character = base_character_lower
            relative_char_ord = ord(char) - base_character
            shifted_char_ord = (relative_char_ord + key) % number_of_letters
            shifted_char = chr(shifted_char_ord + base_character)
        encrypted_input += shifted_char
    
    return encrypted_input


def decrypt (input, key):
    return encrypt(input, -key)