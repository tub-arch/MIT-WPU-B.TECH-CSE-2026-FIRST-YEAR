pan = input("Enter PAN number: ")

if len(pan) == 10:
    if (pan[:5].isalpha() and pan[:5].isupper() and
        pan[5:9].isdigit() and
        pan[9].isalpha() and pan[9].isupper()):
        
        print("Valid PAN Number")
    else:
        print("Invalid PAN Number")
else:
    print("Invalid PAN Number")
