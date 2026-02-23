# Odd numbers between 1 and 100

odd_numbers = []

for num in range(1, 101):
    if num % 2 != 0:
        odd_numbers.append(num)

print("Odd numbers between 1 and 100:")
print(odd_numbers)

# Minimum odd number
min_odd = min(odd_numbers)

# Maximum odd number
max_odd = max(odd_numbers)

# Sum of odd numbers
sum_odd = sum(odd_numbers)

print("\nMinimum odd number:", min_odd)
print("Maximum odd number:", max_odd)
print("Sum of odd numbers:", sum_odd)

# Odd Numbers Operations

print("Odd Numbers Operations:\n")

# List of odd numbers between 1 to 50
odd_numbers = [num for num in range(1, 51) if num % 2 != 0]

print("List of Odd Numbers (1-50):")
print(odd_numbers)

# Three minimum odd numbers
print("\nThree Minimum Odd Numbers:")
print(odd_numbers[:3])

# Three maximum odd numbers
print("\nThree Maximum Odd Numbers:")
print(odd_numbers[-3:])

# Average of odd numbers
average = sum(odd_numbers) / len(odd_numbers)
print("\nAverage of Odd Numbers:")
print(average)