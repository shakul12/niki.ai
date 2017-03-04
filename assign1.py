import math

def fib(n):
	f= 1/math.sqrt(5)*(((1+math.sqrt(5))/2)**(n))
	return round(f)

print(fib(12))
'''
this method is only for small numbers as it uses a recurrsive function.

def fib(n):
	if n==0:
		f =0
	if n==1:
		f =1
	if n>1:
		f = fib(n-1) +fib(n-2)
	return f
'''
num= list()
t= int(input("Enter the number of test cases: "))
for i in range(1,t+1):
	num.append(int(input("Enter %s number:" % i)))

'''
for every string of length n the number of desired strings with no 2 consecutive 0's can be calculated as-:

the no. of ways in which a string can start by 0 is equal to fib(n) - by using TREE's

the no. of ways in which a string can start by 1 is equal to fib(n+1)

so the total no. of strings =>  fib(n)+ fib(n+1) = fib(n+2) 
'''
for n in num:
	desired_value=0
	desired_value= fib(n+2)
	print(desired_value)
