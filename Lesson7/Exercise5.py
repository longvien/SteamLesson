# CÂU HỎI BÀI TẬP
# 
# Danh sách các học sinh trong lớp của Trẩu được lưu trữ dưới dạng mảng profiles gồm các từ điển.
# Mỗi từ điển bao gồm 2 phần tử ứng với 2 khoá: name, score.
# Khoá 'name' lưu tên học sinh và khoá 'score' lưu điểm của học sinh đó.
# 
# Yêu cầu:
# 
# Viết hàm get_average_score trả về điểm trung bình của tất cả học sinh trong lớp của Trẩu.

def get_average_score(profiles):
    # tra ve diem trung binh
    sum_score = 0
    for profile in profiles:
        sum_score = sum_score + profile["score"]
    return sum_score/len(profiles)