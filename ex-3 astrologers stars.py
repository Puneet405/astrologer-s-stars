boolean = int(input("Enter a number either 0 or 1 :  "))

if boolean != 0 and boolean != 1 :
    print("Please enter a no either 0 or 1")

elif boolean == False :
    print("Your boolean value is", False)
    NoOfRows = int(input("enter a number less than or equals to 10 : "))
    if NoOfRows <= 10 :
        for i in range(NoOfRows,0,-1):
            for j in range(i):
                print("*",end=" ")
            print("\r")
    else : print("enter a number less than 10")

elif boolean == True :
    print("Your boolean value is", True)
    NoOfRows = int(input("enter a number less than or equals to 10 : "))
    if NoOfRows <= 10 :
        for i in range(NoOfRows) :
            for j in range(i) :
                print("*", end=" ")
            print("\r")
    else:
        print("enter a number less than 10")