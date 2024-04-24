numbers = []

for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        numbers.append(str(num))

# Join the list into a comma-separated string and print it
result = ", ".join(numbers)
print(result)
