##1.Student marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def getMarks(self):
        return self.__marks

    def setMarks(self, marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")


student1 = Student("Mouna", 85)
student2 = Student("Lakshmi", 72)

print("Student 1:", student1.name)
print("Marks:", student1.getMarks())

student1.setMarks(95)

print("Updated Marks:", student1.getMarks())

print()

print("Student 2:", student2.name)
print("Marks:", student2.getMarks())

student2.setMarks(80)

print("Updated Marks:", student2.getMarks())

##2.product price
class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price")


product1 = Product("Laptop", 50000)
product2 = Product("Headphones", 3000)

print("Product 1:", product1.name)
print("Price:", product1.getPrice())

product1.setPrice(55000)

print("Updated Price:", product1.getPrice())

print()

print("Product 2:", product2.name)
print("Price:", product2.getPrice())

product2.setPrice(3500)

print("Updated Price:", product2.getPrice())

##3.Mobile Phone
class Mobile:
    def __init__(self, brand, battery):
        self.brand = brand
        self.__battery = battery

    def getBattery(self):
        return self.__battery

    def setBattery(self, battery):
        if battery >= 0 and battery <= 100:
            self.__battery = battery
        else:
            print("Invalid battery percentage")


mobile1 = Mobile("Samsung", 60)
mobile2 = Mobile("Apple", 40)

print("Mobile 1:", mobile1.brand)
print("Battery:", mobile1.getBattery())

mobile1.setBattery(90)

print("Updated Battery:", mobile1.getBattery())

print()

print("Mobile 2:", mobile2.brand)
print("Battery:", mobile2.getBattery())

mobile2.setBattery(75)

print("Updated Battery:", mobile2.getBattery())