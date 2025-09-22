import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Birthday 💖")

# Colors
BLACK = (0, 0, 0)
RED = (255, 50, 80)
WHITE = (255, 255, 255)

# Use default system font
font = pygame.font.SysFont(None, 32, bold=True)

# Birthday message
full_message = "I love you For ever & many many happy returns of the day"
message_progress = ""   # gradually built up
letter_index = 0
letter_delay = 5        # frames per letter
frame_counter = 0

# Generate target positions (big heart shape points)
target_positions = []
for t in [i * 0.05 for i in range(0, 630)]:  # smoother heart
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    target_positions.append((WIDTH//2 + int(x * 20), HEIGHT//2 - int(y * 20)))

# Small hearts starting from sides
hearts = []
for pos in target_positions:
    start_x = random.choice([-50, WIDTH + 50])  # left or right side
    start_y = random.randint(0, HEIGHT)
    hearts.append({"x": start_x, "y": start_y, "tx": pos[0], "ty": pos[1]})

# Function to draw a heart
def draw_heart(surface, x, y, size, color):
    points = []
    for t in [i * 0.1 for i in range(63)]:
        hx = size * 16 * math.sin(t) ** 3
        hy = -size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        points.append((x + hx, y + hy))
    pygame.draw.polygon(surface, color, points)

# Main loop
clock = pygame.time.Clock()
running = True
assembled = False
pulse_frame = 0  # for pulsing effect

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    assembled = True
    # Move hearts toward their target positions
    for h in hearts:
        dx = (h["tx"] - h["x"]) * 0.05
        dy = (h["ty"] - h["y"]) * 0.05
        h["x"] += dx
        h["y"] += dy
        if abs(dx) > 0.5 or abs(dy) > 0.5:
            assembled = False
        draw_heart(screen, h["x"], h["y"], 0.3, RED)

    # Once the big heart is assembled
    if assembled:
        # 💖 Pulse effect
        pulse_frame += 1
        pulse_size = 0.35 + 0.05 * math.sin(pulse_frame * 0.1)  # scale up & down
        for h in hearts[::15]:  # draw extra glowing hearts at some points
            draw_heart(screen, h["tx"], h["ty"], pulse_size, (255, 100, 150))

        # 💌 Reveal the birthday message
        frame_counter += 1
        if frame_counter >= letter_delay and letter_index < len(full_message):
            message_progress += full_message[letter_index]
            letter_index += 1
            frame_counter = 0

        text = font.render(message_progress, True, WHITE)
        rect = text.get_rect(center=(WIDTH//2, HEIGHT - 50))
        screen.blit(text, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
