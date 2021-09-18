# CÂU HỎI BÀI TẬP
# 
# Trẩu muốn viết một hàm để tính điểm của vaccine từ mảng trials. Mảng trials chứa điểm của các lần thử nghiệm vaccine. Điểm vaccine được tính bằng cách lấy tổng điểm của các lần thử nghiệm chia cho số lần thử nghiệm.
# 
# Yêu cầu:
# 
# Viết hàm calculate_score(trials) nhận vào một mảng trials.
# Sau đó hàm cần tính toán và trả về số điểm của vaccine theo công thức đã nêu trên.
# 
# Học sinh chỉ nộp hàm calculate_score(trials)

def calculate_score(trials):
      sum = 0
      for number in trials:
          sum = sum + number
      return sum/len(trials)
      