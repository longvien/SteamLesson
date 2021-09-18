# CÂU HỎI BÀI TẬP
# 
# Một ngày nọ, trong giấc mơ, Trẩu thấy mình bị bắt vào thế giới song song trong gương.
# Ở thế giới trong gương, mọi vật đều bị viết ngược lại.
# Ví dụ, một mảng chứa các chữ [“a”, “b”, “c”] sẽ bị viết hoán đổi thành [“c”, “b”, “a”].
# Nhà vua của thế giới trong gương bắt Trẩu viết nên một chương trình có khả năng đảo ngược vị trí của các phần tử
# trong một mảng mới cho phép Trẩu quay trở lại. Trẩu phải làm cách nào bây giờ?
# 
# Yêu cầu:
# 
# Viết hàm reverse_array(array) nhận vào array và trả lại mảng mới đã được đảo ngược

def reverse_array(array):
    ans = []
    n = len(array)
    counter = n - 1
    while counter >= 0:
        ans.append(array[counter]) 
        counter = counter - 1
    return ans    