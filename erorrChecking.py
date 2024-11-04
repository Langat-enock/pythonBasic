# Error handling
x = input("Enter_first number")
y = input("Enter_second number")
z = input("Enter_third number")

try:

    x_num = int(x)
    y_num = int(y)
    z_num = int(z)

    print(x_num + y_num + z_num)
except:
    print("Enter the valid number")

