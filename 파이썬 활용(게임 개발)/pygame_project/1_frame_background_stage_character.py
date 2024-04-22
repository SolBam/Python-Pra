# 조건 1: 캐릭터는 화면 아래에 위치, 좌우로만 이동 가능
# 조건 2: 스페이스를 누르면 무기를 쏘아 올림
# 조건 3: 큰 공 1개가 나타나서 바운스
# 조건 4: 무기에 닿으면 공은 작은 크기 2개로 분할, 가장 작은 크기의 공은 사라짐
# 조건 5: 모든 공을 없애면 게임 종료(성공)
# 조건 6: 캐릭터는 공에 닿으면 게임 종료(실패)
# 조건 7: 시간 제한 99초 초과 시 게임 종료(실패)
# 조건 8: FPS는 30으로 고정(필요시 speed 값을 조정)

import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Nado Pang")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴도 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

running = True
while running:
    dt = clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    pygame.dispaly.update()

pygame.quit()