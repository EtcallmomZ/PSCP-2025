""" ceasar """
def caesar_cipher(text, key):
    """ input """
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            char_num = ord(char) - start
            shifted_num = (char_num + key) % 26
            result += chr(shifted_num + start)
        else:
            result += char
    return result

shift_key = int(input())
message = input()

encrypted_message = caesar_cipher(message, shift_key)

print(encrypted_message)
