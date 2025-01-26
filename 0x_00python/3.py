# 3. Write a program to print 1 to 10 numbers using for loop.
for x in range(1,11):
    print(x)
print("******************************************************************")
for z in range(1,11):
    print(z)
    if z==5:
        break
print("******************************************************************")
for y in range(1,11):
    if y==5:
        continue
    print(y)
print("******************************************************************")
for i in range(1,11):
    if i==5:
        pass
    print(i)
print("******************************************************************")
for j in range(1,11):
    if j==5:
        print(j)
    else:
        print("not 5")
print("******************************************************************")
        