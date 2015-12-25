import pygame, sys
from arduino import SerialData
#from pygame.locals import *

class ThereminUI:

    def __init__(self, width=320, height=200):
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        self.FPS = 25
        self.fpsClock = pygame.time.Clock()
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((width, height))
        self.serial = SerialData()

    def drawCharts(self):
        values = self.serial.next()
        if(values):
            sensor = float(values[0]) / 10
            pitch = float(values[1]) / 10
            pygame.draw.rect(self.DISPLAYSURF, self.BLACK, (30 + sensor, 30, 320-sensor, 50))
            pygame.draw.rect(self.DISPLAYSURF, self.BLACK, (30 + pitch, 120, 320-pitch, 50))
            pygame.draw.rect(self.DISPLAYSURF, self.GREEN, (30, 30, sensor, 50))
            pygame.draw.rect(self.DISPLAYSURF, self.BLUE, (30, 120, pitch, 50))

    def start(self):
        pygame.display.set_caption('Theremin-ui')

        fontObj = pygame.font.Font('freesansbold.ttf', 12)
        sensorText = fontObj.render('Sensor', True, self.WHITE, self.BLACK)
        sensorRect = sensorText.get_rect()
        sensorRect.center = (30, 10)
        pitchText = fontObj.render('Pitch', True, self.WHITE, self.BLACK)
        pitchRect = pitchText.get_rect()
        pitchRect.center = (30, 100)
        self.serial.start()
        while True: # main game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.serial.stop()
                    pygame.quit()
                    sys.exit()

            self.DISPLAYSURF.blit(sensorText, sensorRect)
            self.DISPLAYSURF.blit(pitchText, pitchRect)
            self.drawCharts()
            pygame.display.update()
            self.fpsClock.tick(self.FPS)

if __name__ == "__main__":
    ui = ThereminUI()
    ui.start()
