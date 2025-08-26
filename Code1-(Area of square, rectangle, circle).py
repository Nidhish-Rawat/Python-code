print("choose one of the below to find the area")
print ("1 Circle")
print("2 Square")
print("3 Rectangle")
a=input("Enter your choice : ")
if a=="Circle" or a=="circle":
    x=int(input("enter the radius of the circle : "))
    circle=3.14*x**2
    print(circle)
elif a=="square" or a=="Square":
    y=int(input("enter the length of the side : "))
    square=y**2
    print(square)
elif a=="rectangle" or a=="Rectangle":
    z=int(input("enter the length : "))
    v=int(input("enter the breadth : "))
    rectangle=z*v
    print(rectangle)
else:
    print("error occured, please try again")