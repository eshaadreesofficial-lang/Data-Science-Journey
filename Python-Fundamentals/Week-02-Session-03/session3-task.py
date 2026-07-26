
#Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

# ANSWER

rows = int(input('enter the rows'))

for i in range(0,rows):
  for j in range(rows-i,0,-1):
    print(j,end=' ')
  print()

# Problem 2: Print the following pattern.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

# ANSWER
rows = int(input('enter the rows'))

for i in range(1,rows+1):
  for j in range(0,i):
    print('*',end=' ')
  print()

for i in range(1,rows):
  for j in range(rows-i,0,-1):
    print('*',end=' ')
  print()

# Problem 3:Write a program to pring the following pattern

        *
       * *
      * * *
   * * * * * * *
* * * * * * * * *

#ANSWER 
rows = 6
for i in range(1,rows+1):
  print(' '*rows,end='')
  print('* '*i)
  rows = rows - 1

# Problem 4 :Write a program to print the following pattern

1

2 1

3 2 1

4 3 2 1

5 4 3 2 1

# ANSWER
rows = 5

for i in range(1,rows+1):
  for j in range(i,0,-1):
    print(j,end=' ')
  print()

# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term:<br>
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user

# ANSWER
x = 10
n = 5

sum = 1
s = ''
print('1 + ',end='')
for i in range(2,n+1):
  sum = sum + x**i/i
  s = s + 'x^{}/{} +'.format(i,i)
print(s[:-1])
print(sum)


Problem 6 - Find the sum of the series upto n terms.
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.
Example 1:
Input:
5
Output:
2+22+222+2222+22222
Sum of above series is: 24690

# ANSWER
n = int(input('enter the number of terms'))

start = 2
sum = 0

for i in range(0,n):
  if i < n-1:
    print(start,end='+')
  else:
    print(start)

  sum = sum + start
  start = start*10 + 2

print(sum)


#Problem 7: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers"""

# ANSWER
x = int(input('enter 1st number'))
y = int(input('enter 2nd number'))

if x>y:
  greater = x
else:
  greater = y

while True:
  if (greater % x == 0) and (greater % y == 0):
    lcm = greater
    break

  greater = greater + 1

print(lcm)
#OTHER METHOD
# ANSWER
x = int(input('enter 1st number'))
y = int(input('enter 2nd number'))

if x<y:
  smaller = x
else:
  smaller = y

for i in range(1,smaller+1):
  if (x % i == 0) and (y % i == 0):
    hcf = i

print(hcf)

