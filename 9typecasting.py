# Typecasting : conversion of one datatype into another.
# following are the function for typecasting : int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc.

# Types of typecasting: 1. Explicit conversion.(done by developer)
#                       2. Implicit conversion.(done by python itself)

# Explicit Typecasting.
a = "1"
b = "2"
print(int(a) + int (b))

# Implicit Typecasting.
c = 1.9
d = 8       #here, d(int) will be converted into a float.
print(c + d)