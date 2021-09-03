import random
import pygame 

#  CONSTANTS
SUITS = {"S":"\u2664", "H":"\u2661", "C": "\u2667", "D": "\u2662"}
RANKS = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

BLACK = (0,0,0)
WHITE = (255, 255, 255)

# A basic class for a card
class Card:
    def __init__(self, rank, suit):
        #  Member variables
        self.rank = rank
        self.suit = suit
        self.image = 'img/' + self.rank + self.suit + '.png'

    def print(self):
        print(self.rank + ' ' + self.suit)

    def display(self, canvas, x, y):
        img = pygame.image.load(self.image).convert()
        canvas.blit(img, (x, y))


# A basic standard deck
class Deck:
    def __init__(self):
        # member variable 
        self.cards = [Card(value, suit) for value in RANKS for suit in SUITS]

    def print(self):
        for card in self.cards:
            card.print()

    def deal(self):
        random.shuffle(self.cards)
        return self.cards.pop()

# Define your game class
class Game:
    pass
            
    
#  Basic button
class Button:
    def __init__(self, text, position, dimensions, action=None):
        self.font = pygame.font.SysFont('Courier', 25, True, False)
        self.text = self.font.render(text, True, BLACK)
        self.rect = self.text.get_rect()
        self.position = position
        self.dimensions = dimensions

        self.action = action

    def draw(self, surface):
        x, y = self.position
        w, h = self.dimensions

        self.rect.center = ((x + (w*0.5)), (y + (h*0.5))) 
        pygame.draw.rect(surface, WHITE, (x, y, w, h))
        surface.blit(self.text, self.rect)

    def isOver(self):
        x, y = self.position
        w, h = self.dimensions
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            return True
        else:
            return False