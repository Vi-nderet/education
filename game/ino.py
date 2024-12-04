import pygame



class Ino(pygame.sprite.Sprite):
    """ класс одного пришельца"""

    def __init__(self, screen):
        """ инициализируем и задаем начальную позицию """
        super(Ino, self).__init__()

