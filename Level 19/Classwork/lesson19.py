def bmi(weight, height):
    bmi_mass = weight / (height ** 2)
    if bmi_mass <= 18.5:
        return "Underweight"
    elif bmi_mass <= 25.0:                  
        return "Normal"
    elif bmi_mass <= 30.0:
        return "Overweight"
    else:
        return "Obese"