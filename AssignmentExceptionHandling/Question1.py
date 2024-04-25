def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    else:
        return result


result = divide_by_zero()

print(result)
