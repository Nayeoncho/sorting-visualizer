import pygame
import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

def generate_array(size):
    # Generate a list of random integers
    return [random.randint(10, 400) for _ in range(size)]

def draw_array(screen, array, highlight=[], stats={}, font=None, speed=0, current_algo=""):
    # Calculate bar width based on screen width and array size
    bar_width = WIDTH // len(array)

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

        # Display stats and speed on screen (only if font is not None)
        if font:
            # stats.get: get data from the dictionary
            text = f"Sorting method: {current_algo}   Comparisons: {stats.get('comparisons', 0)}   Swaps: {stats.get('swaps', 0)}   Speed: {speed}ms"
            # Convert data from text to image(surface)
            surface = font.render(text, True, (255, 255, 255))
            # Attach image on the screen / (10, 10) -> x, y coordinate
            screen.blit(surface, (10, 10))


# Initialize all pygame modules
pygame.init()
font = pygame.font.SysFont("consolas", 16)

# Windows dimensions
WIDTH, HEIGHT = 800, 600

# Create the window with specified dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the window title
pygame.display.set_caption("Sorting Visualizer")

# Generate initial array (add this before the while loop)
array = generate_array(20)

# stats: dictionary
stats = {"swaps": 0, "comparisons": 0}

# Set default values
highlight = []
speed = 100
generator = bubble_sort(array, stats)
current_algo = "bubble"

# Main loop flag
running = True

# Keep running til the user closes the window
while running:
    # Handle events
    for event in pygame.event.get():
        # X button clicked
        if event.type == pygame.QUIT:
            running = False

        # Detect key press
        if event.type == pygame.KEYDOWN:
            # Press key 1, switch to bubble sort
            if event.key == pygame.K_1:
                current_algo = "bubble"
                array = generate_array(20)
                generator = bubble_sort(array, stats)
                stats = {"comparisons": 0, "swaps": 0}
                highlight = []

            # Press key 2, switch to merge sort
            elif event.key == pygame.K_2:
                current_algo = "merge"
                array = generate_array(20)
                generator = merge_sort(array, stats, 0, len(array))
                stats = {"swaps": 0, "comparisons": 0}
                highlight = []

            # Press key 3, switch to quick sort
            elif event.key == pygame.K_3:
                current_algo = "quick"
                array = generate_array(20)
                generator = quick_sort(array, stats, 0, len(array)-1)
                stats = {"swaps": 0, "comparisons": 0}
                highlight = []

            # Reset events
            # R key -> reset
            if event.key == pygame.K_r:
                array = generate_array(20)
                # Reset counter, generator, and clear highlights
                stats = {"comparisons": 0, "swaps": 0}
                highlight = []
                if current_algo == "bubble":
                    generator = bubble_sort(array, stats)
                elif current_algo == "merge":
                    generator = merge_sort(array, stats, 0, len(array))
                elif current_algo == "quick":
                    generator = quick_sort(array, stats, 0, len(array)-1)

            # Speed control events
            if event.key == pygame.K_UP:
                speed = max(10, speed-10)
            elif event.key == pygame.K_DOWN:
                speed = min(300, speed+10)

    # Advance one step of the sort
    try:
        highlight = list(next(generator))
    except StopIteration:
        # Sorting complete
        highlight = []

    # Fill the screen with a dart background color
    screen.fill((18, 18, 24))

    # Inside the while loop, after screen.fill()
    draw_array(screen, array, highlight, stats, font, speed, current_algo)

    # Update the display (swap buffers)
    pygame.display.flip()
    pygame.time.delay(speed)

# Quit pygame and clean up
pygame.quit()




