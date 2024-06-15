def main():
    print("Calculate your Body Mass Index (BMI)")
#This will input the patients Name
    name = input("Please Enter your Name : ")
    height = float(input("Enter your height in Centimeters: "))
    weight = float(input("Enter your weight in Kilograms: "))
#The height converts from centimeter to meter
    height = height / 100
#This will calculate BMI
    bmi = weight / (height * height)
    print("Your Body Mass Index is: ", bmi)
    if (bmi <= 16):
        print("You are severely underweight")
    elif (bmi <= 18.5):
        print("You are underweight")
    elif (bmi <= 25):
        print("Great work! You are healthy")
    elif (bmi <= 30):
        print("You are overweight")
    else:
        print("You are severely overweight")

if __name__ == "__main__":
    main()
