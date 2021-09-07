# YÊU CẦU BÀI TẬP
# a. Câu chuyện:
# Sau khi vượt qua được thử thách đoán số, bạn Trẩu và bạn Tre tiếp tục tiến sâu hơn vào siêu máy tính. Trên đường đi, bạn Tre nhờ bạn Trẩu hướng dẫn cách chơi oẳn tù tì. Bạn Tre đã nhờ các lập trình viên nhí viết ra một chương trình oẳn tù tì bằng Python và cài đặt cho bạn Tre để cùng chơi với bạn Trẩu.
# b. Oẳn tù tì:
# Trò chơi oẳn tù tì là trò chơi dân gian bao gồm hai người chơi. Có 3 loại đạo cụ: kéo, búa, bao. Trong đó, kéo thắng bao, bao thắng búa, và búa thắng kéo.
# c. Yêu cầu
# Trong chương trình này người lập trình viên được yêu cầu viết một chương trình oẳn tù tì:
# 1. Người chơi có thể trả lời bằng cách nhập vào bàn phím “keo”, “bua", “bao"
# 2. Chương trình lấy thông tin người chơi và in ra màn hình lượt đi của máy tính
# 3. Nếu người chơi chiến thắng, in ra màn hình ‘Ban da thang!'
# 4. Nếu người chơi thua, in ra màn hình ‘Ban da thua!
# 5. Nếu hoà, in ra màn hình ‘Hoa roi!’
# 
# Ví dụ 1:  Người chơi dành chiến thắng
# 
# Chung minh cung choi oan tu ti nhe!
# Ban ra gi? keo
# May tinh ra bao
# Ban da thang!
# Ví dụ 2: Người chơi hòa với máy tính
# 
# Chung minh cung choi oan tu ti nhe!
# Ban ra gi? bao
# May tinh ra bao
# Hoa roi!
# Ví dụ 3: Người chơi thua máy tính
# 
# Chung minh cung choi oan tu ti nhe!
# Ban ra gi? bua
# May tinh ra bao
# Ban da thua!

# Them thu vien de tao so ngau nhien
import random
 
print("Chung minh cung choi oan tu ti nhe!")
 
# lenh nay cho ta 1 trong 3 so 0, 1, 2 mot cach ngau nhien
random_number = random.randint(0, 2)
if random_number == 0:
    computer_choice = "keo"
elif random_number == 1:
    computer_choice = "bua"
else:
    computer_choice = "bao"

# Goi y:
# so sanh du lieu nguoi dung nhap vao voi bien computer_choice:  
# trong nhung truong hop nao thi may tinh va nguoi choi hoa nhau?
# trong nhung truong hop nao thi nguoi choi thang?
# trong nhung truong hop nao thi may tinh thang?

# Hoc sinh lap trinh tu dong nay tro xuong
vukhi = input("Ban ra gi? ")
print("May tinh ra "+ computer_choice)
if vukhi == "bua" and computer_choice == "bua":
    print("Hoa roi!")
elif vukhi == "bua" and computer_choice == "bao":
    print("Ban da thua!")
elif vukhi == "bua" and computer_choice == "keo":
    print("Ban da thang!")
elif vukhi == "bao" and computer_choice == "keo":
    print("Ban da thua!")
elif vukhi == "bao" and computer_choice == "bua":
    print("Ban da thang!")
elif vukhi == "bao" and computer_choice == "bao":
    print("Hoa roi!")
elif vukhi == "keo" and computer_choice == "bao":
    print("Ban da thang!")
elif vukhi == "keo" and computer_choice == "bua":
    print("Ban da thua!")
elif vukhi == "keo" and computer_choice == "keo":
    print("Hoa roi!")

