def calculator():
    while True:
        try:
            num1, num2 = [int(num1) for num1 in input("Enter Two Values: ").split()]
        except ValueError:
            print('Numbers must only contain digits.')
            break
        if len(str(num1)) > 4:
            print("Numbers cannot be more than four digits.")
            break
        elif len(str(num2)) > 4:
            print("Numbers cannot be more than four digits.")
            break
        operation = (input("Choose the operator that you want: [+] for addition or [-] for subtraction or press [0] to leave \n "))
        if operation == "0":
            print("Script closed!")
            break
        elif operation == "+":
            add = num1 + num2
            lenght = max(len(str(num1)), len(str(num2))) + 2
            dashline = ""
            for i in range(lenght):
                dashline += "-"
            print(f'''           {str(num1).rjust(lenght - 1)  }
          +{str(num2).rjust(lenght - 1)}
          {dashline}
          {str(add).rjust(lenght)}''')
            
        elif operation == "-":
            sub = num1 - num2
            lenght = max(len(str(num1)), len(str(num2))) + 2
            dashline = ""
            for i in range(lenght):
                dashline += "-"
            print(f'''           {str(num1).rjust(lenght - 1)}
          -{str(num2).rjust(lenght - 1)}
          {dashline}
          {str(sub).rjust(lenght)}''')
        elif operation == "/":
            print("The Division operation will not work!")
        elif operation == "x":
            print("The Multiplication operation will not work!")


calculator()