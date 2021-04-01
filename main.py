# MADE BY: Lisette Spalding
# PROJECT NAME: python__snake_game
# FILE NAME: main.py
# DATE CREATED: 04/01/2021
# DATE LAST MODIFIED: 04/01/2021
# PYTHON VER. USED: 3.9

########## IMPORTS ##########
import sys
import random as r
from PIL import Image, ImageTk
from tkinker import Tk, Frame, Canvas, ALL, NW
############ FIN ############

########## CLASSES ##########
class Constants:
        BOARD_WIDTH = 300
        BOARD_HEIGHT = 300
        DELAY = 100
        DOT_SIZE = 10
        MAX_RAND_POS = 27

class Board(Canvas):

    def __init__(self):
        ## Setting up game
        super().__init__(width = Constants.BOARD_WIDTH, height = Constants.BOARD_HEIGHT,
                         background = "black", highlightthinkness = 0)

        self.initGame() # Calling the game class

        self.pack() # Using "pack" for the window set-up

    def initGame(self):
        """ To use: self.initGame()
        This method initializes the Game """

        self.inGame = True # Stating that the game is running
        self.dots = 3 # Stating the number of dots
        self.score = 0 # Starting score

        ## The variables used to move the Snake Object:
        self.moveX = Constants.DOT_SIZE
        self.moveY = 0
        ## FIN

        ## Stating the apple coordinates:
        self.appleX = 100
        self.appleY = 190
        ## FIN

        self.loadImages() # Loading the images

        # Calling other classes
        self.createObjects()
        self.locateApple()
        self.bindAll("<Key>", self.onKeyPressed)
        self.after(Constants.DELAY, self.onTimer)

    def loadImages(self):
        """ To use: self.loadImages()
        This method loads the images. """

        try:
            self.idot = Image.open("dot.png")
            self.dot  = ImageTk.PhotoImage(self.idot)
            self.ihead = Image.open("head.png")
            self.head = ImageTk.PhotoImage(self.ihead)
            self.iapple = Image.open("apple.png")
            self.apple = ImageTk.PhotoImage(self.iapple)
        except IOError as e:
            print(e)
            sys.exit(1)

    def createObjects(self):
        """ To use: self.createObjects()
        This method creates objects on the canvas. """
        pass

############ FIN ############