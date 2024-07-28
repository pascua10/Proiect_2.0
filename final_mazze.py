import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 20
player_color = GREEN
player_pos = [50, 50]
player_speed = 5

# Endpoint settings (placed within the maze)
end_pos = [360, 280]  # Placed in the middle of the maze
end_size = 40

# Maze layout (1 = wall, 0 = path)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Wall settings
wall_size = 40

# Function to draw the maze
def draw_maze():
    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == 1:
                pygame.draw.rect(screen, BLACK, [col_idx * wall_size, row_idx * wall_size, wall_size, wall_size])
            else:
                pygame.draw.rect(screen, BLUE, [col_idx * wall_size, row_idx * wall_size, wall_size, wall_size], 1)

# Function to move the player towards a target position
def move_player_towards(target_pos):
    dx = target_pos[0] - player_pos[0]
    dy = target_pos[1] - player_pos[1]

    if abs(dx) > abs(dy):
        step = player_speed if dx > 0 else -player_speed
        new_pos = [player_pos[0] + step, player_pos[1]]
    else:
        step = player_speed if dy > 0 else -player_speed
        new_pos = [player_pos[0], player_pos[1] + step]

    if not check_collision(new_pos):
        player_pos[0] = new_pos[0]
        player_pos[1] = new_pos[1]

# Function to check for collisions
def check_collision(pos):
    x, y = pos
    row = y // wall_size
    col = x // wall_size
    if maze[row][col] == 1:
        return True
    return False

# Function to check if the player has reached the end
def check_end_reached():
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    end_rect = pygame.Rect(end_pos[0], end_pos[1], end_size, end_size)
    return player_rect.colliderect(end_rect)

# Function to generate a colorful endpoint
def get_colorful_color(frame_count):
    return (
        (frame_count * 5) % 256,
        (frame_count * 7) % 256,
        (frame_count * 11) % 256
    )

# Game loop
running = True
clock = pygame.time.Clock()
target_pos = None
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            target_pos = pygame.mouse.get_pos()

    if target_pos:
        move_player_towards(target_pos)

    screen.fill(WHITE)
    draw_maze()

    # Draw the colorful endpoint
    end_color = get_colorful_color(frame_count)
    pygame.draw.rect(screen, end_color, [end_pos[0], end_pos[1], end_size, end_size])

    # Draw the player
    pygame.draw.rect(screen, player_color, [player_pos[0], player_pos[1], player_size, player_size])

    # Check if the player has reached the end
    if check_end_reached():
        font = pygame.font.SysFont(None, 55)
        text = font.render('You Win!', True, RED)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(30)
    frame_count += 1

pygame.quit()
sys.exit()





