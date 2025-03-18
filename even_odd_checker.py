def even_odd_ckecher(num):
    if num%2 == 0:
        print(f"the number {num} are even.")
    else:
        print(f"the number {num} are odd.")
user = int(input("enter a number: "))
result = even_odd_ckecher(user)
print(result)