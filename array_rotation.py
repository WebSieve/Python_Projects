import time

def userinput():
    a = []
    for i in range(lis_len):
        a.append(int(input(f"number {i+1}: ")))
    return a

def rotation():
    ltwo = []
    ltwo = lisone.copy()
    a = ltwo[0]
    ltwo.pop(0)
    ltwo.append(a)
    return ltwo

try:
    while True:
        lis_len = int(input("enter the length of the list (ctrl+c to exit): "))
        lisone = userinput()
        while True:
            c = rotation()
            lisone.clear()
            lisone = c.copy()
            print(c)
            time.sleep(0.1)
except KeyboardInterrupt:
    print("you broke the code!")
finally:
    print("bye bye black nigger")