# This function adds two numbers
def add(x,y):
  return x+y

# This function subtracts two numbers 
def sub(x,y):
  return(x-y)

# This function multiplies two numbers 
def multiply(x,y):
  return(x*y)

# This function divides two numbers
def  div(x,y):
  return(x/y)


print("-----Welcome To Mide Mini-Calculator!!-----\n")
print("----I can carry out +, -, *, / operations----\n")
print("----To use +, enter 1----\n")
print("----To use -, enter 2----\n")
print("----To use *, enter 3----\n")
print("----To use /, enter 4----\n")

operation = input("What operation would you like to do?: ")


print("Cool!! Please Continue below.")

userInputOne = input("Enter the first value: ")
print("\n")
userInputTwo = input("Enter the second value: ")

if (operation == 1):
  print("The answer is ", add(userInputOne, userInputTwo))
elif( operation == 2 ):
  print("The answer is ", sub(userInputOne, userInputTwo))
elif( operation == 3 ):
  print("The answer is ", multiply(userInputOne, userInputTwo))
elif ( operation == 4 ):
  print("The answer is ", div(userInputOne, userInputTwo))
else:
  print("You have entered an invalid operator/operation.")