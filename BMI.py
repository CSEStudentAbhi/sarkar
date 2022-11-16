
# asking for input from the users  
the_height = 162  
the_weight = 70  
# defining a function for BMI  
the_BMI = the_weight / (the_height/100)**2  
# printing the BMI  
print("Your Body Mass Index is", the_BMI)  
# using the if-elif-else conditions  
if the_BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif the_BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif the_BMI <= 29.9:  
    the_print("Eee! You are over weight.")  
else:  
    print("Seesh! You are obese.")  
