for i in range(1,10):
    for j in range(9-i,0,-1):
        print(0, end = '')
    for k in range(1,i+1):
        print(i, end = '')
    print()
