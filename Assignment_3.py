def check_right_triangle(a, b, c):
    if a*a + b*b == c*c:
        print("Right-angled triangle")
    elif a*a + c*c == b*b:
        print("Right-angled triangle")
    elif b*b + c*c == a*a:
        print("Right-angled triangle")
    else:
        print("Not a right-angled triangle")


a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

check_right_triangle(a, b, c)
