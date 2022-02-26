import math;

while (True):
    #menu
    print("Choose an option\n")
    print("0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division")
    print("4 - Modulo\n5 - Raise to a Power\n6 - Square Root\n7 - Logarithm")
    print("8 - Sine\n9 - Cosine\n10 - Tangent\n")

    op = input("\nOption: ")
    
    #addition
    if op == "0":
        n1 = float(input("\nFirst value: "))
        n2 = float(input("\nSecond value: "))

        print("Result is ", (str(n1 - n2)), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break
    
    #subtraction
    elif op == "1":
        n1 = float(input("\nFirst value: "))
        n2 = float(input("\nSecond value: "))

        print("Result is ", (str(n1 - n2)), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break
       
    #multiplication
    elif op == "2":
        n1 = float(input("\nFirst value: "))
        n2 = float(input("\nSecond value: "))

        print("Result is ", (str(n1 * n2)), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #division
    elif op == "3":
        n1 = float(input("\nFirst value: "))
        n2 = float(input("\nSecond value: "))

        print("Result is ", (str(n1 / n2)), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #modulo
    elif op == "4":
        n1 = float(input("\nFirst value: "))
        n2 = float(input("\nSecond value: "))

        print("Result is ", (str(n1 * n2)), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #power
    elif op == "5":
        n1 = float(input("\nFirst value: "))
        n2 = float(input("\nSecond value: "))

        print("Result is ", (str(math.pow(n1,n2))), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #sqrt
    elif op == "6":
        n1 = float(input("\nFirst value: "))

        print("Result is ", (str(math.sqrt(n1))), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #logarithm
    elif op == "7":
        n1 = float(input("\nFirst value (base 2): "))

        print("Result is ", (str(math.log(n1, 2))), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #sin
    elif op == "8":
        n1 = float(input("\nFirst value: "))

        print("Result is ", (str(math.sin(math.radians(n1)))), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #cos
    elif op == "9":
        n1 = float(input("\nFirst value: "))

        print("Result is ", (str(math.cos(math.radians(n1)))), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    #tan
    elif op == "10":
        n1 = float(input("\nFirst value: "))

        print("Result is ", (str(math.tan(math.radians(n1)))), "\n")

        keepGoing = input("\nReturn to menu? (y/n) ")

        if keepGoing == 'y':
            continue
        else:
            break

    else:
        print("\nInvalid Option")
        continue