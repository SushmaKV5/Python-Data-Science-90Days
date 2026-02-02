#Number patterns using nested loops

n = 5

print("Repeated Number Pattern")
for i in range(1, n+1):
    for j in range(i):
        print(i,end=" ")
    print()

print("\nIncresing Number Pattern")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()