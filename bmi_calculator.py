#BMI Calculator using python

def calculate_bmi(weight, height):
    return weight / height **2

def bmi_category(bmi):
    if bmi < 18.5:
        return "Under Weight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Over Weight"
    else:
        return "Obese"

print("Welcome to BMI Calculator\n")
weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print(f"\nYour BMI is: {bmi:.2f}")
print(f"You're classified as: {bmi_category(bmi)}\n")