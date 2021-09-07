# CÂU HỎI BÀI TẬP
# 
# Cho mảng
# 
# 
# trials = [30,70,100,10]
# Yêu cầu: 
# 
# Dùng vòng lặp for hoặc while tìm số nhỏ nhất trong mảng trials. In ra số nhỏ nhất.
# Input
# 
# 
# trials = [30,70,100,10]
# Ouput
# 
# 
# 10
# 
# Sau khi điền code xong, bạn hãy nhấn nút Submit để máy tính tự động kiểm tra.
# Nếu máy tính trả về CORRECT thì xin chúc mừng, bạn đã giành được trọn số điểm.
# Nếu máy tính trả lại là INCORRECT thì bạn có thể ấn vào See full output để xem bài của mình khác với đáp án như thế nào để sửa lại.

# Luu y: Hoc sinh khong khoi tao mang trials.  
min_number = trials[0]
for number in trials:
    if min_number > number:
        min_number = number
print(min_number)      