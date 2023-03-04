# VARIABLES are like containers which can hold data.
a = 69
b = "Yash"
c = True
d = None
e = (2,-4j)

# DATATYPES are the type of value you are storing in a variable.
# We can use type() function to get the datatype of variable. 
print("The datatype of a is ",type(a))
print("The datatype of b is ",type(b))
print("The datatype of c is ",type(c))
print("The datatype of d is ",type(d))
print("The datatype of e is ",type(e))

# TYPES OF DATATYPE.
# 1. Numderic data: int , float, complex.
# 2. Text data: str.
# 3. Boolean data.
# 4. Sequenced data: list, tuple.
#    list: A list of different datatypes.
#    Lists are mutable(can be changed afterwards). 
list1 = [1,34,56,[344,656,0],["yash","jash"]]
print(list1)
#    Tuples: Almost same as list. But are inmutable(can not be changed afterwards).
tuple1 = ("Yash","Jash",68,69)
print(tuple1)

# Mapped data: dict.
#    dict: An unordered collection of data containing a key, value, pair.
dict1 = {"name":"Yash", "age":19, "canVote":True}
print(dict1)