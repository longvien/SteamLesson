# CÂU HỎI BÀI TẬP
# 
# Ngoài sở thích tìm tòi về máy tính,
# Trẩu và một số bạn trong lớp CS 101 còn thích được trở thành một phi công
# được lái máy bay bay lượn trên bầu trời xanh.
# Để làm phi công, chúng ta phải đạt chuẩn rất nhiều điều kiện như cân nặng, chiều cao, chỉ số BMI... .
# Chúng ta hãy cùng giúp Trẩu viết hàm kiểm tra 2 điều kiện cơ bản nhất là cân nặng và chiều cao nhé!
# Điều kiện về chiều cao: Nếu là nam thì phải cao hơn hoặc bằng 165 cm. Nếu là nữ thì phải cao hơn hoặc bằng 160 cm.
# Điều kiện về cân nặng: Nếu là nam thì phải nặng hơn hoặc bằng 54 kg. Nếu là nữ thì phải nặng hơn hoặc bằng 48 kg.
# Nếu Trẩu và các bạn đạt cả hai điều kiện trên thì mới đạt tiêu chí đăng ký làm phi công.
# 
# Yêu cầu:
# 
# Viết hàm check_condition(gender, height, weight) nhận vào giới tính (chuỗi), chiều cao, cân nặng.
# Hàm cần kiểm tra và trả về True nếu đạt điều kiện hoặc trả về False nếu không đạt điều kiện.
# 
# Học sinh chỉ nộp hàm check_condition(gender, height, weight)

def check_condition(gender, height, weight):
    if (gender == 'nam' and height >= 165 and weight >= 54) or (gender == 'nu' and height >= 160 and weight >= 48):
        return True
    else:
        return False
    