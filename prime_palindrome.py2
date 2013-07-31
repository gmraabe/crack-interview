def isprime(num):
   """
   int -> bool
   checks if a number is prime, only need to check odd numbers, and numbers less
   than half the number.
   >>> isprime(5)
   True
   >>> isprime(10)
   False
   """
   if num % 2 == 0:
      return False
   for i in range(3,num//2 + 1,2):
      if (num % i == 0):
         return False
   return True

def ispalindrome(num):
   """
   int -> bool
   checks if a number is a palindrome, only need to check numbers with more than one
   digit. 
   >>> ispalindrome(123)
   False
   >>> ispalindrome(121)
   True
   """
   return num == int(str(num)[::-1])


def prime_palindrome():
   """
   () -> int
   Write a program to determine the biggest prime palindrome under 1000.
   >>> prime_palindrome()
   929
   """
   # only need to look at odd numbers.
   t = True
   i = 999
   while t:
      if isprime(i):
         if ispalindrome(i):
            return i
      i -= 2

print prime_palindrome()
      
if __name__ == '__main__':
    import doctest
    doctest.testmod()    


