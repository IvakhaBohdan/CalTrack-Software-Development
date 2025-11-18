import pygame
import sys
from models.user_goals import User

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CalTrack: Демонстрація Логіки")

# Створення тестового об'єкта User
test_user = User(
    name="Богдан", 
    age=25, 
    gender="Male", 
    height=178, 
    weight=80, 
    activityLevel="moderate", 
    goal="loss"
)
target_cal = test_user.daily_calories_target

# --- Візуалізація Результату ---
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255) 
background_color = (0, 50, 100)

text_line1 = f"Користувач: {test_user.name}"
text_line2 = f"Ціль: {test_user.goal.upper()} (Втрата ваги)"
text_line3 = f"Розрахована добова норма: {target_cal} ККАЛ"

render1 = font.render(text_line1, True, text_color)
render2 = font.render(text_line2, True, text_color)
render3 = font.render(text_line3, True, text_color)

# --- Головний Цикл Демонстрації ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(background_color)
    screen.blit(render1, (50, 50))
    screen.blit(render2, (50, 100))
    screen.blit(render3, (50, 200))
    pygame.display.flip()

pygame.quit()
sys.exit()