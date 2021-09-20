# CÂU HỎI BÀI TẬP
# 
# Sau cùng, chúng ta hãy giúp các bạn được tạo ra từ lớp Person tương tác với nhau nhé.
# 
# Yêu cầu:
# 
# Sử dụng lớp Person vừa tạo
# 
# Tạo thêm phương thức greet nhận vào 1 đối tượng khác của lớp Person.
# 
# Khi gọi phương thức greet, trên màn hình sẽ được in ra "Hi, [tên đối tượng được nhận vào]! I'm [name]. Nice to meet you!"

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age        
    def introduce(self):
        print("Hi, I'm " + self.name + ". " + "I'm " + str(self.age) + " years old.")
    def increase_age(self):
        self.age = self.age + 1
        print("It's my birthday! I'm " + str(self.age) + " years old now.")
    def greet(self, person):
        print("Hi, " + person.name + "! I'm " + self.name + ". Nice to meet you!")
        
