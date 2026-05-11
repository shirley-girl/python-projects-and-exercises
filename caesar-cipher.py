"""
In this workshop, you are going to build a Caesar cipher. This is one of the simplest techniques to encrypt text, which consists of substituting each letter of the plain text with the letter found at a fixed number of positions down the alphabet. For example, with a shift of 5, a would be replaced by f, b by g and so on.

The str.maketrans() method takes two strings of equal length and returns a translation table that maps each character of the first string with the corresponding character of the second string. Each character in the translation table is stored as a Unicode ordinal, a number that uniquely identifies the character.

Example Code
lower_chars = 'abc'
upper_chars = 'ABC'

table = str.maketrans(lower_chars, upper_chars)
print(table) # {97: 65, 98: 66, 99: 67}
"""

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(encrypted_text)
print(decrypted_text)