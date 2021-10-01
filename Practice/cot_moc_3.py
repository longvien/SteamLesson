import pygame

pygame.init()
WIDTH = 500   # Chiều ngang (W: Width)
HEIGHT = 500  # Chiều dọc   (H: Height)
BLACK = (0, 0, 0)  # Màu Đen
screen = pygame.display.set_mode([WIDTH, HEIGHT])

class Door:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Kích thước cửa (door) 60 x 60 px
        sprite = pygame.image.load("sprites/door.png")
        self.image = pygame.transform.scale(sprite, (80, 80))

class Robot:
    def __init__(self, x, y, x_heading, y_heading, hinh_anh):
        self.x = x
        self.y = y
        self.x_heading = x_heading
        self.y_heading = y_heading
        # Kích thước Robot 60 x 60 px
        sprite = pygame.image.load(hinh_anh)
        self.image = pygame.transform.scale(sprite, (60, 60))

    def move(self):
        self.x = self.x + self.x_heading
        self.y = self.y + self.y_heading
        
        if self.x > 440: self.x_heading = - self.x_heading
        if self.x < 0:   self.x_heading = - self.x_heading
        if self.y > 440: self.y_heading = - self.y_heading
        if self.y < 0:   self.y_heading = - self.y_heading

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # Kích thước trẩu (player) 50 x 80 px
        sprite = pygame.image.load("sprites/trau.png")
        self.image = pygame.transform.scale(sprite, (50, 80))
    
    def move(self, change_x, change_y):
        new_x = self.x + change_x
        new_y = self.y + change_y

        if new_x > 0 and new_x < 450:
            self.x = new_x
        if new_y > 0 and new_y < 420:
            self.y = new_y

# Khởi tạo đối tượng Trẩu + Cửa (Door) + Robot
trau = Player(100, 250)
door = Door(375, 20)
robots = [
    Robot(100, 400, 5, 0, "sprites/robot1.png"),
    Robot(300, 300, 0, 5, "sprites/robot2.png"),
    Robot(200, 200, 10, 2, "sprites/robot3.png"),
    Robot(100, 100, -2, -5, "sprites/robot4.png")
]

#---------------------------------------------------------
# Bắt đầu game
running = True
while running:
    # Tạo hình nền
    screen.fill(BLACK)
    background = pygame.image.load("sprites/background.png").convert_alpha()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(background, (0, 0))

    # Người chơi có tắt màn hình game chưa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #----------------------------------------
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:    trau.move( 0, -5)
    if pressed[pygame.K_DOWN]:  trau.move( 0,  5)
    if pressed[pygame.K_LEFT]:  trau.move(-5,  0)
    if pressed[pygame.K_RIGHT]: trau.move( 5,  0)

    for robot in robots:
        robot.move()

    # Hiển thị vị trí của các đối tượng
    screen.blit(door.image, (door.x, door.y))
    screen.blit(trau.image, (trau.x, trau.y))
    for robot in robots:
        screen.blit(robot.image, (robot.x, robot.y))

    pygame.display.flip()

# Ket thuc game
pygame.quit()
