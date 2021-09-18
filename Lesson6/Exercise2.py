# CÂU HỎI BÀI TẬP
# 
# Trẩu vừa thiết kế ra một chú robot có khả năng giao báo và tạp chí đến từng nhà một.
# Robot của Trẩu có nhiệm vụ giao báo đến các nhà mang số chẵn.
# 
# Ở khu phố mà Trẩu đang sinh sống, số nhà không được phân ra thành chẵn hay lẻ một cách rõ ràng.
# Robot của Trẩu có thể tiếp nhận số nhà của từng nhà trên phố thành một mảng
# nhưng nó không có khả năng phân biệt các số nhà là số chẵn hay số lẻ. Hãy giúp robot của Trẩu làm nhiệm vụ nhé!
# 
# Yêu cầu:
# 
# Viết hàm get_even(array) nhận vào array và trả lại mảng mới chỉ chứa số chẵn từ array đầu vào.
# 
# Phần tử trong mảng trả về phải đúng trình tự xuất hiện trong mảng nhận vào.

def get_even(array):
   ans = []
   for number in array: 
       if number%2 == 0:
           ans.append(number)
   return ans
    