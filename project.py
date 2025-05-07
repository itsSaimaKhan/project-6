# Project 6: Buuild_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series
# Instructor: Saima Khan

# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize
# these values via a constructor. Add a method display() that prints student details.

# solution:
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display(self):
#         print(f" Student Name: {self.name}")
#         print(f" Student Marks: {self.marks}")
        
# student1 = Student("saima", 85)   
# student1.display()     


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable
# and a class method with cls to manage and display the count.

# solution:
# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1

#     @classmethod
#     def display_count(cls):
#         print(f"MY total created objects are: {cls.count}")
        
# obj1 = Counter()
# obj2 = Counter()
# obj3 = Counter()
# obj4 = Counter()

# Counter.display_count()  # Output: Total objects created: 4    

# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate 
# the class and access both from outside the class. 

# solution:
# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         print(f"{self.brand} is starting.")
        
my_car = Car("Toyota")
print(my_car.brand)  # Accessing public variable
my_car.start()  # Calling public method           