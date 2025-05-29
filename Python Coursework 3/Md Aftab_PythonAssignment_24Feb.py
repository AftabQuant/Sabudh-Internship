# Topic: Object Oriented Programming using Python.

# Task 1: Creating a Class (Abstraction)..
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
    def __str__(self):
        return f"Name:{self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"

    def greet(self):
        return f"Hello {self.name}! My name is Jane..."

    @abstractmethod
    def introduce(self):
        pass
    @staticmethod
    def is_adult(self):
        return self.age>18

class Child(Person):
    def introduce(self):
        print("I am from child class...")
        return f"Hi, i am {self.name}, my age is {self.age}, my gender is {self.gender} and my address is {self.address}"

def call_all_function(x):
    print(str(x))
    print(x.greet())
    print(x.introduce())
    print(x.is_adult())
    print()

john = Child("Alice", 20, "Female", "123 Main St")
call_all_function(john)

bob= Child("Bob", 17, "Male", "456 Elm St")
call_all_function(bob)


# Task 2: Single Inheritance, Encapsulation
class Employee(Person):
      count = 0
      def __init__(self, name, age, gender, address, employee_id, salary):
          super().__init__(name, age, gender, address)
          self.__employee_id = employee_id
          self._salary = salary
          Employee.count += 1

      def __del__(self):
          Employee.count -= 1

      def getter(self):
          return self.__employee_id

      @classmethod
      def counter(cls):
          return cls.count

      def getter_salary(self):
          return self._salary
      def setter_salary(self, salary):
          self._salary = salary

      def inc_salary(self, increment):
          self._salary += increment

      def dec_salary(self, decrement):
          self._salary -= decrement

      def introduce(self):
          return f" My name is: {self.name}, my age is: {self.age}, my gender is: {self.gender}, my address is: {self.address} and salary is : {self._salary}"

employee_1 = Employee("Alice", 20, "Female", "123 Main St", "EMP01", 50000)
print(employee_1.counter())
print(employee_1.getter())
print(employee_1.setter_salary(60000))
print(employee_1.getter_salary())
employee_1.inc_salary(15000)
print(employee_1.getter_salary())
print(employee_1.introduce())

# Task 3: Multiple Inheritance, Polymorphism
class Teacher(Employee, Person):
    count = 0
    def __init__(self, name, age, gender, address, employee_id, salary, teacher_id, subjects):
        super().__init__(name, age,gender,address,employee_id, salary)
        self.count += 1
        self.__teacher_id = teacher_id
        self.subjects = subjects if subjects else []

    def __del__(self):
        self.count -=1

    def get_teacher_id(self):
        return self.__teacher_id

    # The class should have the following methods:
    def counter(self):
        return self.count

    @property
    def employee_id(self):
        raise AttributeError(f"{self.__class__.__name__} object has no attribute 'employee_id'.")

    def add_subject(self, sub):
        self.subjects.append(sub)
    def remove_subject(self, sub):
        self.subjects.remove(sub)

    def introduce(self):
        return f"Teacher is is: {self.__teacher_id}, the subjects are: {self.subjects}"


teacher = Teacher("Bob", 40, "Male", "456 Avenue, City", "EMP01", 60000, "TEC01", ["Math", "Science"])
print(teacher.introduce())