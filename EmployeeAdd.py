#This is a program that will keep track of all employees in my company
#By Emily :)

fileName = "Employees.txt" #file to store employees
Employees = open(fileName,"a")

employee = {} #list to keep employees

def printEmployee(Employee): #function to print dictionary
    for item in Employee:
            print ("{}: {}".format(item,str(Employee[item])))

class Employee: #class to store employees' info
    #class attribute
    company = "EmilyEnterprises"
    #initialize the employee objects
    def __init__(self,lastName,firstName,title,telNum,email,city):
        self.lastName = lastName
        self.firstName = firstName
        self.title = title
        self.telNum = telNum
        self.email = email
        self.city = city

    def AddEmployee(): #function to add new employees
        question = input("Would you like to add an employee?: ")
        #if user wants to add another employee follow code
        if question.lower() == 'yes':
            First = input("Enter the first name of the employee: ")
            Last = input("Enter the last name of the employee: ")
            Title = input("Enter the title of the employee: ")
            Telephone = input("Enter the telephone number of the employee: ")
            Email = input("Enter your email: ")
            City = input("What city does the employee live in?: ")
            employee = Employee(Last,First,Title,Telephone,Email,City)
            #creating dictionary to add employee to list
            Name = employee.__dict__
            print("\n")
            printEmployee(Name)
            answer = input("Is this information correct?: ")
            if answer.lower() == 'yes':
                for item in Name:
                    Employees.write(("{}: {}\n".format(item,str(Name[item]))))
                return Employee.AddEmployee()
            return Name
        elif question.lower() == 'no':
            print ("Ok! Thank you for using my program.")
        else:
            print("INVALID INPUT")
            return Employee.AddEmployee()


class CameraMan(Employee): #subclass of Employee
    department = "Camera Crew"
    salery = 48000
    def job(position):
        self.position = position

class Editor(Employee): #subclass of Employee
    department = "Editting"
    salery = 45000
    def job(position):
        self.position = position

class Writer(Employee): #subclass of Employee
    department = "Script Writing"
    salery = 50000
    def job(position):
        self.position = position

class Director(Employee): #subclass of Employee
    department = "Directing"
    salery = 65000
    def job(position):
        self.position = position

#will be shown to user
print('The company is called Emily Enterprises.')
print('This program will add an employee to the file.')
print("\n")

#pompting user to enter new employee
newUser = Employee.AddEmployee()

#to add employee to list if possible
try:
    employee.update(newUser)
except:
    print('\n')
    print("No employee to write to file.")

Employees.close() #close Employees.txt
