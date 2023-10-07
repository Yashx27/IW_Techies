import pygame
from button.button import Button
from math_game.game import Game
import random
import os
import time
from memory_game.memory_game import MGame
from guess_game.guess_game import VegetableFruitGame



pygame.init()
screen_height= 800
screen_width = 1040

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

#font
font = pygame.font.SysFont("arialblack", 40)

#text colour
TEXT_COL = (255, 255, 255)

#images
quiz_img = pygame.image.load("Assests/Quiz.png").convert_alpha()
math_img = pygame.image.load("Assests/Maths.png").convert_alpha()
memory_img = pygame.image.load("Assests/Memory.png").convert_alpha()



#drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#button instances
Quiz_button =  Button(190,295, quiz_img, 0.4)
Memory_button = Button(424,295, memory_img, 0.4)
Math_button = Button(674,295, math_img, 0.4)


#game states
def math():
    pygame.display.set_caption("Math")

    while True:
        menupos = pygame.mouse.get_pos()
        done = False
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        # Create game object
        game = Game()
         # -------- Main Program Loop -----------
        while not done:
            # --- Process events (keystrokes, mouse clicks, etc)
            done = game.process_events()
            # --- Game logic should go here
            game.run_logic()
            # --- Draw the current frame
            game.display_frame(screen)
            # --- Limit to 30 frames per second
            clock.tick(30)
        pygame.quit()

def memory():
    game = MGame()
    game.run()
    

def guess():
    GGame = Game()
    if __name__ == "__main__":
        GGame = VegetableFruitGame()
        GGame.run()



running = True
while running:

    menu_pos = pygame.mouse.get_pos()
    
    
    screen.fill((52,78,91))
    
    
    draw_text("GAME NAME", font, TEXT_COL, 362,142)
    Math_button.draw(screen)
    Quiz_button.draw(screen)
    Memory_button.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Math_button.checkForInput(menu_pos):
                math()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Quiz_button.checkForInput(menu_pos):
                guess()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Memory_button.checkForInput(menu_pos):
                memory()
        
        if event.type == pygame.QUIT:
           running = False
    
    
    pygame.display.update()

pygame.quit()