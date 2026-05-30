import pygame
import random

def generate_array(size):
    # Generate a list of random integers
    return [random.randint(10, 400) for _ in range(size)]

def draw_array(screen, array, highlight=[], stats={}, font=None, speed=0):
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
            text = f"Comparisons: {stats.get('comparisons', 0)}   Swaps: {stats.get('swaps', 0)}   Speed: {speed}ms"
            # Convert data from text to image(surface)
            surface = font.render(text, True, (255, 255, 255))
            # Attach image on the screen / (10, 10) -> x, y coordinate
            screen.blit(surface, (10, 10))


def bubble_sort(array, stats):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            # Count each comparison
            stats["comparisons"] += 1
            if array[j] > array[j + 1]:
                # Swap adjacent element
                array[j], array[j + 1] = array[j + 1], array[j]
                # Count each swap
                stats["swaps"] += 1
            yield j, j+1



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
generator = bubble_sort(array, stats)
highlight = []
speed = 100

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
            # Reset events
            # R key -> reset
            if event.key == pygame.K_r:
                array = generate_array(20)
                # Reset counter, generator, and clear highlights
                stats = {"comparisons": 0, "swaps": 0}
                generator = bubble_sort(array, stats)
                highlight = []

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
    draw_array(screen, array, highlight, stats, font, speed)

    # Update the display (swap buffers)
    pygame.display.flip()
    pygame.time.delay(speed)

# Quit pygame and clean up
pygame.quit()




