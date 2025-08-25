a = input("Enter the main string: ")
b = input("Enter a string: ")

pos = []

for i in range(len(a) - len(b) + 1):
    flag = True
    for j in range(len(b)):
        if a[i + j] != b[j]:
            flag = False
            break
    if flag:  
        pos.append(i)

if pos:
    print("Pattern found", pos)
else:
    print("Not found")
