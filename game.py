import sys
import pygame
from snake import Snake
from food import Food

# ==========|| GLOBAL VARIABLES ||==========
FPS = 60


# COLOURS
BLACK = (0, 0, 0)
WHITE = (255, 255)
RED = (255, 0, 0)  # food colour
GREY = (96, 96, 96)  # background colour
GREEN = (0, 204, 102)  # snake body colour
GREEN2 = (0, 51, 25)  # snake head colour

# DIRECTIONS
UP = 1
RIGHT = 2
LEFT = 3
DOWN = 4



class Game:
    def __init__(self):
        pygame.init()
        font = pygame.font.Font(None, 25)
        self.WIDTH, self.HEIGHT = 640, 480  # 640, 480
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Douda Game")
        self.clock = pygame.time.Clock()
        self.BG_COLOR = GREY
        self.TILE_SIZE = 20
        self.new_game()
        self.score = 0
        # text = font.render("Score: " + str(self.score), True, WHITE)
        # self.display.blit(text, [0, 0])


    def draw_grid(self):
        [pygame.draw.line(self.WINDOW, [20]*3, (x,0), (x, self.HEIGHT)) for x in range(0, self.WIDTH, self.TILE_SIZE)] #vertical
        [pygame.draw.line(self.WINDOW, [20]*3, (0,y), (self.WIDTH, y)) for y in range(0, self.HEIGHT, self.TILE_SIZE)] #horizontal

    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.snake.update()
        pygame.display.update()
        self.clock.tick(FPS)

    def draw(self):
        self.WINDOW.fill(self.BG_COLOR)
        # self.WINDOW.blit("Score:", (20, 20)) #################
        # self.draw_grid()
        self.snake.draw()
        self.food.draw()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # snake control
            self.snake.control(event)

    def launch(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == "__main__": # So it doesn't get executed when we import this file as a module
    game = Game()
    game.launch()