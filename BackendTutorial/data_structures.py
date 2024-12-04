"""
Lists
sets
tuples


"""











#Create a dictionary with more than 5 items
Student1 = {
     'name' : 'Bridget',
     'age': 20,
    'location': 'Nyeri',
    'course': 'Computer science',
    'hobby':'Sketching'
}
print(Student1)
if 'age' in Student1:
    print(Student1['age'])

#perfrom a logical AND opeartion
for num in range(1,11):
    if num % 2 == 1:
        print("Odd")
    elif num % 2 ==0 and num % 5 == 0:
        print("Divisible by 2 and 5")
    else:
        print(num)
