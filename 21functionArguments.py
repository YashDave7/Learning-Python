def calculateAverage(a=5,b=3,c=2):      # Here, if the user doesnt pass any argument for any of the parameter then this default parameters will be passed.
    average = (a+b+c)/3
    print(average)

# Calling function.
calculateAverage()      # with default parameters.
calculateAverage(2,5)       # with some default and some user entered parameters.
calculateAverage(2,35,6)    # with all user entered parameters.

# Passing tuple as argument.
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum/len(numbers))

# calling function.
average(3,5,7,3)    # all this arguments goes in as tuple.

# passing dict as agrument.
def name(**name):
    print(type(name))
    print("hello", name["fname"], name["mname"], name["lname"])

# calling function.
name(mname="damodhardas", lname="modi", fname="narendra")