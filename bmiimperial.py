import math

data = input()
w = float(data)
w = w * 0.453592

data = input()
h = float(data) * 0.0254

bmi = w / (h * h)
print("BMI is: ", bmi, sep="")

