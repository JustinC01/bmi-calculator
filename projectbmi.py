feet = int(input("Enter your height in feet: "))
inches = int(input("Enter your height in inches: "))

weight = int(input("Enter your weight in kilograms: "))

height=(feet*0.3048)+(inches*0.0254)
bmi = weight/height**2

if bmi < 18.5:
    print("you are underweight, you should consider eating more")

elif 18.5 <= bmi <= 24.9:
    print("you are healthy keep up the good work")

elif 25 <= bmi <= 29.9:
    print("you are over weight you should go to the gym and consider changing your diet you can shead a good 30 pounds")

elif 30 <= bmi <= 40:
    print("you suffer from obesity you should shead 50 pounds and change your diet")
else:  
       print("Your BMI is in the severe obesity range. Please seek medical advice.")
