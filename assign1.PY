#1.1: WAP to print your name three times
print("shubham sharma")
print("shubham sharma")
print("shubham sharma")

#2.1:WAP to add three numbers and print the result.
a=10
b=20
c=90
print(a+b+c)

#2.2: WAP to concatinate three strings and print the result.
a="shubh"
b="am"
c="sharma"
print(a+b+c)

#4.1: WAP to print the table of 7, 9
a=int(input("enter the number:"))  # we can input 7 and 9 respectively
for i in range(1,11,1):
  print(i*a)

#4.2: WAP to print the table of n and n is given by user.
n=int(input("enter the number:"))  
for i in range(1,11,1):
  print(i*n)

#4.3: WAP to add all the numbers from 1 to n and n is given by user.

n=int(input("enter the number:"))
sum=0
while n>0:
  sum=sum+n
  n=n-1
print(sum)

#5.1: WAP to find max amoung three numbers and input from user. [Try max() function]

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
print(max(a,b,c))

#5.2: WAP to add all numbers divisible by 7 and 9 from 1 to n and n is given by the user.

n = int(input("Enter the number: "))
sum = 0
for i in range(1, n + 1):
    if i % 7 == 0 and i % 9 == 0:
        sum += i

print(sum)

#5.3: WAP to add all prime numbers from 1 to n and n is given by the user.


n=int(input("enter the number:"))
sum=0
for i in range(2,n+1): #because 1 is not a prime number
  flag=0
  for j in range(2,int((i/2)+1)):
    if(i%j==0):
      flag=1
      break

  if(flag==0):
      sum=sum+i    


print(sum)
 
# 6.1 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:
            return False
    return True


def sum_prime_numbers(n):
    total_sum = 0
    for i in range(2, n + 1):  # Start at 2 because 1 is not prime
        if is_prime(i):
            total_sum += i
    return total_sum


n = int(input("Enter the value of n: "))


result = sum_prime_numbers(n)
print("The sum of all prime numbers from 1 to", n, "is:", result)

6.2# Function to add all odd numbers from 1 to n
def sum_odd_numbers(n):
    total_sum = 0
    for i in range(1, n + 1, 2):  # Start at 1, step by 2 to get only odd numbers
        total_sum += i
    return total_sum


n = int(input("Enter the value of n: "))


result = sum_odd_numbers(n)
print("The sum of all odd numbers from 1 to", n, "is:", result)	