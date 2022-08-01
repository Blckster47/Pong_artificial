import pygame

pygame.init()

WIDTH, HEIGHT =700, 500
FPS=60
WIN = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.display.set_caption("PingPong")


class Paddle:
    COLOR = WHITE

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw_paddle(self, win):
        pygame.draw.rectangle()


def draw(win):
    win.fill(BLACK)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        draw(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == '__main__':
    main()