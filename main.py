import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import copy  # To create a copy of the array

# Function to generate a bar chart with current index highlighted
def visualize_sorting_algorithm(algorithm, array):
    fig, ax = plt.subplots()
    bar_container = ax.bar(range(len(array)), array, align="edge")
    ax.set_title(f"{algorithm.__name__.replace('_', ' ').title()} Visualization")
    ax.set_xlim(0, len(array))
    ax.set_ylim(0, int(1.1 * max(array)))

    def update_bars(array, bar_container, current_index):
        for i, (bar, height) in enumerate(zip(bar_container, array)):
            bar.set_height(height)
            # Highlight the current index bar in a different color (e.g., red)
            if i == current_index:
                bar.set_color('red')
            else:
                bar.set_color('blue')

    def animate(data):
        array, current_index = data
        update_bars(array, bar_container, current_index)
        return bar_container

    # Generator function that yields intermediate states of the sorting process with the current index
    def sort_algorithm_gen():
        array_copy = copy.deepcopy(array)  # Make a deep copy of the array
        for array_copy, current_index in algorithm(array_copy):
            yield array_copy, current_index

    ani = animation.FuncAnimation(
        fig,
        animate,
        frames=sort_algorithm_gen,
        interval=100,
        repeat=False,
        cache_frame_data=False,
        save_count=len(array) * len(array)
    )

    # Save the animation as an MP4 file using ffmpeg
    ani.save("sorting_animation.mp4", writer="ffmpeg", dpi=80)

    # Uncomment this if plt.show() works in your environment:
    # plt.show()

# Bubble sort implementation (with yield for visualization and current index)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            yield arr, j  # Yield the array and the current index being compared
        if not swapped:
            break

# Generate a random array
array = random.sample(range(1, 100), 30)  # Random list of 30 integers

# Call the visualizer with bubble sort
visualize_sorting_algorithm(bubble_sort, array)
