# YÊU CẦU BÀI TẬP
# 
# Hỏi người chơi “Ban hay dien vao mot con so: “.
# 
# So sánh số đó với 100, nếu số đó lớn hơn 100 thì in ra “Cao hon 100”,  nếu không thì in ra “Thap hon hoac bang 100"
# 
# 
# Ví dụ 1:
# 
# 
# Ban hay dien vao mot con so: 99
# Thap hon hoac bang 100
# Ví dụ 2:
# 
# Ban hay dien vao mot con so: 101
# Cao hon 100
# 
# Sau khi điền code xong, bạn hãy nhấn nút Submit để máy tính tự động kiểm tra.
# Nếu máy tính trả về CORRECT thì xin chúc mừng, bạn đã giành được trọn số điểm.
# Nếu máy tính trả lại là INCORRECT thì bạn có thể ấn vào See full output để xem bài của mình khác với đáp án như thế nào để sửa lại.

number = int(input("Ban hay dien vao mot con so: "))
if number > 100:
    print("Cao hon 100")
else:
    print("Thap hon hoac bang 100")
