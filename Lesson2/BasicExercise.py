# YÊU CẦU BÀI TẬP
# a. Câu chuyện
# Bạn Trẩu sau khi bước vào siêu máy tính đã tìm ra chữ số bí mật. Để giúp bạn Trẩu tìm ra số bí mật, các lập trình viên nhí đã viết một chương trình Python nhằm hỗ trợ bạn Trẩu.
# b. Giới thiệu chương trình
# Máy tính sẽ tạo ra một số ngẫu nhiên từ từ 0 đến 10. Người chơi phải đoán được số ngẫu nhiên đó. Qua 3 lượt đoán số, người chơi phải trả lời đáp án cuối cùng, nếu đúng người chơi giành chiến thắng, nếu sai người chơi thua cuộc.
# c. Yêu cầu
# - Chương trình nghĩ ra một số bất kỳ từ 0 đến 10 (đoạn này đã được viết sẵn cho học sinh). Chương trình sau đó cho phép người chơi đoán tối đa 3 lần.
# - Nếu người chơi đoán đúng, chương trình in ra “Dung roi!” và thoát. (Chữ D viết hoa)
# - Nếu người chơi đoán số thấp hơn số chương trình nghĩ ra, thì chương trình in ra “Thap qua!" (chữ T viết hoa)
# - Nếu người chơi đoán số cao hơn số chương trình nghĩ ra, thì chương trình in ra “Cao qua!" (chữ C viết hoa)
# - Nếu người chơi chưa đoán đúng và vẫn còn lượt đoán, thì cho phép người chơi đoán tiếp.
# 
# d. Lưu ý
# 
# Dùng đoạn code sau để tạo ra số ngẫu nhiên
# 
# # Them thu vien de tao so ngau nhien
# import random
#         
# # answer la so ngau nhien tu 0 den 10 duoc may tinh tu dong sinh ra
# answer = random.randint(0, 10)  # lenh randint(0, 10) tra ve mot so tu 0 den 10
# print("To dang nghi den 1 so nguyen nam trong khoang 0 den 10.")
# Ví dụ 1: người chơi thắng cuộc ở lượt đoán thứ 2
# 
# To dang nghi den 1 so nguyen nam trong khoang 0 den 10.
# Do ban biet to dang nghi den so nao? 5
# Cao qua!
# Do ban biet to dang nghi den so nao? 3
# Dung roi!
# Ví dụ 2: người chơi thua cuộc vì đã hết 3 lượt chơi
# 
# To dang nghi den 1 so nguyen nam trong khoang 0 den 10.
# Do ban biet to dang nghi den so nao? 7
# Cao qua!
# Do ban biet to dang nghi den so nao? 5
# Cao qua!
# Do ban biet to dang nghi den so nao? 4
# Cao qua!

# Them thu vien de tao so ngau nhien
import random
        
# answer la so ngau nhien tu 0 den 10 duoc may tinh tu dong sinh ra
answer = random.randint(0, 10)  # lenh randint(0, 10) tra ve mot so tu 0 den 10
print("To dang nghi den 1 so nguyen nam trong khoang 0 den 10.")

# Hoc sinh lap trinh tu dong nay tro xuong
counter = 0
while counter < 3:
    counter = counter + 1
    number = int(input("Do ban biet to dang nghi den so nao? "))
    if number  < answer:
        print("Thap qua!")
    else:
        if number > answer:
            print("Cao qua!")
        else:
            print("Dung roi!")
            break