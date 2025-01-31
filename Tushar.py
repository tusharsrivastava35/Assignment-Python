n=int(input("Enter the number of alphabets: "))
for i in range (1,n+1):
    for j in range(n,i-1,-1):
        print(" ",end="")
    a=65
    for j in range(1,i+1):
        if(j%2!=0):
            print(chr(a),end=" ")
            a+=1
    for j in range(1,i):
        if(j%2!=0):
            print(chr(a),end=" ")
            a+=1
    print()
for i in range(1,n):
    for j in range(1,i+2):
        print(" ",end="")
    a=65
    for j in range(n-1,i-1,-1):
         if(j%2!=0):
            print(chr(a),end=" ")
            a+=1
    for j in range(n,i,-1):
        if(j%2!=0):
            print(chr(a),end=" ")
            a+=1
    print()