print(" *** BMI ***")
weight,heigh = input("Enter your weight(kg) and height(m) : ").split()

weight = float(weight)
heigh = float(heigh)

bmi = weight/(heigh*heigh)

if bmi < 18.5:
    status = "Below normal weight."
elif bmi < 25:
    status = "Normal weight."
elif bmi <30 :
    status = "Overweight."
elif bmi < 35:
    status  = "Case I Obesity."
elif bmi < 40:
    status = "Case II Obesity."
elif bmi >= 40:
    status = "Case III Obesity."

print("Your status is : "+status)









