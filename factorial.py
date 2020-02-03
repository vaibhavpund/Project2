
try:
    n=int(input("Enter the positive number to find factorial: "))
    fact=1


    def fact(n):
        fact1=1
        for i in range(1,n):
            fact1=fact1*n
            print(fact1)
            n=n-1

    fact(n)

except:
    print("Incorrect number entered")


