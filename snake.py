import pygame

vec2 = pygame.math.Vector2

class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.bbloc = pygame.rect.Rect([0, 0, game.TILE_SIZE, game.TILE_SIZE])
        self.bbloc.center = (130, 230) # starting point
        self.direction = vec2(20, 0)
        self.step_delay = 80 #ms
        self.time = 0
        self.length = 1
        self.segment = []
        self.directions = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and self.directions[pygame.K_UP]:
                self.direction = vec2(0, -self.size)
                self.directions = {pygame.K_UP: 1, pygame.K_DOWN: 0, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            if event.key == pygame.K_DOWN and self.directions[pygame.K_DOWN]:
                self.direction = vec2(0, self.size)
                self.directions = {pygame.K_UP: 0, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 1}
            if event.key == pygame.K_LEFT and self.directions[pygame.K_LEFT]:
                self.direction = vec2(-self.size, 0)
                self.directions = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 1, pygame.K_RIGHT: 0}
            if event.key == pygame.K_RIGHT and self.directions[pygame.K_RIGHT]:
                self.direction = vec2(self.size, 0)
                self.directions = {pygame.K_UP: 1, pygame.K_DOWN: 1, pygame.K_LEFT: 0, pygame.K_RIGHT: 1}


    def delta_time(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def check_food(self):
        if self.bbloc.center == self.game.food.bbloc.center: # if eat food
            self.game.food.bbloc.center = self.game.food.random_pos()
            self.length += 1
            self.game.score += 1

    def check_self_eating(self):
        if len(self.segment) != len(set(seg.center for seg in self.segment)):
            self.game.new_game()

    def check_border(self):
        if self.bbloc.left < 0 or self.bbloc.right > self.game.WIDTH or self.bbloc.top < 0 or self.bbloc.bottom > self.game.HEIGHT:
            self.game.new_game()

    def move(self):
        if self.delta_time():
            self.bbloc.move_ip(self.direction)
            self.segment.append(self.bbloc.copy())
            self.segment = self.segment[-self.length:] # we only keep the new ones so the snake moves normally

    def update(self):
        self.check_border()
        self.check_self_eating()
        self.check_food()
        self.move()

    def draw(self):
        [pygame.draw.rect(self.game.WINDOW, 'green', seg) for seg in self.segment]