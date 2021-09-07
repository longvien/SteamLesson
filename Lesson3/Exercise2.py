# CÂU HỎI BÀI TẬP
# 
# Cho mảng gồm tên các thầy trong khoá CS101:
# names = ["Vincent","Duc","Hung"]
# Yêu cầu: 
# Dùng hai vòng lặp for lồng nhau với mảng names để in các chữ cái trong tên các thầy trong khoá CS101.
# Gợi ý: 
# 
# Dùng một vòng lặp để đi qua từng tên trong mảng names.
# Trong vòng lặp đó, hãy dùng một vòng lặp khác để đi qua từng kí tự trong tên và in ra màn hình.
# 
# Input:
# 
# names = ["Vincent","Duc","Hung"]
# Output
# 
# 
# V
# 
# i
# 
# n
# 
# c
# 
# e
# 
# n
# 
# t
# 
# D
# 
# u
# 
# c
# 
# H
# 
# u
# 
# n
# 
# g
# Sau khi điền code xong, bạn hãy nhấn nút Submit để máy tính tự động kiểm tra.
# Nếu máy tính trả về CORRECT thì xin chúc mừng, bạn đã giành được trọn số điểm.
# Nếu máy tính trả lại là INCORRECT thì bạn có thể ấn vào See full output để xem bài của mình khác với đáp án như thế nào để sửa lại.

# Luu y: Hoc sinh khong khoi tao mang names.  
for name in names:
    for letter in name:
        print(letter)         