def case_calculator(str):
    upper = 0
    lower = 0
    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print(f"the number of uppercase is {upper}")
    print(f"the number of lowercase is {lower}")
user = input("enter the string: ")
result = case_calculator(user)
print(result)