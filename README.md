# Sorting Algorithm Visualizer

Real-time sorting algorithm visualization built with Python and Pygame.

## Features
- 5 Algorithms: Bubble, Selection, Insertion, Merge, Quick Sort
- Real-time comparison & swap counters
- Color coding: Comparing / Swapping / Sorted
- Adjustable speed and array size

## Controls
| Key | Action |
|-----|--------|
| `1~5` | Select algorithm |
| `SPACE` | Start / Pause |
| `R` | Reset array |
| `↑ / ↓` | Speed up / down |
| `← / →` | Array size |

## Setup
\```bash
python -m venv venv
venv\Scripts\activate
pip install pygame
python main.py
\```

## Tech Stack
- Python 3.11+
- Pygame 2.x

## Algorithm Complexity
| Algorithm | Average | Worst | Space |
|-----------|---------|-------|-------|
| Bubble    | O(n²)   | O(n²) | O(1)  |
| Selection | O(n²)   | O(n²) | O(1)  |
| Insertion | O(n²)   | O(n²) | O(1)  |
| Merge     | O(n log n) | O(n log n) | O(n) |
| Quick     | O(n log n) | O(n²) | O(log n) |
