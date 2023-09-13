

import random
from cs1graphics import *




# create Hangman class
class Hangman():
    def __init__(self):  # hangman constructor
        # hangman attributes
        self.keywords = ['iPhone',
                         'Airpods',
                         'mouth',
                         'coffe',
                         'Hot',
                         'tropical',
                         'Mud',
                         'Pants',
                         'glove',
                         'Fork',
                         'Hood',
                         'Dog',
                         'Scars',
                         'Bat',
                         'Homerun',
                         'Broke',
                         'Gold',
                         'Silver',
                         'Curtain',
                         'Machine',
                         'Table',
                         'Knife',
                         'Plate',
                         'Mop',
                         'Broom',
                         'Pilow',
                         'Blanked',
                         ]
        self.secretWord = random.choice(self.keywords)
        self.secretHint = []
        self.charGuessed = []
        self.charRight = " "
        self.charWrong = []
        self.numberOfGuesses = 5

        # draw the Canvas screen for the game
        self.hangmanScreen = Canvas(900, 600, "green", "Hangman Game")

        # hangman head
        self.head = Circle(50, Point(250, 150))
        self.head.setFillColor("blue")

        # gameOverText to display that the game is over
        self.gameOverText = Text("Game Over", 50, Point(600, 290))
        self.gameOverText.setFontColor("red")

        # secretTextDescription
        self.secretTextDesc = Text("The secret word was:", 25, Point(500, 350))
        self.secretTextDesc.setFontColor("blue")

        # secretText used to display the secretWord
        self.secretText = Text(self.secretWord, 25, Point(700, 350))
        self.secretText.setFontColor("blue")

        # a text to display a good Bye Message
        self.goodByeMessage = Text("Thanks for playing !!!", 30, Point(610, 400))
        self.goodByeMessage.setFontColor("magenta")

        # a text to display congratulation message
        self.congratulationText = Text("Congratulations !!!", 50, Point(600, 250))
        self.congratulationText.setFontColor("purple")

        # a text to display gameWon message
        self.gameWonText = Text("You've won the game...", 30, Point(580, 310))
        self.gameWonText.setFontColor("magenta")

        # below are three(3) objects to hang the man
        self.baseLine = Rectangle(250, 1, Point(150, 550))
        self.verticalPole = Rectangle(1, 600, Point(50, 250))
        self.topLine = Rectangle(250, 1, Point(150, 50))

        # ropeLine object to hang the head
        self.ropeLine = Rectangle(1, 100, Point(250, 100))

        # hangman body
        self.body = Rectangle(1, 250, Point(250, 320))

        # hangman arms
        self.arms = Rectangle(150, 1, Point(250, 250))

        # bothLegs of hangman (nothing fancy though :) )
        self.bothLegs = Rectangle(150, 1, Point(250, 445))

        # add baseLine, verticalPole, topLine at the start of the program
        self.hangmanScreen.add(self.baseLine)
        self.hangmanScreen.add(self.verticalPole)
        self.hangmanScreen.add(self.topLine)

    # drawHangman() method to draw the man based on guesses as the parameter
    def drawHangman(self, guesses):
        if guesses == 1:
            self.hangmanScreen.add(self.ropeLine)  # draw ropeLine if guesses == 1
        elif guesses == 2:
            self.hangmanScreen.add(self.head)  # draw head if guesses == 2
        elif guesses == 3:
            self.hangmanScreen.add(self.body)  # draw body if guesses == 3
        elif guesses == 4:
            self.hangmanScreen.add(self.arms)  # draw arms if guesses == 4
        elif guesses == 5:
            self.hangmanScreen.add(self.bothLegs)  # draw ropeLine
            self.hangmanScreen.add(self.gameOverText)  # draw gameOverText
            self.hangmanScreen.add(self.secretTextDesc)  # draw secretTextDesc
            self.hangmanScreen.add(self.secretText)  # draw secretText
            self.hangmanScreen.add(self.goodByeMessage)  # draw goodByeMessage

    # playHangman() method to play the game with secret as the parameter
    def playHangman(self, secret):
        # secretWordLength saves the length of the secretWord
        secretWordLength = int((len(self.secretWord)))

        # replace / insert "_" for every character in secretHint using a for loop in range(secretWordLength)
        for i in range(secretWordLength):
            self.secretHint.insert(i, "_")

        # print the secretHint after the above code replaces every character in secretHint
        print("Secret word hint:", self.secretHint)

        # using while loop to control the game based on the number Of guesses
        while self.numberOfGuesses > 0:
            hiddenLettersLeft = 0  # introduce a local variable to track hidden letters left

            # get user input by displaying "Enter a character: " as the prompt
            userInput = input("\nEnter a character: ")
            self.charRight += userInput  # add userInput to charRight

            # using for loop to check if character is in secretWord
            for character in self.secretWord:
                if character in self.charRight:
                    print(character)
                else:
                    print("_")  # print "_" for letters not guessed by the user
                    hiddenLettersLeft += 1  # increase hiddenLettersLeft by 1
            print("\nHidden Letters Left: ", hiddenLettersLeft)  # print number of hidden letters left

            if hiddenLettersLeft == 0:
                print("\t\tCongratulations !!! \n\tYou've won the game")  # print "You've won" message to the console
                print("\tThe secret word was: ", self.secretWord)  # print the secret word to the console
                # add congratulationText, gameWonText, secretTextDesc,secretText and secretWord to hangmanScreen
                self.hangmanScreen.add(self.congratulationText)
                self.hangmanScreen.add(self.gameWonText)
                self.hangmanScreen.add(self.secretTextDesc)
                self.hangmanScreen.add(self.secretText)
                break  # break out of the loop

            # check if userInput not in secretWord
            if userInput not in self.secretWord:
                self.numberOfGuesses -= 1  # decrease numberOfGuesses if userInput is not in secretWord
                self.charWrong.append(userInput)  # append userInput to charWrong
                print("\nWrong guess")  # print "Wrong guess" message to the console
                self.drawHangman(len(self.charWrong))  # call drawHangman() method to draw the hangman
                print("Number of remaining guesses: ", self.numberOfGuesses)  # print number of remaining guesses

                # inner if condition checks if numberOfGuesses == 0
                if self.numberOfGuesses == 0:
                    print("\t\tGame Over")  # print a message indicating the user has lost the game


# create a new hangman player (as an object of the class Hangman())
hangmanPlayer = Hangman()

# call the playHangman() method on the player with secretWord as the parameter
hangmanPlayer.playHangman(hangmanPlayer.secretWord)