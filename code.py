import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window
WIDTH, HEIGHT = 700, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 150, 255)

# Fonts
font = pygame.font.SysFont("comicsans", 40)

# Game clock
clock = pygame.time.Clock()
FPS = 50

# Bird
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
flap_strength = -8

# Pipes
pipe_width = 70
pipe_gap = 150
pipe_speed = 3
pipes = []

# Score
score = 0

# Game states
game_over = False

def reset_game():
    global bird_y, bird_velocity, pipes, score, game_over
    bird_y = HEIGHT // 2
    bird_velocity = 0
    pipes = []
    score = 0
    game_over = False

def create_pipe():
    """Create a new pipe pair with a random gap position."""
    y_top = random.randint(100, HEIGHT - 200)
    top_rect = pygame.Rect(WIDTH, 0, pipe_width, y_top)
    bottom_rect = pygame.Rect(WIDTH, y_top + pipe_gap, pipe_width, HEIGHT)
    pipes.append((top_rect, bottom_rect))

def draw_window():
    win.fill(BLUE)
    
    # Draw pipes
    for top, bottom in pipes:
        pygame.draw.rect(win, GREEN, top)
        pygame.draw.rect(win, GREEN, bottom)
    
    # Draw bird
    pygame.draw.circle(win, WHITE, (bird_x, int(bird_y)), bird_radius)
    
    # Draw score
    text = font.render(f"Score: {score}", True, WHITE)
    win.blit(text, (10, 10))
    
    # Draw game over message
    if game_over:
        over_text = font.render("Game Over!", True, WHITE)
        restart_text = pygame.font.SysFont("comicsans", 25).render("Press SPACE to restart", True, WHITE)
        win.blit(over_text, (WIDTH//2 - over_text.get_width()//2, HEIGHT//2 - 40))
        win.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2))
    
    pygame.display.update()

# Main loop
pipe_timer = 0
running = True
while running:
    clock.tick(FPS)
    
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    reset_game()
                else:
                    bird_velocity = flap_strength
    
    if not game_over:
        # Bird physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # Pipe generation
        pipe_timer += 1
        if pipe_timer > 90:
            create_pipe()
            pipe_timer = 0

        # Move pipes and check collisions
        new_pipes = []
        for top, bottom in pipes:
            top.x -= pipe_speed
            bottom.x -= pipe_speed

            # Check collision
            if top.collidepoint(bird_x, bird_y) or bottom.collidepoint(bird_x, bird_y):
                game_over = True

            # Update score
            if top.x + pipe_width == bird_x:
                score += 1

            if top.x + pipe_width > 0:
                new_pipes.append((top, bottom))
        pipes = new_pipes

        # Check floor/ceiling
        if bird_y - bird_radius <= 0 or bird_y + bird_radius >= HEIGHT:
            game_over = True

    # Draw everything
    draw_window()
