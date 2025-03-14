Name: Balakumar
Email: bala8065@gmail.com
Phno: 9790816791
Batch code: PAT-C-WE-E-B7


Task 4

You have been given a python list[10, 501, 22,37,100,999,87,351] your task is to create two list one which have all the even numbers and another list which will have all the odd numbers in it?

values= [10,501,22,37,100,999,87,351]
even =[]
odd= []


for i in values:
   if i %2==0:
       even.append(i)
   else:
       odd.append(i)
   print("Even numbers:",even)
   print("Odd numbers:",odd)


Given a python list[10, 501, 22,37,100,999,87,351] your task is to count all the prime numbers and create a new python list which will contain all the numbers in it 

def is_prime(n):
   if n <= 1:
       return False
   for i in range(2, int(n ** 0.5) + 1):
       if n % i == 0:
           return False
   return True




def find_primes_in_list(numbers):
   return [num for num in numbers if is_prime(num)]


numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = find_primes_in_list(numbers)
print(prime_numbers)



Given a Python List [10,501,22,37,100,999,87,351] Find out how many numbers are there in the given Python List which are Happy numbers?
def is_prime(n):
   if n < 2:
       return False
   for i in range(2, int(n ** 0.5) + 1):
       if n % i == 0:
           return False
   return True
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in numbers if is_prime(num)]
print("Prime Numbers:", prime_numbers)

Write a python program to find the sum of the first and last digit of an integer
n= int(input("Enter the four digit number:"))
sum= 0
a=n//1000
sum=sum+a
a=n%10
sum=sum+a
print("Sum of First and Last digit=",sum)

How can I use python to find all the ways to make Rs. 10 using Rs. 1, Rs. 2,Rs. 5, and Rs. 10 coins

def count_ways(coins, target):
   dp = [0] * (target + 1)
   dp[0] = 1
   for coin in coins:
       for amount in range(coin, target + 1):
           dp[amount] += dp[amount - coin]
   return dp[target]
coins = [1, 2, 5, 10]
target = 10
print("Total ways to make Rs. 10:", count_ways(coins, target))


You have been given three list. Your task is to find the duplicates in the three list write a python program for the same. You can use your own python lists 

a = [1, 2, 3, 4, 10]
b = [2, 3, 5, 6, 10]
c = [1, 2, 3, 7, 10]
res = set(a).intersection(b, c)
print(f"Common elements: {res}")


Write a python program to find the first non- repeating elements in a given list of integers

list = [4, 8, 2, 8, 9,78]
def nonrepeated(arr):
   return [i for i in arr if arr.count(i) < 2]
print(nonrepeated(list))




Write a python program to find the minimum element in a rated and sorted list

def findMin(arr):
   res = arr[0]


   for i in range(1, len(arr)):
       res = min(res, arr[i])
   return res


if __name__ == "__main__":
   arr = [5, 6, 1, 2, 3, 4]
   print(findMin(arr))



You have been given a python list [10,20,30,9] and a value of 59. Write a python program to find the triplet in the list whose sum is equal to the given value 

from itertools import combinations
def findtriplet(lst, key):
   def valid(val):
       return sum(val) == key
       return list(filter(valid, list(combinations(lst, 3))))


lst = [10,20,30,9]
print(findtriplet(lst,59))


Given a list [4,4,-3,1,6] write a python program to find if there is a sub list with sum equal to zero
def subArray(arr, l):
   for i in range(l - 1):
       s = arr[i]
       for j in range(i + 1, l):
           s += arr[j]
           if s == 0:
               return True
   return False
array = [4,4,-3,1,6]
print(subArray(array, len(array)))
 

			
		
