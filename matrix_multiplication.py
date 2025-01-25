import numpy as np

def userinput():
    print("enter the elements of matrix 1")
    a = []
    for i in range(3):
        n = []
        for j in range(3):
            n.append(int(input(f"input row {i+1} and column {j+1}:  ")))
        a.append(n)
    return a

def userinput2():
    print("enter the elements of matrix 2")
    a = []
    for i in range(3):
        n = []
        for j in range(3):
            n.append(int(input(f"input row {i+1} and column {j+1}:  ")))
        a.append(n)
    return a
              
try:
    while True:
        print("MATRIX MULTIPLIER".center(100, "."))
        mat_one = userinput()
        mat_two = userinput2()
        a = np.dot(mat_one, mat_two)
        print("matrix 1".center(40, "-"))
        for i in range(3):
            print(mat_one[i])
        print("matrix 2".center(40, "-"))
        for i in range(3):
            print(mat_two[i])
        print("RESULT".center(40, "-"))
        for i in range(3):
            print(a[i])
        print("-".center(40, "-"))
except KeyboardInterrupt:
    print("you broke the code")
finally:
    print("I wasn't able to do matrix multiplication on my own.")
    
