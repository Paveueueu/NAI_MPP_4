import random
from point import Centroid


def k_means(points, k):
    # assign each point to random number in range [0, k-1]
    assignments = [[points[i]] for i in range(k)]
    for p in points[k:]:
        idx = random.randint(0, k - 1)
        assignments[idx].append(p)

    # create 'k' centroids, each with points from matching group, coordinates of centroid are updated
    centroids = [
        Centroid(assignments[i])
        for i in range(k)
    ]

    yield centroids

    # continue until centroids keep changing coordinates
    while any(c.has_changed() for c in centroids):
        # remove previous assignments
        for c in centroids:
            c.remove_assignments()

        # assign each point to the closest centroid
        for p in points:
            distances = []
            for c in centroids:
                distances.append(c.distance_to(p))

            min_distance = min(distances)
            min_index = distances.index(min_distance)

            centroids[min_index].assign(p)

        for c in centroids:
            c.update_coordinates()

        yield centroids


