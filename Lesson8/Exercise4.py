# CÂU HỎI BÀI TẬP
# 
# Trong trò chơi mà cô giáo Trẩu đang tạo ra, tuổi là một yếu tố rất quan trọng.
# Vì vậy, các con hãy tạo một hàm để so sánh tuổi của các nhân vật mà là vật thể được khởi tạo từ lớp Person nhé.
# Sau khi tạo ra lớp Person rồi, con hãy viết hàm compare_age để so sánh tuổi của các bạn nhé.
# 
# Yêu cầu:
# 
# Tạo một hàm compare_age(person1,person2) nhận vào 2 đối tượng của lớp Person
# 
# Hàm này sẽ so sánh tuổi của 2 đối tượng được nhận vào, và in ra trên màn hình "[Name 1] is older than [Name 2]"
# 
# Nếu 2 bạn bằng tuổi thì in ra “[Name 1] and [Name 2] are of the same age"
# 
# Học sinh chỉ cần nộp code của hàm compare_age, không cần nộp code của lớp Person

def compare_age(person1, person2):
    if person1.age < person2.age:
        print(person2.name +" is older than " + person1.name)
    elif person1.age > person2.age:
        print(person1.name +" is older than " + person2.name)
    else:
        print(person1.name + " and " + person2.name + " are of the same age")
       