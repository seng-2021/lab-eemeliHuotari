import codecs


def encode(string):
    '''Encodes the string'''
    if not isinstance(string,str):
        raise TypeError
    origlen = len(string)
    if origlen > 1000:
        raise ValueError
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    
    pad = False
    if origlen < 1000:
        pad = True
        padding = 1000 - origlen
        string = string.ljust(padding, 'z')
    
    for character in string:
        if character == ('å' or 'ä' or 'ö'):
            raise ValueError
        if character.isalpha():
            if character.islower():
                character=character.upper()
                crypted+=codecs.encode(character,'rot13')
        elif character in digitmapping:
            crypted+=digitmapping[character] 
        else:
            raise ValueError
        
    returnstring = ""
    if pad:
        for i in range(origlen):
            returnstring += crypted[i]

    return returnstring

def decode(string):
    '''Returns the decoded string'''
    decrypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    for character in string:
        if character.isalpha():
            if character.isupper():
                character = character.lower()
                decrypted += codecs.decode(character, 'rot13')
        elif character in digitmapping:
            decrypted += digitmapping[character]
        
    return decrypted