# YÊU CẦU BÀI TẬP
# Hỏi người chơi “Ban hay dien vao mot con so: “.
# In ra màn hình tổng các số từ 1 đến số đó.
# 
# Ví dụ 1:
# 
# Ban hay dien vao mot con so: 4
# 10
# Ví dụ 2:
# 
# Ban hay dien vao mot con so: 3
# 6
# Ví dụ 3:
# 
# Ban hay dien vao mot con so: 6
# 21
# Sau khi điền code xong, bạn hãy nhấn nút Submit để máy tính tự động kiểm tra.
# Nếu máy tính trả về CORRECT thì xin chúc mừng, bạn đã giành được trọn số điểm.
# Nếu máy tính trả lại là INCORRECT thì bạn có thể ấn vào See full output để xem bài của mình khác với đáp án như thế nào để sửa lại.

number = int(input("Ban hay dien vao mot con so: "))
sum=0
counter=0
while counter<number:
    counter=counter+1
    sum=sum+counter
print(sum)