# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
#
# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.
#
# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

def rot13(message):
    newstr = ""
    lowercaseAlphabet = "abcdefghijklmnopqrstuvwxyz"
    uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in message:
        if uppercaseAlphabet.rfind(letter) == -1 and lowercaseAlphabet.rfind(letter) == -1:
            newstr += letter
        elif letter == letter.upper():
            newstr += uppercaseAlphabet[uppercaseAlphabet.rfind(letter)-13]
        else:
            newstr += lowercaseAlphabet[lowercaseAlphabet.rfind(letter)-13]
    return newstr