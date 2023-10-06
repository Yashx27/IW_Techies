import pygame
import random
import os
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 30

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Vegetable or Fruit")

# Load vegetable and fruit images
image_dir = "image_dir"  
image_files = os.listdir(image_dir)
images = [pygame.image.load(os.path.join(image_dir, file)) for file in image_files]

# Create a dictionary of words (vegetable and fruit names) and their corresponding images
word_image_dict = {
    "carrot": "carrot.png",
    "cucumber": "cucumber.png",
    "tomato": "tomato.png",
    "apple": "apple.png",
    "banana": "banana.png",
    "orange": "orange.png"
}

# Initialize variables
current_word = ""
current_image = None
score = 0
input_text = ""
correct_answer_displayed = False
correct_answer_display_time = 2  # Display "Good job!" for 2 seconds
image_display_time = 3  # Display each image for 3 seconds
last_image_display_time = 0
user_answered = False

# Fonts
font = pygame.font.Font(None, 36)

# Function to select a random word and corresponding image
def select_word_and_image():
    global current_word, current_image
    current_word = random.choice(list(word_image_dict.keys()))
    current_image = pygame.image.load(os.path.join(image_dir, word_image_dict[current_word]))

# Function to display text on the screen
def display_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))

# Main game loop
running = True
select_word_and_image()
correct_answer_timer = 0

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                if not user_answered:
                    # Check if the entered word matches the current word
                    user_input = input_text.strip().lower()
                    if user_input == current_word:
                        score += 1
                        correct_answer_timer = time.time()
                    user_answered = True
                # Select a new word and image
                select_word_and_image()
                input_text = ""
                user_answered = False
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Clear the screen
    screen.fill(WHITE)

    # Display the current image
    if current_image:
        if user_answered and time.time() - last_image_display_time >= image_display_time:
            select_word_and_image()
            user_answered = False
        screen.blit(current_image, (WIDTH // 2 - current_image.get_width() // 2, HEIGHT // 4))
        last_image_display_time = time.time()

    # Display the current word
    display_text("Guess: " + input_text, 300, 400)

    # Display the user's score
    display_text("Score: " + str(score), 20, 20)

    # Display "Good job!" for a short time if the answer was correct
    if correct_answer_timer > 0:
        display_text("Good job!", 300, 500)
        if time.time() - correct_answer_timer >= correct_answer_display_time:
            correct_answer_timer = 0

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
