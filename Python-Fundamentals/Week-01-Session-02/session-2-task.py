                                                 "#TASK 2
"# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
> Salary(Lakhs) : Tax(%)

*   Below 5 : 0%
*   5-10 : 10%
*   10-20 : 20%
*   aboove 20 : 30%

"# ANSWER
ctc = int(input('Enter your anual CTC:'))

if ctc < 5000000:
    salary=ctc*.82
elif ctc<1000000:
    salary=ctc*.72
elif ctc<2000000:
    salary=ctc*.62
else:
    salary=ctc*.52

print("You in hand monthly salary will be-", round(salary/12,2))

"# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
Hint - Sum of all angles is 180 and all angles are positive

"# ANSWER
first = int(input('enter the 1st angle'))
second = int(input('enter the 2nd angle'))
third = int(input('enter the 3rd angle'))

if (first+second+third) == 180 and first>0 and second>0 and third>0:
  print('forms a triangle')
else:
  print('does not form a triangle')

"# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit."""
"# ANSWER
cost_price = int(input('Enter cost price-'))
selling_price = int(input('Enter selling price-'))

if cost_price < selling_price:
    print('Profit')
elif cost_price > selling_price:
    print('Loss')
else:
    print('No Loss No Gain')

"# Problem 4: Write a menu-driven program 
1. cm to ft
2. km to miles
3. USD to INR
4. exit

Hint
- 1 cm = 0.032ft
- 1km = 0.62
- 1 USD = 80 INR

"# ANSWER
menu = input("""Hi select an option
1. cms to ft
2. km to miles
3. USD to INR
4. Exit    """)

if menu == '1':
  cm = float(input('enter the cm value'))
  print('ft value is',0.032*cm)
elif menu == '2':
  km = float(input('enter the km value'))
  print('miles value is',km*0.62)
elif menu == '3':
  usd = float(input('enter usd'))
  print('inr',usd*80)
else:
  exit()

"# Problem 5: Exercise 12: Display Fibonacci series up to 10 terms.
*Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34

"#ANSWER

num1,num2 = 0,1
for i in range(10):
  print(num1)

  next = num1 + num2
  num1 = num2
  num2 = next

"#Problem 6: Find the factorial of a given number.
"#Write a program to use the loop to find the factorial of a given number.
#CONCEPT
The factorial (symbol: `!`) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5
5! = 5 × 4 × 3 × 2 × 1 = 120
Output:
120

"# ANSWER
num = int(input('enter the number'))

fact = 1
for i in range(1,num+1):
  fact = fact*i

print(fact)

"# Problem 7: Reverse a given integer number.
Example:
Input:
76542
Output:
24567

"# ANSWER
number = int(input('enter the number'))
rev = 0

while number>0:
  last = number%10
  rev = rev*10 + last
  number = number//10

print(rev)

"Problem 8: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
Example 1
Input
30
Output
276

"#ANSWER
N = int(input('enter the number'))
sum = 0
i = 1

while i < N+1:
  if i % 5 == 0:
    i+=1
    continue

  sum += i

  if sum > 300:
    sum = sum - i
    break

  i+=1

print(sum)

"# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers."""

"# ANSWER
sum = 0
count = 0

while True:
  num = int(input('enter number'))
  if num == 0:
    break
  sum = sum + num
  count = count + 1

print('sum',sum)
print('avg',sum/count)

"# Problem 9: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line."""

"# ANSWER
L = []
for i in range(2000,3201):
  if i % 7 == 0 and i % 5 != 0:
    L.append(str(i))

print(",".join(L))

"# Problem 10: Write a program  which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.

"# ANSWER 
L = []
for i in range(1000,3001):
  flag = True

  curr = i

  while curr > 0:
    last = curr%10
    if last % 2 != 0:
      flag = False
      break
    curr = curr//10

  if flag == True:
    L.append(str(i))

print(",".join(L))


"# Problem 11:Write a program to print whether a given number is a prime number or not"

"#ANSWER
num = int(input('enter the num'))

flag = True
for i in range(2,num):
  if num%i == 0:
    flag = False
    break

if flag == True:
  print('Prime')
else:
  print('Not Prime')


