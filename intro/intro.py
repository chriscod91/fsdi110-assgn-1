#single line comm ent
#indentation is imortant
#variables
name = "Chris"
last_name = "Codina"
age = 21 #integer
price = 29.99#float

print(name)

print(name + name)#str concatenation
print(age + price)#math/sum 

print(name + str(age))
  


def say_hello(): 
        print("hello there")
        print("im a function")

print("im outside the function")
say_hello() # call a function

#snake_case is naming convention for python
#if statement no parenthesis is needed
if(age<100): 
        print("you are young!!")

elif age==100:
        print("you are exactly 100") 

else:
        print("youre getting old")
