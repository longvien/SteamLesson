# CÂU HỎI BÀI TẬP
# 
# Ở ngoài đời, từng bạn trong lớp sau mỗi năm lớn thêm một tuổi.
# Tương tự như vậy, cô giáo của Trẩu muốn các bạn trong trò chơi của mình cũng có khả năng lớn thêm một tuổi và
# thông báo sinh nhật mỗi khi đến dịp.
# Các con có thể thấy mỗi nhân vật mà được khởi tạo từ lớp (class) Person đều có thuộc tính tuổi (age), và
# các con có thể cho một phương thức vào lớp (class) Person để thay đổi chính thuộc tính này!
# 
# Yêu cầu:
# 
# Tiếp tục sử dụng lớp Person vừa tạo
# 
# Tạo thêm phương thức increase_age() để tăng thêm 1 tuổi mỗi khi vào dịp sinh nhật
# 
# Khi gọi phương thức increase_age,
# thuộc tính age của lớp được tăng thêm 1 và trên màn hình sẽ được in ra “It's my birthday! I'm [x] years old now.”

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("Hi, I'm " + self.name + ". " + "I'm " + str(self.age) + " years old.")
    
    def increase_age(self):
        self.age = self.age + 1
        print("It's my birthday! I'm " + str(self.age) + " years old now.")