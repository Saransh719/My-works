#19-05-203
#R14
'''WAP to create a binary file 'employ.dat' where the data is stored as list-:[Empid,name,salary,department,desgination]
Write a menu driven program to perform the following operations-
1. Add a Record
2. Delete a Record whose Employee ID is given
3. Update the Record of a given Employee
4. Display the Record Department-wise when given Name and ID
5. Display the Record of a particular Employee using ID
6. Department wise highest and lowest salary'''
import pickle

def add_record():
    with open('employ.dat', 'ab') as f:
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = input("Enter employee salary: ")
        department = input("Enter employee department: ")
        designation = input("Enter employee designation: ")
        record = {'Employee_ID': emp_id, 'Name': name, 'Salary': salary, 'Department': department, 'Designation': designation}
        pickle.dump(record, f)
        print("Record added successfully.")

def delete_record():
    emp_id = input("Enter employee ID to delete record: ")
    with open('employ.dat', 'rb') as f:
        records = []
        while True:
            try:
                record = pickle.load(f)
                if record['Employee_ID'] != emp_id:
                    records.append(record)
            except EOFError:
                break
    with open('employ.dat', 'wb') as f:
        for record in records:
            pickle.dump(record, f)
    print(f"Record with Employee ID {emp_id} deleted successfully.")

def update_record():
    emp_id = input("Enter employee ID to update record: ")
    with open('employ.dat', 'rb') as f:
        records = []
        while True:
            try:
                record = pickle.load(f)
                if record['Employee_ID'] == emp_id:
                    name = input("Enter updated employee name: ")
                    salary = input("Enter updated employee salary: ")
                    department = input("Enter updated employee department: ")
                    designation = input("Enter updated employee designation: ")
                    record['Name'] = name
                    record['Salary'] = salary
                    record['Department'] = department
                    record['Designation'] = designation
                records.append(record)
            except EOFError:
                break
    with open('employ.dat', 'wb') as f:
        for record in records:
            pickle.dump(record, f)
    print(f"Record with Employee ID {emp_id} updated successfully.")

def display_record_department_wise():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    with open('employ.dat', 'rb') as f:
        while True:
            try:
                record = pickle.load(f)
                if record['Name'] == name and record['Employee_ID'] == emp_id:
                    print(f"Employee ID: {record['Employee_ID']}, Name: {record['Name']}, Department: {record['Department']}")
            except EOFError:
                break

def display_record_by_employee_id():
    emp_id = input("Enter employee ID to display record: ")
    with open('employ.dat', 'rb') as f:
        while True:
            try:
                record = pickle.load(f)
                if record['Employee_ID'] == emp_id:
                    print(f"Name: {record['Name']}, Salary: {record['Salary']}, Department: {record['Department']}, Designation: {record['Designation']}")
            except EOFError:
                break

def display_department_wise_highest_and_lowest_salary():
    departments_salary_dict = {}
    with open('employ.dat', 'rb') as f:
        while True:
            try:
                record = pickle.load(f)
                if record['Department'] not in departments_salary_dict.keys():
                    departments_salary_dict[record['Department']] = [float(record['Salary'])]
                else:
                    departments_salary_dict[record['Department']].append(float(record['Salary']))
            except EOFError:
                break
    for department in departments_salary_dict.keys():
        print(f"Department Name: {department}")
        print(f"Highest Salary in Department: {max(departments_salary_dict[department])}")
        print(f"Lowest Salary in Department: {min(departments_salary_dict[department])}")

while True:
    print('''
1. Add a Record
2. Delete a Record whose Employee ID is given
3. Update the Record of a given Employee
4. Display the Record Department-wise when given Name and ID
5. Display the Record of a particular Employee using ID
6. Department wise highest and lowest salary
7. Exit''')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_record()
    elif choice == 2:
        delete_record()
    elif choice == 3:
        update_record()
    elif choice == 4:
        display_record_department_wise()
    elif choice == 5:
        display_record_by_employee_id()
    elif choice == 6:
        display_department_wise_highest_and_lowest_salary()
    elif choice == 7:
        break
