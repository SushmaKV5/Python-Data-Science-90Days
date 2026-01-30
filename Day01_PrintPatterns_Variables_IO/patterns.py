#Star pattern - Right triangle

n = 5

print("Right triangle pattern")
for i in range(1, n+1):
    print("*"*i)

print("\nInverted triangle pattern")
for i in range(n, 0, -1):
    print("*"*i)

print("\nPyramid pattern")
for i in range(1, n+1):
    print(" "*(n-i) + "* "*i)


#Numeric pattern

print("\nNumeric pattern:")
for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()