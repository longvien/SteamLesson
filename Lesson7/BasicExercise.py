# CÂU HỎI BÀI TẬP
# 
# Trẩu và Tre đang sắp xếp chồng sách vào kệ sách.
# Tre đang cầm trên tay một chồng sách.
# Mỗi thao tác của Tre sẽ là xếp một quyển sách vào kệ (pop) hoặc
# thêm một quyển sách từ Trẩu vào chồng sách mà Tre đang cầm (push).
# 
# Yêu cầu:
# 
# Viết hàm update_stack để tự động hoá công việc của Tre.
# 
# Hàm update_stack nhận vào một stack bao gồm tên các quyển sách Tre đang cầm
# và một danh sách các hành động actions được lưu dưới dạng từ điển.
# 
# Từ điển có hai khoá là action và book.
# Khoá action là một mảng gồm các thao tác của Tre (push hoặc pop).
# Khoá book là một mảng gồm tên các quyển sách thêm vào chồng sách của Tre
# tương ứng với thao tác push hoặc giá trị None tương ứng với thao tác pop.
# Thao tác nào xuất hiện trong mảng trước sẽ được thực hiện trước.
# 
# Hàm update_stack trả về stack đã thay đổi sau khi thực hiện hết các hành động trong danh sách đã cho.

def update_stack(stack, actions):
    # hoc sinh thay doi stack voi cac hanh dong trong danh sach actions
    # tra ve stack
    ans = stack
    action = actions["action"]
    books = actions["book"]
    for index in range(0,len(books)):
        if action[index] == "pop":
            new_stack = []
            if not stack:
                return new_stack
            for i in range(0,len(stack)-1):
                new_stack.append(stack[i])
            stack = new_stack
        elif action[index] == "push":
            stack.append(books[index])
           
        
    return stack
          