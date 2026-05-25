import pygame
import random

def generate_array(size):
    # Generate a list of random integers
    return [random.randint(10, 400) for _ in range(size)]

def draw_array(screen, array, highlight):
    # Calculate bar width based on screen width and array size
    bar_width = WIDTH / len(array)

    for i, value in enumerate(array):
        # Calculate x position and bar height
        x = i * bar_width
        bar_height = value
        y = HEIGHT - bar_height

        # Change color if this bar is being compared
        if i in highlight:
            color = (251, 146, 60)
        else:
            color = (99, 102, 241)

        # Draw each bar as a rectangle
        pygame.draw.rect(screen, color, (x, y, bar_width-2, bar_height))

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # Swap adjacent element
                array[j], array[j + 1] = array[j + 1], array[j]
                yield j, j+1



# Initialize all pygame modules
pygame.init()

# Windows dimensions
WIDTH, HEIGHT = 800, 600

# Create the window with specified dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Sorting Visualizer")

# Generate initial array (add this before the while loop)
array = generate_array(50)
generator = bubble_sort(array)
highlight = []

# Main loop flag
running = True

# test = [5,3,8,1,9,2]
# print("Before:", test)
# bubble_sort(test)
# print("After:", test)

# Keep running til the user closes the window
while running:
    # Handle events
    for event in pygame.event.get():
        # X button clicked
        if event.type == pygame.QUIT:
            running = False

    # Advance one step of the sort
    try:
        highlight = list(next(generator))
    except StopIteration:
        # Sorting complete
        highlight = []

    # Fill the screen with a dart background color
    screen.fill((18, 18, 24))

    # Inside the while loop, after screen.fill()
    draw_array(screen, array, highlight)

    # Update the display (swap buffers)
    pygame.display.flip()
    pygame.time.delay(100)

# Quit pygame and clean up
pygame.quit()




