# YÊU CẦU BÀI TẬP
# Hỏi người chơi “Ban hay dien vao mot con so: “.
# In ra màn hình “Day la so chan" hoặc “Day la so le" dựa theo tính chẵn lẻ của số đó.
# 
# Ví dụ 1:
# 
# Ban hay dien vao mot con so: 4
# Day la so chan
# Ví dụ 2:
# 
# Ban hay dien vao mot con so: 199
# Day la so le
# Sau khi điền code xong, bạn hãy nhấn nút Submit để máy tính tự động kiểm tra.
# Nếu máy tính trả về CORRECT thì xin chúc mừng, bạn đã giành được trọn số điểm.
# Nếu máy tính trả lại là INCORRECT thì bạn có thể ấn vào See full output để xem bài của mình khác với đáp án như thế nào để sửa lại.

number = int(input("Ban hay dien vao mot con so: "))
if number%2==0:
    print("Day la so chan")
else:
    print("Day la so le")