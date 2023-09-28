import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize clock
CLOCK = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH//2, HEIGHT//2)]
        self.direction = (1, 0)
        self.score = 0

    def move(self):
        head = self.body[-1]
        new_head = (head[0] + self.direction[0]*10, head[1] + self.direction[1]*10)
        self.body.append(new_head)
        if len(self.body) > self.score + 1:
            del self.body[0]

    def grow(self):
        self.score += 1

    def check_collision(self):
        head = self.body[-1]
        return head in self.body[:-1] or head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT

# Food class
class Food:
    def __init__(self):
        self.position = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))

    def spawn_food(self):
        self.position = (random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10))

    def get_position(self):
        return self.position

# Draw function
def draw_objects(snake, food):
    WINDOW.fill(WHITE)
    for segment in snake.body:
        pygame.draw.rect(WINDOW, GREEN, (segment[0], segment[1], 10, 10))
    pygame.draw.rect(WINDOW, RED, (food.position[0], food.position[1], 10, 10))
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(snake.score), True, (0, 0, 0))
    WINDOW.blit(score_text, (10, 10))

# Main function
def main():
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN:
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT:
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.direction = (1, 0)

        snake.move()

        if snake.body[-1] == food.get_position():
            snake.grow()
            food.spawn_food()

        if snake.check_collision():
            print("Excellent Game Over. Your score was:", snake.score)
            pygame.quit()
            quit()

        draw_objects(snake, food)
        pygame.display.update()
        CLOCK.tick(10)

if __name__ == "__main__":
    main()
