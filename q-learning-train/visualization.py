import matplotlib.pyplot as plt
from train import Qmaze, show

def plot_maze(maze):
    plt.figure(figsize=(8, 8))
    plt.imshow(maze, cmap='binary')
    plt.grid(True)
    plt.xticks(range(maze.shape[1]))
    plt.yticks(range(maze.shape[0]))
    plt.show()

def plot_mouse_path(qmaze: Qmaze, title="Mouse Path"):
    canvas = qmaze.draw_maze()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(canvas, cmap='gray')
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.title(title)
    plt.show()

def plot_training_history(history):
    plt.plot(history['win_rate'], label='Win rate')
    plt.plot(history['loss'], label='Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Win rate/Loss')
    plt.title('Training History')
    plt.legend()
    plt.show()
