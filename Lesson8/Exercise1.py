# CÂU HỎI BÀI TẬP
# 
# Khái niệm class đã học trên lớp vô cùng có ích -- nó là
# một cái khuôn mà từ đó máy tính có thể tạo ra nhiều phiên bản vật thể của cái khuôn đó.
# Ví dụ, Tre muốn mở tiệm trà chanh. Trẩu và Tre bèn tạo một lớp (class) tên là trà chanh (lemon_tea) và cứ mỗi lần khách hàng mua một cốc,
# máy tính khởi tạo một vật thể (object) theo khuôn mẫu của lớp lemon_tea ở trên. Việc khởi tạo một vật thể dựa trên khuôn mẫu trà chanh đã có
# cho phép Trẩu và Tre có thể thêm thuộc tính cho vật thể đó (ví dụ, cùng là khuôn mẫu trà chanh, nhưng có khách uống ít đường,
# có khách uống nhiều đá,...).
# Cô giáo của Trẩu đang làm một trò chơi mà tất cả nhân vật là các thành viên trong lớp.
# Bởi việc xác lập khuôn mẫu từ lớp (class) có ích như vậy, nên ở bài dưới đây,
# cô giáo muốn nhờ Trẩu thiết lập một khuôn mẫu tên là Person để chúng ta có thể khởi tạo các vật thể mà là các bạn trong lớp lúc sau.
# 
# Yêu cầu:
# 
# Định nghĩa lớp Person
# 
# Lớp Person có 2 thuộc tính (attribute) là name (tên) và age (tuổi)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
      