# Function is used when we have to perform a task again and again. 

def calculateAverage(a, b):         # def is used to create a function.
    average = (a+b)/2
    print(average)

calculateAverage(30,23)     # function call.



def comparsion(a,b):
    if(a>b):
        print("First number is greater")
    elif(a<b):
        print("Second number is greater")
    else:
        print("Both the numbers are equal")

comparsion(40,34)       #function call.