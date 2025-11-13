
size = int(input("Enter the size of the pattern: "))
count = 1

if size <= 0:
    print("Please enter a positive integer.")
else:
    while count <= size:
        for i in range(1, size + 1):
            print("*", end="")
        print()
        count += 1