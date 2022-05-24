def sort_employees(employees, sort_by):
    # Write your code here.
    def myFunc(e):
        if sort_by == 'name':
            return e[0]
        elif sort_by == 'age':
            return e[1]
        elif sort_by == 'salary':
            return e[2]

    return sorted(employees, key=myFunc)
employees = [
            ["John", 33, 65000],
            ["Sarah", 24, 75000],
            ["Josie", 29, 100000],
            ["Jason", 26, 55000],
            ["Connor", 25, 110000],
        ]
sort_by = "age"
print(sort_employees(employees, sort_by))