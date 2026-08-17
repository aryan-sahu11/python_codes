print("Calculator")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter choice (1/2/3/4): ")
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        while True:
            a = int(input("Enter  number: "))
            c = 0
            num = input("Enter '=' to get the result or any integer to continue adding: ")
            if num == "=":
                a += a
                print("The sum is: ", a)
            else:
                c += af   
            print("The sum is: ", c)    
