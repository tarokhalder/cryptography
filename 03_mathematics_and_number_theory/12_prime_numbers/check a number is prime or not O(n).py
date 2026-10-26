def check_prime(n):
   for i in range(2 , n):
       if n % i == 0:
           return False
   return True
   
   
n = int(input())
if check_prime(n) == True:
   print("It is a Prime Number")
else:
   print("It is not a Prime Number")              
