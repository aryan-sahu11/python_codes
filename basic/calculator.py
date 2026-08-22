print("Calculator")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        sum = 0
        while True:
            num = input("enter your number : ")
            if num == "=":
                break
            sum = sum + int(num)
        print(sum)
        
    if choice =='2':
        sub = 0
        while True:
            num = input("enter your number:")
            if num=="=":
                break
            sub = int(num)-sub

        print(sub)

    if choice =='3':
        mup =0
        while True:
            num = input("enter your number:")
            if num=="=":
                break


    if choice =='4':
        div=0
        while True:
            num = input("enter your number:")
            if num=="=":
                break
    
            



        