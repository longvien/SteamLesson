# CÂU HỎI BÀI TẬP
# 
# Sau khi đã làm quen với kiến thức về lớp, chúng mình hãy cùng áp dụng vào trò chơi đã được thầy Louis hướng dẫn ở trên lớp nhé.
# Trong game, ta thường thấy các nhân vật có khả năng di chuyển dựa vào phím lên, xuống, trái, phải mà người chơi nhấn.
# Ở đây, ta cũng muốn lập trình sao cho nhân vật của chúng ta phản ứng với các phím bấm trên, dưới, trái, phải như vậy.
# Bài bên dưới sẽ giúp chúng ta tách nhỏ và nhìn rõ hơn các bước để làm điều này.
# 
# Yêu cầu:
# 
# Định nghĩa lớp Player
# 
# Lớp Player có 3 thuộc tính (attribute) là name (tên), x và y.
# 
# Lớp Player có phương thức (method) là move (di chuyển) để thay đổi vị trí của nhân vật
# 
# Phương thức move nhận vào 2 tham số là hướng đi và đơn vị thay đổi.
# 
# Nếu hướng đi là “left", giảm toạ độ x của người chơi theo đơn vị thay đổi
# Nếu hướng đi là “right", tăng toạ độ x của người chơi theo đơn vị thay đổi
# Nếu hướng đi là “up", giảm toạ độ y của người chơi theo đơn vị thay đổi
# Nếu hướng đi là “down", tăng toạ độ y của người chơi theo đơn vị thay đổi

class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def move(self, direction, step):
        if direction == "up":
            self.y = self.y - step
        elif direction == "down":
            self.y = self.y + step
        elif direction == "right":
            self.x = self.x + step
        else:
            self.x = self.x - step
        
      class Player:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def move(self, direction, step):
        if direction == "up":
            self.y = self.y - step
        elif direction == "down":
            self.y = self.y + step
        elif direction == "right":
            self.x = self.x + step
        else:
            self.x = self.x - step
        
      