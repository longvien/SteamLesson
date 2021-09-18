# Câu chuyện:
# 
# Cho một mảng lưu thông tin các trợ giảng của STEAM for Vietnam.
# Mỗi phần tử của mảng có định dạng như sau: "ID,Name,City",
# với ID là số thứ tự của trợ giảng (có định dạng integer),
# Name là tên trợ giảng (có định dạng string), và City là tên thành phố hiện tại đang làm việc (có định dạng string)
# 
# Yêu cầu:
# 
# Viết hàm filter(array) nhận vào array và trả về một mảng mới lưu thông tin toàn bộ trợ giảng đến từ Hanoi
# 
# Mảng trả về phải đúng trình tự xuất hiện của các trợ giảng trong array nhận được.

def filter(array):
    ans = []
    for index in array:
        staff = index.split(",") 
        if staff[2] == "Hanoi":
            ans.append(index)
    return ans       
            