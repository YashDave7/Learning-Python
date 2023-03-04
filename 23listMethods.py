l = [11,34,45,65,23,45,67]
print(l)
# l.append(7)     # adds 7 to the last.
# l.sort()        # sorts the list.
# l.sort(reverse=True)    # sorts in reverse order.
# l.reverse()     # reverse the given string.
print(l.index(11))  # gives first index of 11.
print(l.count(45))  # gives the no of occurence.
m = l.copy()
m[0] = 0
print(m)
l.insert(1,69)
print(l)
k = l + m
print(k)
