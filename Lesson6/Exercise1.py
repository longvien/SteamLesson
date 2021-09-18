# CÂU HỎI BÀI TẬP
# 
# Bạn Trẩu của chúng ta vừa viết ra một chương trình để ghi lại danh sách các đồ vật cần mua khi cả nhà đi siêu thị.
# Chương trình để ghi lại danh sách này sẽ hoạt động như sau:
# Từng thành viên của gia đình có thể đánh vào chương trình một câu bao gồm tất cả các vật dụng cần mua
# được chia bởi dấu cách (“ “)
# 
# Ví dụ, khi mẹ của Trẩu viết:
# 
# Orange, apple, cheese
# Bạn Trẩu biết rằng mẹ của bạn cần mua 3 thứ ở siêu thị là Orange (cam), apple (táo), và cheese (phô mai).
# Tuy nhiên, nhiều thành viên trong nhà Trẩu đánh máy không được chính xác cho lắm. Thỉnh thoảng, em của
# Trẩu hay viết như sau:
# 
# Candy,               banana,                           apple
# Cách đánh máy này thật lạ vì có quá nhiều khoảng trống ở giữa! Tuy khó nhìn, nó vẫn là một list đồ cần mua hợp lý.
# Trẩu muốn làm gì đó để chỉnh cho các input nhập vào sao thật đẹp và đúng ý mình hơn.
# Ví dụ, khi em Trẩu đánh dòng trên, Trẩu muốn biến đổi dòng đó thành list các đồ vật cần mua để dễ nhìn hơn:
# 
# [Candy, banana, apple]
# Yêu cầu:
# 
# Viết hàm process_string(string) nhận vào string và trả lại mảng với phần tử là các chữ trong câu được đưa vào.
# 
# Sử dụng hàm strip() để xoá đi các dấu cách thừa ở đầu và cuối câu.
# 
# Sử dụng hàm split() để chia các từ ở cách dấu cách.
# 
# Học sinh chỉ nộp hàm process_string(string).

def process_string(string):
    return string.replace("_"," ").strip().split()