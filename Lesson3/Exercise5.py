# CÂU HỎI BÀI TẬP
# Chúng ta có array 
# 
# trials = [[2,4,6],[3,5,7]]
# Yêu cầu: 
# 
# Dùng hai vòng lặp lồng nhau để in ra tất cả các phần tử của mảng trials.
# Gợi ý 1: 
# 
# Dùng một vòng lặp để đi qua từng mảng con.
# Trong vòng lặp đó, hãy dùng một vòng lặp khác để đi qua từng phần tử bên trong mảng con và in ra màn hình.
# 
# Gợi ý 2: 
# 
# Dùng một vòng lặp để đi qua các hàng và trong vòng lặp đó hãy dùng một vòng lặp khác để đi qua các cột. 
# 
# Input:
# 
# trials = [[2,4,6],[3,5,7]]
# Output
# 
# 2
# 4
# 6
# 3
# 5
# 7
# Sau khi điền code xong, bạn hãy nhấn nút Submit để máy tính tự động kiểm tra.
# Nếu máy tính trả về CORRECT thì xin chúc mừng, bạn đã giành được trọn số điểm.
# Nếu máy tính trả lại là INCORRECT thì bạn có thể ấn vào See full output để xem bài của mình khác với đáp án như thế nào để sửa lại.

# Luu y: Hoc sinh khong khoi tao mang trials.
for row in range(len(trials)):
    for column in range(len(trials[0])):
        print(trials[row][column])
          