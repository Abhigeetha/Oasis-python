height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))
if height<=3 and weight<150:
    bmi=round(weight/height**2)
    if bmi<18.5:
        print("Your BMI is",bmi,". You are underweight.")
    elif bmi<25:
        print("Your BMI is",bmi,". You are normal.")
    elif bmi<30:
        print("Your BMI is",bmi,". You are overweight.")
    elif bmi<35:
        print("Your BMI is",bmi,". You are obese.")
    else:
        print("Your BMI is",bmi,". You are clinically obese.")
else:
    print("Enter valid input")
    
        
