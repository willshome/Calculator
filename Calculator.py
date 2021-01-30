import math #importing required module for operation

while True: #while loop for continuous looping of programme
  print("\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n") #menu

  oper = input("Your option from the menu: ")

  if oper == "0": #Addition
    num1 = float(input("First value: "))
    num2 = float(input("Second value: "))
    print("The result is:", num1 + num2)
  
  elif oper == "1": #Subtraction
    num1 = float(input("First value: "))
    num2 = float(input("Second value: "))
    print("The result is:", num1 - num2)
  
  elif oper == "2": #Multiplication
    num1 = float(input("First value: "))
    num2 = float(input("Second value: "))
    print("The result is:", num1 * num2)
  
  elif oper == "3": #Division
    num1 = float(input("First value: "))
    num2 = float(input("Second value: "))
    print("The result is:", num1 / num2)
  
  elif oper == "4": #Modulo
    num1 = float(input("First value: "))
    num2 = float(input("Second value: "))
    print("The result is:", num1 % num2)
  
  elif oper == "5": #To the power of
    num1 = float(input("First value: "))
    num2 = float(input("Second value: ")) 
    print("The result is:", math.pow(num1, num2))
  
  elif oper == "6": #Square root
    num1 = float(input("Value to square: "))
    print("The result is:", math.sqrt(num1))

  elif oper == "7": #Logarithm
    num1 = float(input("Value (to base 2): "))
    print("The result is:", math.log(num1, 2))

  elif oper == "8": #Sine
    num1 = float(input("Value (in degrees): "))
    print("The result is:", math.sin(math.radians(num1)))

  elif oper == "9": #Cosine
    num1 = float(input("Value (in degrees): "))
    print("The result is:", math.cos(math.radians(num1)))

  elif oper == "10": #Tangent
    num1 = float(input("Value (in degrees): "))
    print("The result is:", math.tan(math.radians(num1)))
  
  else: #Reminder of selection limits
    print("\nPlease select an option between 0 - 10")
    continue
  
  opt = input("\nWould you like another option: y/n ")
  if opt == "y":
    continue #Returns to menu
  elif opt == "n": #Ends loop
    break
  else: #Repeats question (once)
    opt = input("\nWould you like another option: y/n ")