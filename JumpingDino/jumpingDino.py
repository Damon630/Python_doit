import pygame
import sys

pygame.init()
pygame.display.set_caption('Jumping Dino')
MAX_WIDTH = 800
MAX_HEIGHT = 400

def main():
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    imgDino1 = pygame.image.load('dino1.png')
    imgDino2 = pygame.image.load('dino2.png')
    dino_height = imgDino1.get_size()[1]
    dino_bottom = MAX_HEIGHT - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 200
    leg_swap = True
    is_Bottom = True
    is_go_up = False

    imgTree = pygame.image.load('tree.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    while True:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if is_Bottom:
                    is_go_up = True
                    is_Bottom = False

        if is_go_up:
            dino_y -= 10.0
        elif not is_go_up and not is_Bottom:
            dino_y += 10.0

        if is_go_up and dino_y <= jump_top:
            is_go_up = False

        if not is_Bottom and dino_y >= dino_bottom:
            is_Bottom = True
            dino_y = dino_bottom

        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        screen.blit(imgTree, (tree_x, tree_y))

        if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino2, (dino_x, dino_y))
            leg_swap = True

        pygame.display.update()
        fps.tick(30)

if __name__ == '__main__':
    main()
