# Conditional statements in pyhton

# 1)Basic syntax

num=10

if num>18:
  print("Number is greater than 18")
else:
  print("Number is less than 18")


# 2)elif syntax
num=10

if num==0:
  print("Num is zero")
elif num>0:
  print("Num is positive")
else:
  print("Num is negative")



# 3)Nested else - if

num=5
if num==0:
  print("Num is zero")
elif num>0:
  print("Num is positive")
  if num>10:
    print("Num is greater than 10")
  elif num<10:
    print("Num is less than 10")
  else:
    print("Num is 10")
else:
  print("Num is negative")
  if (num>-10):
    print("Num is greater than -10")
  else:
    print("Num is lesser than -10")



# 4)Short-hand for else-if
# result = value_if_true if condition else value_if_false


num=num*num if num<10  else num-10

print("New num is",num)

# 5) match

num=5

match num:
  case 1:
    print("Num is 1")
  case 2:
    print("Num is 2")
  case 4:
    print("Num is 4")
  case 5:
    print("Num is 5")
  case _:
    print("Some other number is there")
