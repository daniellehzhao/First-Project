# First-Project
#1.Set the following variables to the appropriate values for today's date.
Day_of_Week = "Wednesday"
Month = "September"
Day_of_Month = "11"
Year = "2019"

#1a. Then write print functions that prints them in succession to indicate today's date"

print(Day_of_Week, Month, Day_of_Month, ",", Year)

#2.Call the print function one time to print the following strings.

print('''The newscaster said, "And Now for Something Completely Different!"\n''',
      '''One Quote:', Two Quotes", Red Quotes, Blue Quotes''')

#3. Execute these 2 lines 
print('5'+'4')

print(5+4)

#Different values print out because the first one is adding two strings together and not two numbers. Therefore it is simply concatenating the two numbers. However,
#the second one is actually adding two integers so you get a sum.

#4. Incorporate type conversion functions (str and int) into a statement
output = str(int('5')+int('4'))
print(output)

#5. Make new versions of each numeric expression incorporating parentheses

output = ((5*5)/5)-5
print(output)

output = 5-((5**5)*5)
print(output)

output = (60-(40*1.5))+((5**2)-25)
print(output)             

#6.Use integer division (//) and the modulus operator (%). Write a program for paying 543 cents using only quarters, nickels, and pennies.

quarters = (543//25)
nickels = (543%25)//5
pennies = (543%25)%5
print(quarters, 'quarters', nickels,'nickels', pennies, 'penny')

#7.Function 1:
def avg_of_3_num (a,b,c):
     average=((a+b+c)/3)
     return(average)

print(avg_of_3_num(10,12,14))

#8.Function 2:
def repeat_and_print(a, b):
    print(a)
    print(b)
    print(b*3)
   
repeat_and_print('You entered:', 'hello')

#9.Function 3: Write a function that calculates two averages (using Function 1) and returns the sum of the two averages
def avg_sum (num1,num2,num3,num4,num5,num6):
     print((avg_of_3_num(num1,num2,num3))+(avg_of_3_num(num4,num5,num6)))

avg_sum(2,4,6,8,10,12)

#10. Write a program to compute biorythms.
import math
def compute_biorhythm(t):
    physical = math.sin((2*(math.pi)*t)/23)
    emotional = math.sin((2*(math.pi)*t)/28)
    intellectual = math.sin((2*(math.pi)*t)/33)
    print("Your biorhythm today is:\n"
          "Physical:", physical, "Emotional:", emotional, "Intellectual:", intellectual)

compute_biorhythm(6782)

