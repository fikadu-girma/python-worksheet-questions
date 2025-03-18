weight = int(input("Enter ur body weight(in pounds): "))
height = float(input("Enter ur height(by inch): "))

BMI = (weight*720) / (height**2)
print("ur BMI are:", BMI)
if 19 <= BMI <= 25:
    print("u're healthy person")
elif BMI > 25:
    print("u're over weighted")
else:
    print("u're under weighted")
