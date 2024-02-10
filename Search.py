import pyglet
import random

window = pyglet.window.Window(width=810, height=600, caption='Search Comparison')
batch = pyglet.graphics.Batch()

numbers_linear = random.sample(range(1, 100), 19) + [42]
random.shuffle(numbers_linear)

current_index_linear = 0
found_index_linear = -1
search_complete_linear = False

numbers_binary = sorted(random.sample(range(1, 100), 19) + [42])
target_binary = 42
low_binary = 0
high_binary = len(numbers_binary) - 1
search_complete_binary = False

def linear_search(dt):
    global current_index_linear, found_index_linear, search_complete_linear
    if current_index_linear < len(numbers_linear):
        if numbers_linear[current_index_linear] == 42:
            found_index_linear = current_index_linear
            search_complete_linear = True
        current_index_linear += 1
    else:
        search_complete_linear = True

def binary_search(dt):
    global low_binary, high_binary, search_complete_binary
    if low_binary <= high_binary and not search_complete_binary:
        mid = (low_binary + high_binary) // 2
        if numbers_binary[mid] == target_binary:
            search_complete_binary = True
        elif numbers_binary[mid] < target_binary:
            low_binary = mid + 1
        else:
            high_binary = mid - 1
    else:
        search_complete_binary = True

@window.event
def on_draw():
    window.clear()
    
    # Linear search visualization
    for i, number in enumerate(numbers_linear):
        x = i * 40 + 10
        y = window.height - 200
        width = 30
        height = 30

        if i == current_index_linear and not search_complete_linear:
            color = (255, 0, 0)
        elif i == found_index_linear:
            color = (50, 205, 50)
        else:
            color = (200, 200, 200)
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()
    
    # Binary search visualization
    for i, number in enumerate(numbers_binary):
        x = i * 40 + 10
        y = window.height - 400
        width = 30
        height = 30

        if not search_complete_binary and (i == low_binary or i == high_binary):
            color = (255, 140, 0)  # Yellow for low and high pointers
        elif not search_complete_binary and low_binary <= i <= high_binary:
            color = (0, 0, 128)  # Blue for the range being searched
        elif search_complete_binary and number == target_binary:
            color = (50, 205, 50)  # Green for the found number
        else:
            color = (200, 200, 200)  # Default color
        
        pyglet.shapes.Rectangle(x, y, width, height, color=color, batch=batch).draw()
        label = pyglet.text.Label(str(number), x=x+width//2, y=y+height//2, anchor_x='center', anchor_y='center', batch=batch)
        label.draw()

pyglet.clock.schedule_interval(linear_search, 0.5)
pyglet.clock.schedule_interval(binary_search, 0.5)
pyglet.app.run()
