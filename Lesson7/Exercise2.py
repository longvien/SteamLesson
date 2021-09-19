# CÂU HỎI BÀI TẬP
# 
# Sau khi viết hàm push, bây giờ chúng ta sẽ viết hàm pop cho stack.
# 
# Yêu cầu:
# 
# Viết hàm pop cho stack. Nếu stack không chứa phần tử nào, hàm trả về stack rỗng.
# Nếu stack chứa ít nhất một phần tử, hàm sẽ xóa một phần tử của stack và trả về stack.

def pop(stack):
    # thay doi va tra ve stack
    ans = []
    if not stack:
        return ans
    else:
        for index in range(0,len(stack)-1):
            ans.append(stack[index])
    return ans