# unit conversion using python

def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def main():
    print("Unit Converter")
    print("1. Inches to Centimeters\n2. Centimeters to Inches")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1":
        inches = float(input("Enter length in inches: "))
        print(f"{inches} inches is equal to {inches_to_cm(inches):.2f} cm")
    elif choice == "2":
        cm = float(input("Enter length in cm: "))
        print(f"{cm} cm is equal to {cm_to_inches(cm):.2f} inches")
    else:
        print("Invalid choice")

main()
        