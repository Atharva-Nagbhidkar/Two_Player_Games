import pygame

# Constants
WIDTH, HEIGHT = 800, 600
BROWN = (50,109,160)
WHITE = (255,255,255)
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
PADDLE_SPEED = 5
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR HOCKEY")

# Initialize paddles and ball positions
player1_x, player1_y = 10, (HEIGHT - PADDLE_HEIGHT) // 2
player2_x, player2_y = WIDTH - PADDLE_WIDTH - 10, (HEIGHT - PADDLE_HEIGHT) // 2
ball_x, ball_y = (WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2

# Game variables
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)
winner = None

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 50:
        player1_y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_y < HEIGHT - PADDLE_HEIGHT - 50:
        player1_y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_y > 50:
        player2_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_y < HEIGHT - PADDLE_HEIGHT - 50:
        player2_y += PADDLE_SPEED

    # Update ball position
    ball_x += BALL_SPEED_X
    ball_y += BALL_SPEED_Y

    # Ball collisions
    if ball_y <= 50 or ball_y >= HEIGHT - BALL_SIZE -50:
        BALL_SPEED_Y *= -1
    if (
        ball_x <= player1_x + PADDLE_WIDTH
        and player1_y <= ball_y <= player1_y + PADDLE_HEIGHT
    ) or (
        ball_x >= player2_x - BALL_SIZE
        and player2_y <= ball_y <= player2_y + PADDLE_HEIGHT
    ):
        BALL_SPEED_X *= -1

    # Scoring
    if ball_x <= 0:
        player2_score += 1
        ball_x, ball_y = (WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2
        BALL_SPEED_X *= -1
    elif ball_x >= WIDTH:
        player1_score += 1
        ball_x, ball_y = (WIDTH - BALL_SIZE) // 2, (HEIGHT - BALL_SIZE) // 2
        BALL_SPEED_X *= -1

    # Clear the screen
    screen.fill(BROWN)

    # Draw the white vertical line through the center
    pygame.draw.rect(screen,WHITE, (0,48,2,HEIGHT-96))
    pygame.draw.rect(screen,WHITE, (WIDTH-2,48,2,HEIGHT-96))
    pygame.draw.rect(screen,WHITE, (0,HEIGHT-48,WIDTH,2))
    pygame.draw.rect(screen,WHITE, (0,48,WIDTH,2))
    pygame.draw.circle(screen,WHITE , (WIDTH // 2, (HEIGHT) // 2), 70)
    pygame.draw.circle(screen,BROWN , (WIDTH // 2, (HEIGHT) // 2), 68)
    pygame.draw.rect(screen, WHITE, (WIDTH // 2, 50, 2, HEIGHT-100))

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (player1_x, player1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (player2_x, player2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    # Display scores
    text = font.render(f"{player1_score}   -   {player2_score}", True, WHITE)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, 10))
    font1 = pygame.font.Font(None,30)
    text1 = font1.render("PLAYER - 1",True,WHITE)
    screen.blit(text1,((WIDTH - text1.get_width()) // 5,10))
    font2 = pygame.font.Font(None,30)
    text2 = font2.render("PLAYER - 2",True,WHITE)
    screen.blit(text2,((WIDTH -(WIDTH - text2.get_width()) // 3),10))

    # Check for game over
    if player1_score >= 5 or player2_score >= 5:
        if player1_score > player2_score:
            winner = "Player 1"
        else:
            winner = "Player 2"
        running = False

    # Update the display
    pygame.display.update()

    clock.tick(60)

# Display winner
if winner:
    text = font.render(f"{winner} wins! ({player1_score} - {player2_score})", True, WHITE)
    screen.fill(BROWN)
    screen.blit(text, ((WIDTH - text.get_width()) // 2, HEIGHT // 2 - text.get_height()))
    pygame.display.update()
    pygame.time.wait(3000)  # Display winner
