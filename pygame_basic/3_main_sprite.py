import pygame

pygame.init()  # 초기화(반드시 필요)

# 화면크기설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("NADO GAME")  # 게임 이름

# 배경이미지 불러오기
background = pygame.image.load(
    "C:/Users/simon/OneDrive/바탕 화면/CODING/Python_Game/background.png")

# 캐릭터 불러오기
character = pygame.image.load(
    "C:/Users/simon/OneDrive/바탕 화면/CODING/Python_Game/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - \
    (character_width/2)  # 화면 가로의 절반크기에 해당하는 곳애 위치
character_y_pos = screen_height - character_height  # 화면 세로크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프
running = True  # 게임이 진행중인가
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가
            running = False  # 게임 진행중이 아님

    screen.blit(background, (0, 0))  # 배경그리기

    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기

    pygame.display.update()  # 매번 업데아트로 게임화면 계속그리기


# pygame 종료
pygame.quit()