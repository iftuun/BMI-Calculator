height=float(input("enter your height in m: "))
weight=float(input("enter your weight kg: "))

bmi=weight/((height)*(height))

if bmi<18.5:
    print("your BMI is: "+str(bmi)+"you are under weight.")
elif bmi>18.5 and bmi<25:
    print("your BMI is: "+str(bmi)+"you are have normal weight.")
elif bmi>25 and bmi<30:
    print("your BMI is: "+str(bmi)+" you are over weight.")
elif bmi>30 and bmi<35:
    print("your BMI is: "+str(bmi)+"you are OBESE.")
elif bmi>35:
    print("your BMI is: "+str(bmi)+"you are clinically obese.")
    
    