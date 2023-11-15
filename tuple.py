   # thistuple = ("banana", "cherry")
    #if "apple" in thistuple:
     # print("Yes, 'apple' is in the fruits tuple") 
    #else:
     #   print("no, 'apple' is not in the fruits tuple") 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
