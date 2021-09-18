# CÂU HỎI BÀI TẬP
# 
# Bạn Trẩu đi nhà sách và muốn mua giấy để vẽ những bước thuật toán.
# Loại giấy bạn Trẩu mua là loại giấy hình chữ nhật. Giá để mua giấy là 2 đồng/cm2. Chúng hãy tính số tiền Trẩu cần trả khi biết giấy Trẩu mua có diện tích là chiều dài x chiều rộng.
# Công thức tính tiền:
# Số tiền cần trả = Diện tích của tờ giấy x 2.
# 
# Yêu cầu:
# 
# Viết hàm paper_price(length, width) nhận vào length (chiều dài) và width (chiều rộng) của tờ giấy Trẩu muốn mua.
# Hàm này sẽ trả về số tiền Trẩu cần trả.
# 
# Học sinh chỉ nộp hàm paper_price(length, width).

def paper_price(length, width):
    return length * width * 2