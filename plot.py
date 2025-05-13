import matplotlib.pyplot as plt

from point import Centroid


def show(centroids: list[Centroid]):

    plt.figure(figsize=(6, 6))

    for i, c in enumerate(centroids):
        color = plt.color_sequences['Set1'][i]
        plt.scatter(c.centroid[0], c.centroid[1], color=color, s=200, marker='X', label=f'Centroid {i + 1}')

        for p in c.assigned:
            plt.scatter(p.coordinates[0], p.coordinates[1], color=color, s=100)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()
