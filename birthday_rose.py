import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🌹 Happy Birthday 🌹")

# Colors
BG = (10, 10, 20)
PETAL = (220, 30, 70)
LEAF = (50, 180, 80)
TEXT = (255, 245, 245)

# Font
font = pygame.font.SysFont("Segoe Script", 42, bold=True)

# Message
full_message = "Happy Birthday To You"
typed_message = ""
msg_index, frame_counter = 0, 0
letter_delay = 5

# --- Create rose spiral pattern (polar rose curve) ---
target_positions = []
a = 180   # scale
k = 7     # number of petals (higher = fuller rose)
for theta in [i * 0.02 for i in range(0, 2000)]:
    r = a * math.sin(k * theta)
    x = int(r * math.cos(theta)) + WIDTH // 2
    y = int(r * math.sin(theta)) + HEIGHT // 2 - 60
    target_positions.append((x, y))

# Add leaves around bottom
for i in range(-100, 100, 10):
    target_positions.append((WIDTH//2 + i*2, HEIGHT//2 + 200 + abs(i)//2))

# Small hearts start from all sides
hearts = []
for tx, ty in target_positions:
    side = random.choice(["left", "right", "top", "bottom"])
    if side == "left":
        sx, sy = -80, random.randint(0, HEIGHT)
    elif side == "right":
        sx, sy = WIDTH + 80, random.randint(0, HEIGHT)
    elif side == "top":
        sx, sy = random.randint(0, WIDTH), -80
    else:
        sx, sy = random.randint(0, WIDTH), HEIGHT + 80
    hearts.append({
        "x": sx, "y": sy,
        "tx": tx, "ty": ty,
        "speed": random.uniform(0.03, 0.08),
        "size": random.uniform(0.25, 0.45),
        "color": PETAL if ty < HEIGHT//2 + 150 else LEAF,
        "arrived": False
    })

# Draw heart shape
def draw_heart(surface, x, y, size, color):
    points = []
    for t in [i * 0.1 for i in range(63)]:
        hx = size * 16 * math.sin(t)**3
        hy = -size * (13*math.cos(t) - 5*math.cos(2*t)
                      - 2*math.cos(3*t) - math.cos(4*t))
        points.append((x + hx, y + hy))
    pygame.draw.polygon(surface, color, points)

# Main loop
clock = pygame.time.Clock()
assembled, pulse_frame = False, 0

while True:
    screen.fill(BG)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    assembled = True
    for h in hearts:
        dx = (h["tx"] - h["x"]) * h["speed"]
        dy = (h["ty"] - h["y"]) * h["speed"]
        h["x"] += dx
        h["y"] += dy
        if abs(dx) > 0.7 or abs(dy) > 0.7:
            assembled = False
        draw_heart(screen, h["x"], h["y"], h["size"], h["color"])

    # Once rose is formed
    if assembled:
        pulse_frame += 1
        scale = 0.5 + 0.1 * math.sin(pulse_frame * 0.15)
        for (tx, ty) in target_positions[::40]:  # glowing petals
            draw_heart(screen, tx, ty, scale, (255, 120, 150))

        frame_counter += 1
        if frame_counter >= letter_delay and msg_index < len(full_message):
            typed_message += full_message[msg_index]
            msg_index += 1
            frame_counter = 0

        text = font.render(typed_message, True, TEXT)
        rect = text.get_rect(center=(WIDTH//2, HEIGHT - 80))
        screen.blit(text, rect)

    pygame.display.flip()
    clock.tick(60)
