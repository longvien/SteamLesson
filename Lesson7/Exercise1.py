# CÂU HỎI BÀI TẬP
# 
# Các con đã học về stack trong lớp, chúng ta hãy cùng viết các hàm cho nó nhé! Chúng ta hãy bắt đầu bằng hàm push.
# 
# Yêu cầu:
# 
# Viết hàm push cho stack. Hàm push sẽ thêm phần tử value vào stack và trả về stack.

def push(stack, value):
    # thay doi va tra ve stack
    ans = stack
    ans.append(value)
    return ans
      