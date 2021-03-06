import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        """Initialize the alien and set it's starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings= ai_settings
        #Load the alien image and set it's rect attribute
        self.image = pygame.image.load('images/ship_Alien.png')
        self.rect = self.image.get_rect()
        #Start each new alien near the top left of the screen
        self.rect.x= self.rect.width
        self.rect.y= self.rect.height
        #Store the ailen's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        """Move the alien right"""
        self.x+=self.ai_settings.alien_speed_factor
        self.rect.x= self.x
