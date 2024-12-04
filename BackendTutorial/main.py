#pass values statically
class Student:
    first_name = "Layla"
    second_name = "Hasaan"
    gender = "female"
    age = 21

#pass values dynamically
class Person:
    #constructor-allows to pass the values dynamically
    def __init__(self,name,gender,marital_status,occupation):
            #self keyword represents an instance of a class
            #It allows you to access variables, attributes, and methods of a defined class in Python.
        self.name = name
        self.gender = gender
        self.marital_status = marital_status
        self.occupation = occupation
   #methods
    def salutation(self):
        print(f"Good afternoon {self.name}, you are {self.marital_status}")

    def display_name(self):
        print(f"Your name is {self.name}")


#create a class that instantiates variety of animals.Create 4 objects
class Animal:
    def __init__(self,name,species,weight,num_legs,is_domestic):
        self.name = name
        self.species = species
        self.weight = weight
        self.num_legs = num_legs
        self.is_domestic = is_domestic


#create a rectangle that takes in length and width. Create a perimeter method ,area method  and
# a method that displays the length, width, perimeter and area. Create 4 objects
class Rectangle:
    def __init__(self,length,width):
        self.length = float(input(length))
        self.width = float(input(width))

    def perimeter(self):
        return 2 * (self.length+self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print(f"The length is: {self.length}")
        print(f"The width is: {self.width}")
        print(f"The perimeter is: {self.perimeter()}")
        print(f"The area is: {self.area()}")



#inheritance
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def display_name(self):
        return f"{self.name} is {self.age} years old"

class Manager(Employee):
    def __init__(self,name,age,salary,gender,education_level):
        #super declares what we are inheriting from the parent class,Employee
        super().__init__(name,age,salary,gender)
        self.education_level = education_level

class Developer(Employee):
    def __init__(self,name,age,salary,gender,programming_language):
        super().__init__(name,age,salary,gender)
        self.programming_language = programming_language


class SalaryEmployee(Employee):
    def __init__(self,name,age,salary,gender,monthly_salary):
        super().__init__(name,age,salary,gender)
        self.monthly_salary = monthly_salary

    def calculate(self):
        return self.monthly_salary +self.salary

class HoursEmployee(Employee):
    def __init__(self,name,age,salary,gender,hourly_rate,hours_worked):
        super().__init__(name,age,salary,gender)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_payment(self):
        return (self.hourly_rate * self.hours_worked) + self.salary


class CommissionEmployee(SalaryEmployee):
    def __init__(self,name,age,salary,gender,monthly_salary,commission):
        super().__init__(name,age,salary,gender,monthly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate()
        return fixed + self.commission



#create a parent class bankaccount which represents a bank account with its respective attributes
#create a deposit method  that manages the deposit actions
#create a withdrawal method which manages withdrawal actions
# create a bankfees method that appplies bank fees percentage of 5% on the balance in account
#create display method to display account details

#NB ensure the parent class has at least 2 child classes

class BankAccount:
    def __init__(self,account_holder_name, account_number,account_type,account_balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance

    #diplay account details method
    def account(self):
        return f"Account details is {self.account_holder_name}, {self.account_number}, {self.account_type}, {self.account_balance}"

    def validate_account(self):
        account_name = self.account_holder_name.upper()
        account_no = input("Enter your account number: ")
        if account_name == self.account_holder_name and account_no == self.account_number:
            print("Account details are valid")
        else:
            print("Enter valid account details")

    #deposit method
    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.account_balance += deposit_amount
            total = self.account_balance

            print(f"Deposit successful. Your new account balance is {total}")
        else:
            print("Invalid deposit amount.")

    #withdraw method
    def withdraw(self, withdraw_amount):
        if withdraw_amount > 0 and withdraw_amount <= self.account_balance:
            self.account_balance -= withdraw_amount
            print(f"Withdrawal successful. The account_balance is {self.account_balance}")
        else:
            print("Insufficient funds in your account. Top up your account")

    #bank fees method
    def bank_fees(self):
        fee_amount = self.account_balance * 0.05
        self.account_balance -= fee_amount
        print(f"Bank Fees {fee_amount} from your account balance has been applied successful. Your account balance is {self.account_balance}")

class SavingsAccount(BankAccount):
    def __init__(self,account_holder_name,account_number,account_type,account_balance,interest_rate):
        super().__init__(account_holder_name,account_number, account_type, account_balance)
        self.interest_rate = interest_rate


    #method that calculates interest for the saving accounts
    def calculate_interest(self):
        interest = self.account_balance * self.interest_rate
        self.account_balance = self.account_balance + interest
        print(f"The interest for your account is {interest}")
        print(f"Your new account balance is {self.account_balance}")





"""
Create a Vehicle class in Python with a start() method that prints 'Vehicle is starting.' Then, create two subclasses, Car and Bike, where each has an overridden start() method that prints specific messages. Test both to see how method overriding works in Python.

 

Write a Device class in Python with an init() method that takes brand and year as parameters.
Then create a Phone subclass that inherits Device and adds a new attribute model.
 Use the super() function to call the Device initializer from the Phone class. 
Test it by creating a Phone object and printing out all attributes.

"""

class Vehicle:
    def __init__(self,brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print("Vehicle is starting.")

class Car(Vehicle):
    def __init__(self,brand, year,milesperhour):
        super().__init__(brand, year)
        self.milesPerHour = milesperhour

    def start(self):
        print(f"Car with {self.milesPerHour} miles per hour is starting.")

class Bike(Vehicle):
    def __init__(self,brand, year,color):
        super().__init__(brand, year)
        self.color = color
    def start(self):
        print(f"Bike with {self.color} color is starting.")



class Device:
    def __init__(self,brand, year):
        self.brand = brand
        self.year = year

class Phone(Device):
    def __init__(self,brand, year,model):
        super().__init__(brand, year)
        self.model = model

    def phone_details(self):
        print(f"Your phone details are {self.brand}, {self.year}, {self.model}")











