# Full Pyramid Pattern

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Full Pyramid Alphabet Pattern

print("Full Pyramid:\n")

rows = 5

for i in range(rows, 0, -1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()