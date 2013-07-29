def switch_base(n,base=2):
    """ (int) -> str
    Precondition: 1 < base < 11
    Convert an integer (base 10) into a base integer (base two is default).
    Not currently implemented for any base that requires letters, but returns
    a string, anticipating one day to do bases requiring letters.
    >>> switch_base(16)
    '10000'
    >>> switch_base(17)
    '10001'
    """
    assert 1 < base < 11, ('currently not implemented for bases less than 2 or' 
        'greater than 10, you used base {}'.format(base))

    if (n == 0):
        return '0'
    newnum = []
 
    while n:
        rem = n % base
        n = n // base
        # string or number? logic easier as string, and if base includes
        # letters, would need to anyway, but of course then we would have
        # to lookup the letters...
        newnum.append(str(rem))
    newnum.reverse()
    return ''.join(newnum)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
