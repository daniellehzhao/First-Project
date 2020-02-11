#1.Write a function that takes a number as a parameter argument. 
#  The program should contain a series of if (and possibly else) statements.
#  It should print different things depending on the number
def what_is_number(a):
    if (a%2 == 0):
        print('even')
    else:
            print('odd')
    if (a%3 == 0):
        print('divisible by three')
    if (a == 0):
        print('zero')
        return(True)
    
def question1():
    what_is_number(10)

#2.Write a function that takes a number as an argument and returns true if the number meets Condition 1 or Condition 2(or both):
#  Condition 1: The number is even and it is not divisible by 3
#  Condition 2: The number is odd and it is divisible by 3

def special_number(a):
    if (a%2 == 0 and a%3 != 0) or (a%2 != 0 and a%3 == 0):
        return(True)
def question2():
    print(special_number(15))

#3.Write a function that queries the user about the truth of a statement and then uses the
#  user's answers to distinguish between facts, falsehoods, alternative facts, and other categories of information.
def is_it_an_alternative_fact():
    input("What statement would you like to evaluate? ")
    print("Is this True, False, or Unknown to experts?")
    test1 = input("Choose True, False, or Unknown: ")
    print("Now, is it True, False, or Unknown to Trump?")
    test2 = input("Choose True, False, or Unknown: ")
    if (test1=='true' or test1=='True') and (test2=='true' or test2=='True'):
        print('True')
    if (test1=='false' or test1=='False') and (test2=='false' or test2=='False'):
        print('False')
    if (test1=='Unknown' or test1=='unknown') and (test2=='Unknown' or test2=='unknown'):
        print('Unknown')
    if (test1=='false' or test1 =='unknown' or test1=='False' or test1=='Unknown') and (test2=='true' or test2=='True'):
        print('Alternative Fact')
    if (test1=='true' or test1=='True' or test1=='Unknown' or test1=='unknown') and (test2=='false' or test2=='False'):
        print('Alternative Falsehood')
    if (test1=='true' or test1=='True' or test1=='false' or test1=='False') and (test2=='Unknown' or test2=='unknown'):
        print('Alternative Unknown')

def question3():
    print(is_it_an_alternative_fact())


#4 Write a Decision Tree Program

#sets up questions, answers, and factors that will go into the decision of what activity to do
problemintro="Your friends from back home are visiting and they've never been to the city! There's so many iconic things to do, something to fit every need! What do you and your friends want to do?"
factor1="Is it a) day or is it b)night? "
factor2="Are you trying to a) be indoors or b) outdoors?"
factor3="How much energy do you guys have? a)high energy or b)low energy"
factor4="Are you on a bit of a) a budget or b) more willing to spend?"
moreactivites="Would you like a) some night activities or b) is the day over?"

#sets up an a/b multiple choice structure
def choose_a_b(message):
    print(message)
    answer = 'X'
    while (answer != 'a') and (answer != 'A') \
      and (answer != 'b') and (answer != 'B'):
      answer = input('Choose: a, b: ')
      if (answer != 'a') and (answer != 'A') \
        and (answer != 'b') and (answer != 'B'):
        print('Only "a" or "b" are valid choices. Please try again.')
    if (answer == 'a') or (answer == 'A'):
        return('a')
    elif (answer == 'b') or (answer == 'B'):
        return('b')

#sets up what activities to do for night time, could be used to loop to after day activities
def nighttime():
    inorout=choose_a_b(factor2)
    if inorout=='a':
        budget=choose_a_b(factor2)
        if budget=='a':
            print("Play some games and enjoy some great food at Dave n Buster's. They often have deals going on!")
        if budget=='b':
            print("Get tickets to a Broadway show and enjoy the theatrics :)")
        print('Hope you guys had fun!')
    elif inorout=='b':
        strenuity=choose_a_b(factor4)
        if strenuity=='a':
            print("Go clubbing at a famous club or karaoke in K-town in the city that never sleeps!")
        elif strenuity=='b':
            print("Get a great from of the city at night from the top of the Empire State")

#main activities           
def chooseactivity():
    print(problemintro)
    timeofday=choose_a_b(factor1)
    if timeofday=='a':
        in_or_out=choose_a_b(factor2)
        if in_or_out=='a':
            price=choose_a_b(factor4)
            if price=='a':
                print("Hit up some museums! A lot of them have student discounts and aren't too expensive in general!")
            elif price=='b':
                print("There are a lot of great shopping areas such as Braodway, Fifth Ave, and Chelsea!")
        elif in_or_out=='b':
            energy=choose_a_b(factor3)
            if energy=='a':
                price=choose_a_b(factor4)
                if price=='a':
                    print("Walk along or around the Highline, Central Park, or even the Brooklyn Bridge! It's free!")
                elif price=='b':
                    print("Go rowboating in Central Park or spend a day in Coney Island and ride the Cyclone!")
            if energy=='b':
                price=choose_a_b(factor4)
                if price=='a':
                    print("Have your own little picnic in Central Park or Washington Square Park and listen to some great street music")
                if price=='b':
                    print('Go to the top of the 9/11 Memorial and get a great view of the city!')
        keepgoing=choose_a_b(moreactivites)
        if keepgoing=='a':
            print(nighttime())
        elif keepgoing=='b':
            print("Hope you and your friends had a great time!")
    elif timeofday=='b':
        print(nighttime())

def question4():
    chooseactivity()
        

  
