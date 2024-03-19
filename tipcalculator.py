print("WELCOME TO THUNGA'S TIP CALCULATOR!!")

bill = float(input("what is the total bill?"))

tip = int(input("How much tip would you like to give 10 12 15: "))

people = int(input("how many people will split the bill?: "))

x = float((bill + (tip/100)*bill)/people)

print(f"Each person should pay: {x}")
