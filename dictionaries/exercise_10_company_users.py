companies = dict()

while True:
    data = input().split("->")
    if len(data) == 1:
        break

    company_name = data[0]
    employee_id = data[1]
    if company_name not in companies:
        companies[company_name] = [employee_id]
    else:
        if employee_id not in companies[company_name]:
            companies[company_name].append(employee_id)

for key in companies:
    print(f"{key}")
    for employee_id in companies[key]:
        print(f"--{employee_id}")
