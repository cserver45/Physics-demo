"""A simple POC physics demo."""
import sys
import pygame
import pymunk


class GameState():

    def __init__(self):
        self.mode = "landing"

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                apples.append(create_apple(space, event.pos))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    apples.append(create_apple(space, pygame.mouse.get_pos()))
                elif event.key == pygame.K_o:
                    oranges.append(create_orange(space,
                                                 pygame.mouse.get_pos()))

        screen.fill((217, 217, 217))
        draw_apples(apples)
        draw_oranges(oranges)
        draw_static_ball(balls)
        print_fps()
        space.step(1 / 50)
        pygame.display.update()

    def landing(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mode = "main_game"

        screen.fill((217, 217, 217))
        print_fps()
        text_img = font.render("Apples", True, (0, 0, 0))
        atext_img = font.render("Click to play", True, (0, 0, 0))
        screen.blit(text_img, (400, 250))
        screen.blit(atext_img, (380, 280))
        screen.blit(apple_surface, (360, 110))
        space.step(1 / 50)
        pygame.display.update()

    def state_manager(self):
        if self.mode == "main_game":
            self.main_game()
        elif self.mode == "landing":
            self.landing()


def create_orange(space, pos):
    body = pymunk.Body(1, 85, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 60)
    space.add(body, shape)
    return shape


def create_apple(space, pos):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = pos
    shape = pymunk.Circle(body, 64)
    space.add(body, shape)
    return shape


def draw_oranges(oranges):
    for orange in oranges:

        pos_x = int(orange.body.position.x)
        pos_y = int(orange.body.position.y)
        orange_rect = orange_surface.get_rect(center=(pos_x, pos_y))

        screen.blit(orange_surface, orange_rect)


def draw_apples(apples):
    for apple in apples:

        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        apple_rect = apple_surface.get_rect(center=(pos_x, pos_y))

        screen.blit(apple_surface, apple_rect)


def static_ball(space, pos):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 40)
    space.add(body, shape)
    return shape


def draw_static_ball(balls):
    for ball in balls:

        pos_x = int(ball.body.position.x)

        pos_y = int(ball.body.position.y)

        pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), 40)


def print_fps():
    fps = clock.get_fps()
    fps_img = font.render(str(round(fps)), True, (0, 200, 0))
    pygame.draw.rect(screen, (0, 0, 0), (10, 10, 30, 20), 0)
    screen.blit(fps_img, (11, 11))


pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)
space = pymunk.Space()
game_mode = GameState()

space.gravity = (0, 350)
apple_surface = pygame.image.load("apple.png")
orange_surface = pygame.image.load("orange.png")

apples = []
balls = []
oranges = []
balls.append(static_ball(space, (450, 400)))
balls.append(static_ball(space, (220, 440)))
balls.append(static_ball(space, (390, 230)))

pygame.display.set_caption("Apple")

while True:
    game_mode.state_manager()
    clock.tick(120)
