# MADE BY: Lisette Spalding
# PROJECT NAME: python__snake_game
# FILE NAME: main.py
# DATE CREATED: 03/01/2021
# DATE LAST MODIFIED: 04/18/2021
# PYTHON VER. USED: 3.9

########## IMPORTS ##########
import sys
import random as r
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW
############ FIN ############

########## CLASSES ##########
class Constants():
    """ To Use: Constants()
    This class defines all the constants that will be used throughout this program. """
    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27

class Board(Canvas):

    def __init__(self):
        ## Setting up game
        super().__init__(width = Constants.BOARD_WIDTH, height = Constants.BOARD_HEIGHT,
                         background = "black", highlightthickness = 0)

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
        self.bind_all("<Key>", self.onKeyPressed)
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

        self.create_text(30, 10, text = "Score: {0}".format(self.score),
                         tag = "score", fill = "white")
        self.create_image(self.appleX, self.appleY, image = self.apple,
                          anchor = NW, tag = "apple")
        self.create_image(50, 50, image = self.head, anchor = NW, tag = "head")
        self.create_image(30, 50, image = self.dot, anchor = NW, tag = "dot")
        self.create_image(40, 50, image = self.dot, anchor = NW, tag = "dot")

    def checkAppleCollision(self):
        """ To use: self.checkAppleCollision()
        This method checks if the head of the snake collides with the apple. """

        apple = self.find_withtag("apple")
        head = self.find_withtag("head")

        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for over in overlap:
            if apple[0] == over:
                self.score += 1
                x, y = self.coords(apple)
                self.create_image(x, y, image = self.dot, anchor = NW, tag = "dot")
                self.locateApple()

    def moveSnake(self):
        """ To use: self.moveSnake()
        This method moves the player (Snake). """

        dots = self.find_withtag("dot")
        head = self.find_withtag("head")

        items = dots + head

        z = 0
        while z < len(items)-1:
            c1 = self.coords(items[z])
            c2 = self.coords(items[z+1])
            self.move(items[z], c2[0] - c1[0], c2[1] - c1[1])
            z += 1

        self.move(head, self.moveX, self.moveY)

    def checkCollisions(self):
        """ To use: self.checkCollisions()
        This method checks for collisions. """

        dots = self.find_withtag("dot")
        head = self.find_withtag("head")

        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)

        for dot in dots:
            for over in overlap:
                if over == dot:
                    self.inGame = False

        if x1 < 0:
            self.inGame = False

        if x1 > Constants.BOARD_WIDTH - Constants.DOT_SIZE:
            self.inGame = False

        if y1 > 0:
            self.inGame = False

        if y1 > Constants.BOARD_HEIGHT - Constants.DOT_SIZE:
            self.inGame = False

    def locateApple(self):
        """ To use: self.locateApple()
        This method places the Apple object on the Canvas. """

        apple = self.find_withtag("apple")
        self.delete(apple[0])

        rand = r.randint(0, Constants.MAX_RAND_POS)
        self.appleX = rand * Constants.DOT_SIZE

        rand = r.randint(0, Constants.MAX_RAND_POS)
        self.appleY = rand * Constants.DOT_SIZE

        self.create_image(self.appleX, self.appleY, anchor = NW,
                          image = self.apple, tag = "apple")

    def onKeyPressed(self, e):
        """ To use: self.onKeyPressed(e)
        This method controls the direction variables with cursor keys. """

        key = e.keysym

        LEFT_CURSOR_KEY = "Left"
        if key == LEFT_CURSOR_KEY and self.moveX <= 0:
            self.moveX = -Constants.DOT_SIZE
            self.moveY = 0

        RIGHT_CURSOR_KEY = "Right"
        if key == RIGHT_CURSOR_KEY and self.moveX >= 0:
            self.moveX = 0
            self.moveY = 0

        RIGHT_CURSOR_KEY = "Up"
        if key == RIGHT_CURSOR_KEY and self.moveY <= 0:
            self.moveX = 0
            self.moveY = -Constants.DOT_SIZE

        DOWN_CURSOR_KEY = "Down"
        if key == DOWN_CURSOR_KEY and self.moveY >= 0:
            self.moveX = 0
            self.moveY = Constants.DOT_SIZE

    def onTimer(self):
        """ To use: self.onTimer()
        This method creates a game cycle at each timer event. """

        self.drawScore()
        self.checkCollisions()

        if self.inGame:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Constants.DELAY, self.onTimer)
        else:
            self.gameOver()

    def drawScore(self):
        """ To use: self.drawScore()
        This method draws the score on the screen. """

        score = self.find_withtag("score")
        self.itemconfigure(score, text="Score: {0}".format(self.score))

    def gameOver(self):
        """ To use: self.gameOver()
        This method deletes all objects and draws the game over message. """

        self.delete(ALL)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2,
                         text = "Game Over with Score {0}".format(self.score),
                         fill = "white")

class Snake(Frame):
    """ To use: Snake()
    This class runs the game and sets up the board using the Board() class. """
    def __init__(self):
        super().__init__()

        self.master.title("Snake")
        self.board = Board()
        self.pack()

def main():
    """ To use: main()
    This function actually runs the game and displays it. """

    root = Tk()
    nib = Snake()
    root.mainloop()

if __name__ == "__main__":
    main()

############ FIN ############