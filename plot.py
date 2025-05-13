import matplotlib.pyplot as plt
from kmeans import Centroid

def show(centroids: list[Centroid]) -> None:

    plt.figure(figsize=(6, 6))

    for i, c in enumerate(centroids):
        color = plt.color_sequences['Set1'][i]
        plt.scatter(c.coords[0], c.coords[1], color=color, s=80, marker='X', label=f'Centroid {i + 1}')

        for p in c.assigned:
            plt.scatter(p.coords[0], p.coords[1], color=color, s=40)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()


def show3d(centroids: list[Centroid]) -> None:
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')

    for i, c in enumerate(centroids):
        color = plt.color_sequences['Set1'][i]
        ax.scatter(c.coords[0], c.coords[1], c.coords[2], color=color, s=80, marker='X', label=f'Centroid {i + 1}')

        for p in c.assigned:
            ax.scatter(p.coords[0], p.coords[1], p.coords[2], color=color, s=40)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    ax.grid(True)
    plt.show()
