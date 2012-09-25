import hashlib
import string

import basicDB

def generate_strings(digits):
    '''Generates a list of all possible lowercase ascii characters up to the 
    digits limit. Don't do anything too high, or it will take forever.'''
    letters = string.ascii_lowercase
    seed = [x for x in letters]
    
    for x in range(digits):
        temp = seed
        for y in xrange(len(temp)):
            for z in xrange(26): # If you change the size of seed, change this to equal len(seed)
                seed.append(temp[y] + letters[z])
            
    return seed
    
def generate_hash(value):
    ''' Takes a string value and computes the hexdigest (sha1) for that 
    value. Returns hexdigest in string format.'''
    digest = hashlib.sha1()
    digest.update(value)
    return digest.hexdigest()