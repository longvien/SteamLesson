# CÂU HỎI BÀI TẬP
# 
# Từ một từ gốc, chúng ta có thể tạo ra nhiều từ ngữ khác nhau.
# Ví dụ như trong tiếng Việt, khi ta có từ “bánh”, ta có thể liệt kê ra tên gọi của nhiều
# loại bánh khác nhau: bánh rán, bánh mì, bánh ngọt, v.v…
# 
# Với bài tập lần này, bạn Trẩu của chúng ta phải làm một nhiệm vụ đó là:
#     Tạo ra một hàm mà có thể lấy một từ gốc và thêm vào từ gốc đó một từ khác để thành một từ mới.
# 
# Qua bài tập này, chúng ta có thể hiểu hơn về khái niệm Phạm vi (Scope).
# Mặc dù 2 hàm đều nhận vào cùng 1 tham số, nhưng khi thay đổi giá trị của tham số đấy ở trong từng hàm,
# giá trị của tham số đấy sẽ không bị ảnh hưởng giữa các hàm với nhau.
# 
# Yêu cầu:
# 
# Tạo ra 2 hàm có cùng tham số, function1(string) và function2(string)
# 
# Trong hàm function1(string), thêm vào chuỗi string chuỗi “ Tom" và trả lại chuỗi mới đó.
# 
# Trong hàm function2(string), thêm vào chuỗi string chuỗi “ Jerry" và trả lại chuỗi mới đó.
# 
# Lỗi thường gặp:
# 
# Nếu gặp lỗi 'TypeError: got an unexpected keyword argument "string"' có nghĩa là
# hàm chưa có tham số (input) tên là string theo yêu cầu đề bài.

def function1(string):
    string = string + " Tom"
    return string
def function2(string):      
    string = string + " Jerry"
    return string