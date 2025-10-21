# Print command
print("This is python print")

print("First Print","Second Print")

print("First","Second","Third",sep=",",end="") #Changed behaviour using the optional parameter
print("Fourth")

print("this is first line\nthis is next line")



# This is a single line comment
"""
   This is a multi line comment
   print("doesn't work here")
"""


# Aritheamatic Operators
a=10; b=3
c=5
fa=23.4; fb=5.6

print("Addition",a+b)
print("Substraction",a-b)
print("Divisions",a/b)
print("Floor division",a//b) 
print("Floor Division on float",fa//fb) #Works on float too
print("Modulo",a%b)
print("Modulo on negative",-5%3)
print("Multiplication",a*b)
print("Power",a**b)
print("Follows bodmas",1+3*4)



# Logical operators
# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False



# Booleans
# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0)      # => False
bool("")     # => False
bool([])     # => False
bool({})     # => False
bool(())     # => False
bool(set())  # => False
bool(4)      # => True
bool(-6)     # => True