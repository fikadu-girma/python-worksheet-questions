def binary(num):
    if num == 0:
        return "0"
    binarys = ""
    while num > 0:
        binarys = str(num%2) + binarys
        num = num // 2
    return binarys
user = int(input("enter a number: "))
result = binary(user)
print(result)
