# determine variables
try:
    height = float(input("Input your height in meters: "))
    weight = float(input("Input your weight: "))
    # provide computations of BMI
    if weight <= 0 or height <= 0:
        print('Error: weight and height must be positive')
    else:
        BMI = weight / (height ** 2)
        print(f'Your BMI is: {BMI:.2f} kg/m^2')
        if BMI < 18.5:
            print('Underweight')
        elif 18.5 <= BMI < 25:
            print('Normal weight')
        elif 25 <= BMI < 30:
            print('Overweight')
        elif BMI >= 30:
            print('Obesity')
except ValueError:
    print('Error: input must be a number')
except Exception as e:
    print(f'Unexpected error: {e}')