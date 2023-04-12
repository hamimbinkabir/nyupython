w = float(input("Please enter weight in kilograms:"))

h = float(input("Please enter height in meters:"))
BMI = round(w / (h**2),2)

if 0 < BMI <= 18.5:
    print("BMI is: ", BMI, ", Status is Underweight", sep="")
elif 18.51 <= BMI <= 25:
    print("BMI is: ", BMI, ", Status is Normal", sep="")
elif 25 < BMI <= 29.99:
    print("BMI is: ", BMI, ", Status is Overweight", sep="")
elif BMI >= 30:
    print("BMI is: ", BMI, ", Status is Obese", sep="")