# Câu chuyện:
# 
# Trẩu đã học và hoàn thành xong chương trình đánh giá vaccine.
# Thế nhưng việc tính trung bình cộng như thế vẫn chưa phải là phương pháp đánh giá tốt nhất.
# Ngoài điểm số của vaccine, vaccine đó phải đạt chuẩn 2 yêu cầu sau:
# 
# Vaccine phải trải qua ít nhất 3 lần thử nghiệm
# Trong các lần thử nghiệm của vaccine, không lần nào có điểm dưới 50.
# Nếu vaccine có điểm cao nhưng không đạt được 2 yêu cầu trên thì cũng không đạt yêu cầu.
# 
# Yêu cầu:
# 
# Chúng ta hãy giúp Trẩu cải tiến chương trình đánh giá vaccine bằng cách kiểm tra thêm 2 yêu cầu trên
# để loại bỏ những vaccine không đạt chuẩn trước khi tính điểm các vaccine nhé!
# 
# Điểm của những vaccine không đạt được 2 yêu cầu trên là 0.0 nhé!
# Trẩu sẽ được nhận dữ liệu vaccine là mảng data tương tự như đã học. Nhiệm vụ của Trẩu là in ra điểm của tất cả các vaccine.
# 
# Input:
# 
# [
# 
# [10, 62, 30, 65], 
# 
# [100, 100], 
# 
# [86, 85, 87]
# 
# ]
# Output:
# 
# [0.0, 0.0, 86]
# Giải thích:
# 
# Vaccine thứ nhất không đạt vì có 2 lần thử nghiệm mà điểm dưới 50. Điểm của vaccine này là 0.0.
# Vaccine thứ hai không đạt vì chỉ trải qua 2 lần thử nghiệm mặc dù điểm trung bình là 100. Điểm của vaccine này là 0.0.
# Vaccine thứ ba đạt yêu cầu nên output là điểm của vaccine này.

# Luu y: Hoc sinh khong khoi tao mang data.
result = []
result = [0.0]*len(data)
for row in range(len(data)):
    counter = 0
    lenght = len(data[row])
    if lenght >= 3:
        sum = 0
        for col in range(len(data[row])):
            if data[row][col] >= 50:
                counter = counter + 1
                sum = sum + data[row][col]
        if counter == len(data[row]):
            result[row] = sum / counter        
print(result)                             