# CÂU HỎI BÀI TẬP
# 
# Sau khi viết hàm enqueue, bây giờ chúng ta sẽ viết hàm dequeue cho queue.
# 
# Yêu cầu:
# 
# Viết hàm dequeue cho queue. Nếu queue không chứa phần tử nào, hàm trả về queue rỗng.
# Nếu queue chứa ít nhất một phần tử,
# hàm sẽ xóa phần tử của queue và trả về queue.

def dequeue(queue):
    # Neu queue khong chua phan tu nao, tra ve queue rong.
    # Neu queue chua it nhat mot phan tu, thay doi queue
    # va tra ve queue
    ans = []
    if not queue:
        return ans
    for index in range(1,len(queue)):
        ans.append(queue[index])
    return ans         