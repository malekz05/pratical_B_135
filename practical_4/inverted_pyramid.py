# Inverted Right Half Pyramid Pattern

rows = 6

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

rows = 5

for i in range(rows, 0, -1):
    ch = ord('A')
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
