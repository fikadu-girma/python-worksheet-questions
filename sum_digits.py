def summation(num):
    sum = 0
    digit = 0
    while num > 0:
        digit = num%10
        sum = sum*10 + digit
        num = num%10
    return sum
user = int(input("enter the entiger: "))
result = summation(user)
print(f"the summation of the each digit of {user} are {result}.")
