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
