# CÂU HỎI BÀI TẬP
# 
# Một vật thể được khởi tạo từ lớp sẽ sở hữu hết tất cả các thuộc tính và phương thức mà lớp đó có.
# Phương thức là hành động mà vật thể được tạo ra có thể truy cập và để thực hiện.
# Cô giáo của Trẩu muốn tất cả các nhân vật trong trò chơi đều có thể làm một hành động đơn giản: tự giới thiệu bản thân.
# Để mở rộng cho lớp Person chúng ta vừa tạo, con hãy thêm phương thức (method) introduce cho lớp đấy.
# 
# Yêu cầu:
# 
# Sử dụng lớp Person vừa tạo ở bài thực hành 1 (chứa thuộc tính name, age).
# 
# Tạo thêm phương thức introduce().
# 
# Khi gọi phương thức introduce, trên màn hình sẽ được in ra "Hi, I'm [name]. I'm [x] years old.".

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("Hi, I'm " + self.name + ". " + "I'm " + str(self.age) + " years old.")
        