def calc(numA, numB, *operators):
    for o in operators:
        if o == "+":
            result1 = (numA + numB)
            print(numA, "+", numB,"=", result1)
        elif o == "-":
            result2 = (numA - numB)
            print(f"{numA} - {numB} = {result2}")
        elif o == "*":
            result3 = (numA * numB)
            print(numA, "*", numB,"=", result3)
        elif o == "/":
            result4 = (numA / numB)
            print(str(numA)+ " "+"/"+" "+ str(numB)+" "+"="+" "+ str(round(result4, 5)))
        elif o == "%":
            result5 = (numA % numB)
            print(f"{numA} % {numB} = {result5}")
        else:
            return "wrong input"
    #return any(result1, result2, result3, result4, result5)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter your operations: ")
opr =op.split(",")
opr = tuple(opr)
print(opr)
result = calc(num1, num2, *opr)


# simple Calculator By Paschal
def calc(a, b):
    if "+" in what:
        return a + b
    elif "-" in what:
        return a - b
    elif "*" in what:
        return a * b
    elif "/" in what:
        return a / b
    elif "%" in what:
        return a % b
    else:
        print("wrong input")
A = input("enter first number:")
B = input("enter second number: ")
a = int(A)
b = int(B)
func = input("enter an operation: ")
what = A + " "+ func +" "+ B
print(f"{a} {func} {b} equals {calc(a, b)}")
