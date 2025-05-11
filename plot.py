import matplotlib.pyplot as plt

def show(cen, pts):

    plt.figure(figsize=(6, 6))

    for i, (centroid, points) in enumerate(zip(cen, pts)):
        color = plt.color_sequences['Set1'][i]
        print(plt.color_sequences)
        cx, cy = centroid

        plt.scatter(cx, cy, color=color, s=200, marker='X', label=f'Centroid {i + 1}')

        px, py = zip(*points)
        plt.scatter(px, py, color=color, s=100)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()
