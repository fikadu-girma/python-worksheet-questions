commissioned_salaried_employee = {
    "seid": [10000, 0.05,5000],
    "chala" : [2000,0.05,5000],
    "Abenezer" : [4000,0.05,5000],
    "Abel" : [20000,0.05,5000],
    "Kebede" : [8000,0.05,5000],
    "Mohammed" : [5000,0.05,5000]
}

for key, value in commissioned_salaried_employee.items():
    fixed_salary = value[2]
    sell = value[0]
    percent = value[1]
    salary = fixed_salary+(sell*percent)
    value.append(salary)
print(value)


print("Name \t\t Total_Salary")
for key, value in commissioned_salaried_employee.items():
    print(key, "\t\t", value[3])

for key, value in commissioned_salaried_employee.items():
    rank = value[3]
    if i in range(7):
        if rank < value[i]:
            rank = value[i]
        print(rank)
    print()