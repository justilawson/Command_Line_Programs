height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

weight = weight*703
height = int(height * height)
bmi = int(weight/height)

if bmi <= 18.5:
  print(f"You BMI is {bmi}, you are underweight")
elif bmi <= 25:
  print(f"You BMI is {bmi}, you are normal weight")
elif bmi <= 30:
  print(f"You BMI is {bmi}, you are slightly overweight")
elif bmi <= 35:
  print(f"You BMI is {bmi}, you are obese")
else:
  print(f"You BMI is {bmi}, you are clinically obese")
