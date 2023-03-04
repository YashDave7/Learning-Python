# Almost same as array, can store any type of data.(represented in [])
marks = [2,5,3,"yash",False,23]
print(marks)
print(type(marks))
print(marks[0])     # index.
print(marks[1])
print(marks[2])

print(marks[-3])    # negative indexing.
print(marks[len(marks)-3]) # Positive index
print(marks[5-3]) # Positive index
print(marks[2]) # Positive index

if "6" in marks:
    print("Yes")
else:
    print("No")

print(marks[0:7])   # including first and not including second.
print(marks[1:9])
print(marks[1:9:3]) # from first to second by jumping every third number of digit.

lst = [i*i for i in range(10)]
print(lst)