import pygame
import random
import os
import time

class VegetableFruitGame:
    def __init__(self):
        pygame.init()

        # Constants
        self.WIDTH, self.HEIGHT = 1040, 800
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.FPS = 30

        # Initialize the game window
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Guess the Vegetable or Fruit")

        # Create a dictionary of words (vegetable and fruit names) and their corresponding images
        self.word_image_dict = {
            "carrot": "carrot.png",
            "cucumber": "cucumber.png",
            "tomato": "tomato.png",
            "apple": "apple.png",
            "banana": "banana.png",
            "orange": "orange.png"
        }

        # Initialize variables
        self.current_word = ""
        self.options = []
        self.correct_option = ""
        self.score = 0
        self.correct_answer_displayed = False
        self.correct_answer_display_time = 1  # Display "Good job!" for 1 second
        self.image_display_time = 3  # Display each image for 3 seconds
        self.last_image_display_time = 0
        self.user_answered = False
        self.selected_option = None  # Track the selected option

        # Fonts
        self.font = pygame.font.Font(None, 36)

        self.clock = pygame.time.Clock()
        self.running = True
        self.questions_asked = 0  # Counter for questions asked
        self.max_questions = 10  # Maximum number of questions per session
        self.select_word_and_options()
        self.correct_answer_timer = 0

    # Function to select a random word and multiple-choice options
    def select_word_and_options(self):
        if self.questions_asked >= self.max_questions:
            self.end_game()  # End the game when max questions are reached
            return

        self.current_word = random.choice(list(self.word_image_dict.keys()))
        self.correct_option = self.current_word
        self.options = [self.correct_option]  # Initialize options with the correct answer
        while len(self.options) < 4:
            option = random.choice(list(self.word_image_dict.keys()))
            if option != self.correct_option and option not in self.options:
                self.options.append(option)
        random.shuffle(self.options)  # Shuffle the options to randomize their order
        self.questions_asked += 1  # Increment the questions asked counter

    # Function to display text on the screen
    def display_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.BLACK)
        self.screen.blit(text_surface, (x, y))

    # Function to display multiple-choice options
    def display_options(self):
        option_texts = [f"Option {i + 1}: {self.options[i]}" for i in range(len(self.options))]
        for i, opt_text in enumerate(option_texts):
            self.display_text(opt_text, 400, 400 + i * 80)

    # Function to end the game and display the final score
    def end_game(self):
        self.screen.fill(self.WHITE)
        end_text = f"You won! Score: {self.score}/{self.max_questions}"
        self.display_text(end_text, 400, 400)
        pygame.display.flip()
        time.sleep(3)  # Display the end message for 3 seconds before quitting
        self.running = False

    # Main game loop
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if not self.user_answered:
                        for i in range(len(self.options)):
                            option_rect = pygame.Rect(400, 400 + i * 80, 300, 50)  # Adjust the rectangle size as needed
                            if option_rect.collidepoint(x, y):
                                self.selected_option = self.options[i]
                                if self.selected_option == self.correct_option:
                                    self.score += 1
                                    self.correct_answer_timer = time.time()
                                self.user_answered = True
                                self.select_word_and_options()  # Call this to move to the next question
                                self.user_answered = False  # Reset user_answered

            # Clear the screen
            self.screen.fill(self.WHITE)

            # Display the current image
            if self.user_answered and time.time() - self.last_image_display_time >= self.image_display_time:
                self.user_answered = False
            if self.current_word in self.word_image_dict:
                self.current_image = pygame.image.load(os.path.join("guess_game/image_dir", self.word_image_dict[self.current_word]))
                self.screen.blit(self.current_image, (self.WIDTH // 2 - self.current_image.get_width() // 2, self.HEIGHT // 4))
                self.last_image_display_time = time.time()

            # Display multiple-choice options
            self.display_options()

            # Display the user's score
            self.display_text("Score: " + str(self.score), 20, 20)

            # Display "Good job!" for a short time if the answer was correct
            if self.correct_answer_timer > 0:
                self.display_text("Good job!", 450, 150)
                if time.time() - self.correct_answer_timer >= self.correct_answer_display_time:
                    self.correct_answer_timer = 0

            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()

# Create an instance of the game and run it
if __name__ == "__main__":
    game = VegetableFruitGame()
    game.run()
