import pyglet
import random

window = pyglet.window.Window(width=810, height=200, caption='Binary Search')
batch = pyglet.graphics.Batch()

numbers = sorted(random.sample(range(1, 100), 19) + [42])  # Sorted array for binary search
target = 42
low = 0
high = len(numbers) - 1
search_complete = False

def binary_search(dt):
    global low, high, search_complete
    if low <= high and not search_complete:
        mid = (low + high) // 2
        if numbers[mid] == target:
            search_complete = True
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    else:
        search_complete = True

@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        x = i * 40 + 10
        y = window.height // 2
        width = 30
        height = 30

        if not search_complete and (i == low or i == high):
            color = (255,140,0)  # Yellow for low and high pointers
        elif not search_complete and low <= i <= high:
            color = (0,0,128)  # Blue for the range being searched
        elif search_complete and number == target:
            color = (50, 205, 50)  # Green for the found number
        else:
            color = (200, 200, 200)  # Default color
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.clock.schedule_interval(binary_search, 0.5)
pyglet.app.run()
