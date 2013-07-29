def file_words(filename):
    """ (filename) -> dict
    Counts all of the words in a file and returns a (dictionary) tally of                                     
    how many of each word in that file. Changes all words to lowercase so count                               
    is correct. Strips out !,. and ? This deals with most problems in normal writing.                         
    Does not care if words are in paragraph form or a list. Uses function count_words                             >>> count_words('wordlist1.txt') == {'crunchy': 1, 'cows': 2, 'grass': 1, 'eat': 1}                       
    True                                                                                                      
    """    
    fc = open(filename,'r')
    sl = fc.read().split()
    fc.close()
    words = count_words(sl)
    return words

def count_words(listname):
    """ (list) -> dict
    Counts all of the words in a list and returns a (dictionary) tally of
    how many of each word in that file. Changes all words to lowercase so count
    is correct. Strips out !,. and ? This deals with most problems in normal writing.
    Does not care if words are in paragraph form or a list.
    >>> count_words(['crunchy', 'cows', 'eat', 'grass', 'cows']) == {'crunchy': 1, 'cows': 2, 'grass': 1, 'eat': 1}
    True
    """
    words = {}
    for word in listname:
        lword = word.lower().strip('!,.?')
        if lword not in words:
            words[lword] = 0
        words[lword] += 1
    return words

def freq_words(file_words):
    """ Takes a dictionary of word counts and returns the ten words with highest
    frequencey in that dictionary (if less than 10 words, returns all words sorted).
    >>> freq_words({'crunchy': 4, 'cows': 2, 'grass': 7, 'eat': 1, 'messy': 5, 'spam': 10,'bird': 3, 'dead': 9, 'towel': 6, 'earth': 8, 'trouble': 12})
    [('trouble', 12), ('spam', 10), ('dead', 9), ('earth', 8), ('grass', 7), ('towel', 6), ('messy', 5), ('crunchy', 4), ('bird', 3), ('cows', 2)]

    """
    import operator
    # If just want the most common word, probably don't want to sort the whole list.
    # Not sure at what point it is more effecient to sort whole list rather than
    # get most common word multiple times, depends on total number of words. 
    sorted_words = sorted(file_words.items(), key=operator.itemgetter(1), reverse=True)
    #print(sorted_words)
    return sorted_words[:10]

if __name__ == '__main__':
    import doctest
    doctest.testmod()    
