even_numbers = []

for i in range(1, 101):
    if i % 2 == 0:
        even_numbers.append(i)

print("Even Numbers from 1 to 100:")
print(even_numbers)

print("\nMinimum Even Number:", min(even_numbers))
print("Maximum Even Number:", max(even_numbers))
print("Sum of Even Numbers:", sum(even_numbers))