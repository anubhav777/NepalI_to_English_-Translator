from collections import Counter
from math import sqrt
import re

def nepali_number(word):
    ret_word=re.sub(r'[^a-z0-9 ]+','',word)
    return_word=re.sub("\s\s*" , " ", ret_word)
    return_word=return_word.strip()
    return return_word

    
def word2vec(word):


    # count the characters in word
    cw = Counter(word)
    # precomputes a set of the different characters
    sw = set(cw)
    # precomputes the "length" of the word vector
    lw = sqrt(sum(c*c for c in cw.values()))

    # return a tuple
    return cw, sw, lw

def cosdis(v1, v2):
    # which characters are common to the two words?
    common = v1[1].intersection(v2[1])
    if v1[2] != 0 and v2[2] != 0:
        
        # by definition of cosine distance we have
        return sum(v1[0][ch]*v2[0][ch] for ch in common)/v1[2]/v2[2]
    else:
        return False