#get the numbers and operator from the user

num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
operator = input("Please enter the operator (+,-,*,/): ")

#definiton of the calculator function

def calculator(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error"
    else:
        return "You entered an invalid operator."
    return result

#definiton of result
result = calculator(num1, num2, operator)

#display the result    
print("Result: ", result)
