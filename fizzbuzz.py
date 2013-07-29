def fizzbuzz(n):
    """ (int) -> NonType
    Print numbers 1 to n, except instead of the number print Fizz if number
    is divisible by, Fuzz if it is divisible by 5, and FizzBuzz if divisible
    by both.

    >>> fizzbuzz(16)
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
    16
    """
    for i in range(1,n+1):
        print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    

        
