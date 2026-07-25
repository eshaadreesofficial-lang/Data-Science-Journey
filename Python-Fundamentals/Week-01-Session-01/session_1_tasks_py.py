
#Q1 Pint the given strings as per stated format.
#Given strings:
"Data" "Science" "Mentorship" "Program"
"By" "CampusX"r
Output:
Data-Science-Mentorship-Program-started-By-CampusX
Concept- [Seperator and End]

#SOLUTION
#CODE
print("Data","Science","Mentorship","Program",sep='-',end='-started-')
print("By","CampusX",sep='-')

# Q2  Write a program that will convert celsius value to fahrenheit.

# CODE
celcius = float(input('enter the temp in celcius'))
faren = celcius * (9/5) + 32
print(faren,'F')

# Q3 Take 2 numbers as input from the user.Write a program to swap the numbers without using any special python syntax.

#CODE
a = 3
b = 5

temp = a
a = b
b = temp

print(a)
print(b)

# Q4 Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

#CODE
p1x = int(input('enter x coord of 1st point'))
p1y = int(input('enter y coord of 1st point'))
p2x = int(input('enter x coord of 2nd point'))
p2y = int(input('enter y coord of 2nd point'))

#distance = ((p2x - p1x)**2 + (p2y - p1y)**2)**0.5
distance=((p2x-p1x)**2+(p2y-p1y)**2)**0.5
print(round(distance,2))

# Q5 Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.
Hint - si = (p * t * r)/100

#CODE
p = int(input('Enter amount'))
t = int(input('Enter time period'))
r = float(input('Enter rate'))

interest = (p*t*r)/100

print('the interest is',interest)

# Q6 Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

For example:
Input:
heads -> 4
legs -> 12
<br>
Output:
dogs -> 2
chicken -> 2

#CODE
heads=int(input("enter heads "))
legs=int(input("enter legs "))

dogs=(legs - 2 * heads)//2
chicken= heads - dogs

print(f"dogs {dogs} , chicken {chicken}")        # 'f' activates formatting.(f btata hai ky jo bi {} ma likha hai usay string considerd nhi krna uski value lyni hai)
                                                 # '{}' prints the variable's value instead of its text.
#print("dogs" ,dogs,"chicken",chicken)

# Q7  Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.
Hint - Thus, the sum of the squares of first n natural numbers =  n(n+1)(2n+1)/6

#CODE
n = int(input('enter the number'))
result = (n*(n+1)*(2*n + 1))/6
print(result)

# Q8  Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.
Hint - an = a + (n – 1)d
 #CODE

first_term = int(input('enter 1st term'))
second_term = int(input('enter 2nd term'))
n = int(input('enter the value of n'))

d = second_term - first_term

an = first_term + (n-1)*d
print(an)

"""### Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user."""

# Write your code here
n1 = int(input('num1'))
d1 = int(input('den1'))
n2 = int(input('num2'))
d2 = int(input('den2'))

rn = n1*d2 + n2*d1
rd = d1*d2

print('{}/{}'.format(rn,rd))

# Q10 Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.
Input:
Dimensions of the milk tank<br>
H = 20cm, L = 20cm, B = 20cm
Dimensions of the glass<br>
h = 3cm, r = 1cm


#CODE
import math

h_t = float(input('height'))
b_t = float(input('breadth'))
l_t = float(input('length'))

h_g = float(input('height of glass'))
r_g = float(input('radius of the glass'))

vol_tank = h_t*b_t*l_t
vol_glass = 3.14*r_g*r_g*h_g

print('no of glasses',math.floor(vol_tank/vol_glass))

math.floor(6.7)           #point value convert into integer

