# Strings are immutable.
s = "yash!!!! jjjnn 5567bjhb"
print(len(s))
print(s.upper())
print(s.lower())
print(s.strip("!"))
print(s.replace("yash","jash"))
print(s.split(" "))     # converts to list.
print(s.capitalize())       # make first letter capital.
print(s.center(50))         # 
print(s.count("yash"))      # returns the count of that string.
print(s.endswith("jhb"))    # returns true or false.
print(s.find("jjj"))        # returns the first occurence.
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isupper())
print(s.isnumeric())
print(s.isspace())
print(s.istitle())