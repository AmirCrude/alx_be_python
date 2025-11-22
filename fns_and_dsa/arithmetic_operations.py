
def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return add(num1, num2)
        case 'subtract':
            return subtract(num1, num2)
        case 'multiply':
            return multiply(num1, num2)
        case 'divide':
            if num2 == 0:
                return "Can not divide by 0."
            else:
                return divide(num1, num2)
        case _:
            print(f"Unknown operation: {operation}")

def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    if num2 != 0:
        result = num1 / num2
        return result 
    else:
        print("Can not divide by 0.")