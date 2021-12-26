import pygame
from plane_sprites import *


class PlaneGame:

    def __init__(self):
        # create window
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # create clock
        self.clock = pygame.time.Clock()
        # create sprite
        self.__create_sprite()

    def __create_sprite(self):
        bg1 = Background("./images/background.png")
        bg2 = Background("./images/background.png")
        bg2.rect.y = -bg2.rect.height

        self.back_group = pygame.sprite.Group(bg1, bg2)

    def start_game(self):
        while True:
            # set rate
            self.clock.tick(FPS)

            # event handler
            self.__event_handler()

            # collision detection
            self.__check_collide()

            # update sprite
            self.__update_sprites()

            # update screen
            pygame.display.update()


    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update();
        self.back_group.draw(self.screen)
        pass

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()


if __name__ == '__main__':
    # create game object
    game = PlaneGame()

    game.start_game()
