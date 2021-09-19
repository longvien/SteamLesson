# CÂU HỎI BÀI TẬP
# 
# Chúng ta sẽ bắt đầu viết các hàm cho Queue. Chúng ta hãy bắt đầu bằng hàm enqueue.
# 
# Yêu cầu:
# 
# Viết hàm enqueue cho queue. Hàm enqueue sẽ thêm phần tử value vào queue và trả về queue.

def enqueue(queue, value):
    # thay doi va tra ve queue
    ans = queue
    ans.append(value)
    return ans
      
      