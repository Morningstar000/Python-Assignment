Q1
# Input string
str = input()

# Declaring a dictionary
dict = {}

# Building dictionary with alphabets as keys
# and its count as its value
for i in str:
    dict[i] = dict.get(i, 0) + 1

# Sorting dictionary with
# values(count) in descending order(first priority)
# and keys(alphabets) in ascending order(second priority)
dict = sorted(dict.items(), key=lambda a: (-a[1], a[0]))

# Printing results
for j in dict:
    print(j[0], j[1])

    
    
    
Q2
# importing packages
import statistics
import pandas as pd

# Input series
sr = pd.Series([10, 50, 80, 70, 49, 23, 11, 4])

# calculating mean
mean = sr.mean()

# calculating standard deviation
sd = sr.std()

# printing results
print(min(sr), max(sr), '{:.2f}'.format(mean), '{:.2f}'.format(sd), '{:.2f}'.format(statistics.variance(sr)))





Q3
# Function return maximum area
def maxArea(A, L):
    area = 0
    for i in range(L):
        for j in range(i + 1, L):
            # Calculating the max area
            area = max(area, min(A[j], A[i]) * (j - i))
    return area


# Driver code
# Input height
a = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(maxArea(a, len(a)))






Q4
# importing required packages
from itertools import combinations

# First line of input containing space-separated integers.
values = [int(i) for i in input().split()]
values.sort()

# Second line of input containing K integer
K = int(input())

# Output will contain the count of
# all unique combinations of numbers whose sum is equal to K
counter = 0

for i in range(1, len(values) + 1):
    com = list(set(combinations(values, i)))
    for combination in com:
        if sum(combination) == K:
            counter += 1

print(counter)






Q5
1
try:
    a = 1/0
    print(a)
except ArithmeticError:
    print("Arithmetic exception.")
else:
    print ("Success.")

2
try:
    a = [1,2]
    print(a[2])
except LookupError:
    print("Index out of bound error")

3
class Attributes(object):
    pass
object = Attributes()
print(object.attribute)

4
import math
print(math.exp(1000))

5
array = [1, 2]
print(array[2])




Q7
from django.shortcuts import render  from.forms import ContactForm
from django.core.mail import send_mail

def contactview(request): name=''
email='' comment=''

form= ContactForm(request.POST or None)
if form.is_valid():
name= form.cleaned_data.get("name") 
email= form.cleaned_data.get("email") comment=form.cleaned_data.get("comment")


comment= name + " with the email, " + email + ", sent the following message:\n\n" + comment;
send_mail('The title of this post', comment, 'admin@gmail.com', ['admin@gmail.com'])


     context= {'form': form}
     return render(request, 'contact/contact.html', context) 
          else:
                       context= {'form': form}
                     return render(request, 'contact/contact.html', context) 
 







Q8
# Base class 1
class Base1():
    def show(self):
        print("Inside Base1 Class")


# Base class 2
class Base2():
    def display(self):
        print("Inside Base2 Class")


# Child class deriving from base class 1 and 2
class Child(Base1, Base2):
    def show(self):
        print("Inside Child Class")


# Example of overriding of show()
obj = Child()
obj.show()
obj.display()







Q8
class Point(object):
    pass


class Rectangle(object):
    pass


rectangle = Rectangle()
bottom_left = Point()
bottom_left.x = 5.0
bottom_left.y = 2.0
top_right = Point()
top_right.x = 7.0
top_right.y = 5.0
rectangle.corner1 = bottom_left
rectangle.corner2 = top_right
dx = 20.0
dy = 14.0


def move_rectangle(rectangle, dx, dy):
    print(f"The rectangle started with bottom left corner at({rectangle.corner1.x},{rectangle.corner1.y})"
f"\nTop right corner at ({rectangle.corner2.x},{rectangle.corner2.y})"
          f"\ndx is {dx} and dy is {dy}")
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print(f"It ended with a bottom left corner at ({rectangle.corner1.x},{rectangle.corner1.y})"
          f"\nTop right corner at ({rectangle.corner2.x},{rectangle.corner2.y})")


move_rectangle(rectangle, dx, dy)
