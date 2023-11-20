import string

def alphabetinverse():
    alphabet = list(string.ascii_lowercase)
    alphabet.reverse()
    return ''.join(alphabet)

print(alphabetinverse())