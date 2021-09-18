# CÂU HỎI BÀI TẬP
# 
# Trẩu vừa mới được học trên lớp về khái niệm median,
# là số nằm chính giữa trong 1 dãy số đã được sắp xếp theo thứ tự tăng dần hoặc giảm dần.
# Số median khác số trung bình cộng ở chỗ nó không bị làm lệch đi bởi một số phần tử số mà nhỏ quá hay to quá,
# bởi nó không bị cộng dồn và chia ra. Hãy giúp Trẩu tìm số median trong một mảng các số từ gợi ý bên dưới nhé!
# 
# Yêu cầu:
# 
# Viết hàm find_median(array) nhận vào array và trả về phần tử ở giữa trong 1 mảng đầu vào đã được sắp xếp
# 
# Nếu số phần tử trong mảng là số lẻ, trả về phần tử ở giữa
# 
# Nếu số phần tử trong mảng là số chẵn, trả về trung bình cộng của 2 phần tử ở giữa
# 
# Nếu array nhận vào bị rỗng thì trả về giá trị None

def find_median(array):
    n = len(array)
    if n == 0:
        return None
    if n%2 == 0:
        return (array[int(n/2)-1] + array[int(n/2)]) /2
    else:
        return array[int(n/2)]