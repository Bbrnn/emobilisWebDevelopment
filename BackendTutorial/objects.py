from main import Student, Person, Animal, Rectangle, Employee, Developer, Manager, SalaryEmployee, CommissionEmployee, \
    HoursEmployee, SavingsAccount, Device
from main import BankAccount

from main import Vehicle,Car,Device,Phone

student1 = Student()
print(student1.first_name)
print(student1.second_name)
print(student1.gender)
print(student1.age)


student2 = Student()
print(student2.first_name)
print(student2.second_name)
print(student2.gender)
print(student2.age)

person1 = Person("Jane","Female","single","doctor")
print(person1.name)
print(person1.gender)
print(person1.marital_status)
print(person1.occupation)

person2 = Person("Holland","Male","married","engineer")
person3 = Person("Yake","Male","Divorced","chef")
print(f"name: {person3.name}, gender: {person3.gender}, marital_status: {person3.marital_status}, occupation: {person3.occupation}")

#accessing the method within the person class
person1.salutation()
person2.salutation()
person3.salutation()

person3.display_name()


#Animal class
animal1 = Animal("Farah","Dog",20, 4,True)
animal2 = Animal("Chia","Bird",0.2, 2,False)
animal3 = Animal("Yam","Fish",0.6,0,False)
animal4 = Animal("Ugway","Snake",2.0,0,False)
#Print the names of all the animals
print("The name of all the animals are:")
print(animal1.name)
print(animal2.name)
print(animal3.name)
print(animal4.name)

print("Animal 2 is:")
print(f"name {animal2.name},species {animal2.species}, weight {animal2.weight},num_legs {animal2.num_legs}, is_domestic {animal2.is_domestic}")

#rectangle class
#rect1 = Rectangle("Length of rectangle 1:","Width of rectangle 1 is:")
#rect2 = Rectangle("Length of rectangle 2:","Width of rectangle 2 is:")
#rect3 = Rectangle("Length of rectangle 3:","Width of rectangle 3 is:")
#rect4 = Rectangle("Length of rectangle 4:","Width of rectangle 4 is:")
#rect1.display()

#rect4.display()




#inheritance
employee1 = Employee("Jane",23,20000,"Female")
manager1 = Manager("Jones",32,30000,"Male","Doctorate")
developer1 = Developer("Jack","Jones",20000,"Female","Kotlin")
salary1 = SalaryEmployee("jack",45,30000,"Male",3000)
hoursEmployee1=HoursEmployee("leila",19,6000,"female",300,8)
commissionEmployee1=CommissionEmployee("Jilian",23,20000,"Male",3000,800)
print(employee1.display_name())
print(manager1.display_name())

print(salary1.calculate())
print(hoursEmployee1.calculate_payment())

print(commissionEmployee1.calculate_payroll())


Account1 = BankAccount("bridget",45345666,"Savings",40000)
print(Account1.account())
Account1.validate_account()

Account1.deposit(400)
Account1.withdraw(400)
Account1.bank_fees()

Account2 = BankAccount("jeremy",12345678, "Savings",2100)
print(Account2.account())
Account2.deposit(-400)
Account2.withdraw(800)
Account2.bank_fees()

savings_account1 = SavingsAccount("Ginga",123458,"Savings",200, 0.02)
print(savings_account1.calculate_interest())


Vehicle1 = Vehicle("lorry",2023)
Vehicle1.start()
Car1 = Car('car',2024,500)
Car1.start()

device1 = Device("tablet",2021)

phone1 = Phone("samsung","Year: 2022","galaxy")
phone1.phone_details()

