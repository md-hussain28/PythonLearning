# 1)Primary types of loop in python

# a)for loop

'''
   Iterate over a sequence (like list, tuple, dictionary, string) or any iterable object.
   Syntax : for variable in iterable:
                # code block
   

'''

#Simple syntax
for i in range(10):
    print(i)

#for loops on iterable
temp=["banana",32,23.0,"s","apple",123]

for i in temp:
    print(i)

# b)while loop
'''
   Repeat code as long as a condition is True.
   Syntax : while condition:
               # code block

'''

temp=0

while (temp<10):
    temp+=1
    print(temp)


#2)Loop Control Statements

# a)break statement
'''
  Immediately exits the nearest enclosing loop.
'''
temp=0
while temp<10:
    if(temp==5): break
    temp+=1
    print("Temp-->",temp)
    
# b) continue statement
'''
  Skips the rest of the current loop iteration and moves to the next.
'''

temp=0
while (temp<10):
   
    temp+=1
    if(temp==5):continue
    print("Temp",temp)



#3)Enumertate

seasons=["Summer","Winter","Autumn","Rain"]

for id,season in enumerate(seasons):
    print(f"{season} has id {id}")



#4)Zip 

temperature =["Hot","cold","balanced","Nice"]

for a,b in zip(seasons,temperature):
    print(f"{a} is {b}")

print("Completed--------------------//")