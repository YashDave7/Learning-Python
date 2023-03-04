names = "Harry, Yash"
length = len(names)         # len(name_of_string) is the function to get the length of string.
print("the length of string is ", length)

slicing = names[0:5]        # name_of_variable[i, j] slicing function. 
print("slicing :-", slicing)

negativeSlicing = names[0:-2]       # negative slicing.negative number is interpreted as length - that number.
negativeSlicing1= names[0:len(names)-2]     # same as above line. 
print("negative slicing :-", negativeSlicing)