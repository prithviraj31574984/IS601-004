x = [5,4,3,2,1]
a = 0
for i in x:
    print("i =  " + str(i))
    a += 1
    if i % 2 ==0:
        a -= 1
    print("a is " + str(a))

