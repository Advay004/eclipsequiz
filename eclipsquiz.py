import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define questions and answers
questions = [
    {
        "question": "What causes a lunar eclipse?",
        "options": ["The Earth passes between the Sun and the Moon", "The Moon passes between the Earth and the Sun", "A comet blocks the Moon"],
        "correct_answer": "The Earth passes between the Sun and the Moon",
    },
    #{
        #"question": "What causes a solar eclipse?",
        #"options": ["The Earth passes between the Sun and the Moon", "The Moon passes between the Earth and the Sun", "A comet blocks the Sun"],
        #"correct_answer": "The Moon passes between the Earth and the Sun",
    #},
    {
        "question": "During a total solar eclipse, what is visible from Earth?",
        "options": ["The entire Sun is visible", "The Moon completely covers the Sun", "The Moon partially covers the Sun"],
        "correct_answer": "The Moon completely covers the Sun",
    },
    #{
     #   "question": "What is the phase of the Moon during a lunar eclipse?",
      #  "options": ["Full Moon", "New Moon", "Quarter Moon"],
       # "correct_answer": "Full Moon",
    #},
    {
        "question": "What is the term for the outer part of a shadow during a lunar eclipse?",
        "options": ["Antumbra", "Umbra", "Penumbra"],
        "correct_answer": "Penumbra",
    },
]

# Initialize variables
current_question = 0
score = 0
selected_option = None

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eclipse Quiz")

# Create fonts
font = pygame.font.Font(None, 36)
question_font = pygame.font.Font(None, 48)

# Flag to determine if the answer has been checked
answer_checked = False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not answer_checked:
                if event.key == pygame.K_1:
                    selected_option = 1
                elif event.key == pygame.K_2:
                    selected_option = 2
                elif event.key == pygame.K_3:
                    selected_option = 3
                elif event.key == pygame.K_q:  # Quit game
                    running = False
                else:
                    selected_option = None

    # Clear the screen
    screen.fill(WHITE)

    if current_question < len(questions):
        # Display the current question
        question_text = question_font.render(f"Question {current_question + 1}: {questions[current_question]['question']}", True, BLACK)
        screen.blit(question_text, (20, 20))

        # Display answer options
        for i, option in enumerate(questions[current_question]['options'], start=1):
            option_text = font.render(f"{i}. {option}", True, BLACK)
            screen.blit(option_text, (20, 100 + i * 40))

        if selected_option is not None and not answer_checked:
            correct_answer = questions[current_question]['correct_answer']
            if questions[current_question]['options'][selected_option -1] == correct_answer:
                score += 1
                result_text = font.render("Correct!", True, (0, 255, 0))
            else:
                result_text = font.render(f"Wrong. Correct answer: {correct_answer}", True, (255, 0, 0))
            screen.blit(result_text, (20, SCREEN_HEIGHT - 100))
            answer_checked = True

        # Display current score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (20, SCREEN_HEIGHT - 50))

        if answer_checked:
            next_question_text = font.render("Press 'N' for the next question", True, BLACK)
            screen.blit(next_question_text, (20, SCREEN_HEIGHT - 150))
    else:
        # Display final score
        final_score_text = question_font.render(f"Final Score: {score}/{len(questions)}", True, BLACK)
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - final_score_text.get_height() // 2))
        pygame.display.flip()

    pygame.display.flip()

    if answer_checked and current_question < len(questions):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    current_question += 1
                    answer_checked = False

# Quit Pygame
pygame.quit()
sys.exit()
