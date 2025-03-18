def product_sum(x,y):
    a = x*y
    b = x+y
    if a > 500:
        print(f"the summation of {x} and {y} are {b}")
    else:
        print(f"the product of {x} and {y} are {a}")
user1 = int(input("enter the 1st number: "))
user2 = int(input("enter the 2nd number: "))
result = product_sum(user1, user2)
print(result)
