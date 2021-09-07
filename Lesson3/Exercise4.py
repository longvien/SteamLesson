# CÂU HỎI BÀI TẬP
# 
# Cho mảng các số:
# 
# number = [1,2,3,15,40,70,9,100,8] 
# Yêu cầu: 
# 
# In ra tổng các số nhỏ hơn 10 trong mảng number bằng vòng lặp for hoặc while.
# Gợi ý: 
# 
# Dùng vòng lặp đi qua từng phần tử trong mảng. Kiểm tra nếu phần tử nhỏ hơn 10 thì cộng vào tổng.
# 
# Input:
# 
# 
# number = [1,2,3,15,40,70,9,100,8] 
# Output:
# 
# 
# 23
# Sau khi điền code xong, bạn hãy nhấn nút Submit để máy tính tự động kiểm tra.
# Nếu máy tính trả về CORRECT thì xin chúc mừng, bạn đã giành được trọn số điểm.
# Nếu máy tính trả lại là INCORRECT thì bạn có thể ấn vào See full output để xem bài của mình khác với đáp án như thế nào để sửa lại.

# Luu y: Hoc sinh khong khoi tao mang number.  
sum_number = 0
for item in number:    
    if item < 10:
        sum_number = sum_number + item
print(sum_number)   