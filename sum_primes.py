def isprime(num):
   """
   int -> bool
   checks if a number is prime, only need to check odd numbers (if greater than 2), 
   and only need to try dividing by numbers less than half the number. All numbers 
   less than 2 are not prime.
   >>> isprime(5)
   True
   >>> isprime(10)
   False
   """
   if num == 2:
      return True
   if num % 2 == 0 or num < 2:
      return False
   for i in range(3,num//2 + 1,2):
      if (num % i == 0):
         return False
   return True

def sum_primes():
   """
   () -> int
   Write a program to determine the biggest prime palindrome under 1000.
   >>> sum_primes()
   3682913
   """
   sum_now = 0
   # after 2, all primes have to be odd numbers, so start the sum at 2, and then
   # loop through all odd numbers, adding them to sum_now if prime. count starts 
   # at one, because of the 2.
   i = 3
   sum_now = 2
   count = 1
   while count < 1000:
      if isprime(i):
         sum_now += i
         count += 1
      i += 2
   return sum_now

print sum_primes()
      
if __name__ == '__main__':
    import doctest
    doctest.testmod()    


