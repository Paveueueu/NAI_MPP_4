import copy
import random


def get_centroid(points: list[list[float]]):
    if len(points) == 0:
        return None

    n = len(points[0])
    if n == 0:
        return None

    for p in points:
        if len(p) != n:
            return None

    cen = []
    for attr in range(n):
        cen.append(sum([p[attr] for p in points]) / len(points))
    return cen


def assign(points, centroids) -> list[list[list[float]]]:
    assignments = [[] for _ in range(len(centroids))]

    for p in points:
        distances = []
        for c in centroids:
            dist = sum([(x - y)**2 for (x, y) in zip(p, c)])
            distances.append(dist)

        min_index = distances.index(min(distances))
        assignments[min_index].append(p)

    return assignments



def k_means(points, k):
    # random assignment to centroids at first
    assignments = [[] for _ in range(k)]
    for point, cen in zip(points, random.sample(range(k), k)):
        assignments[cen].append(point)

    # get initial centroid for each group
    centroids = []
    for pts in assignments:
        centroids.append(get_centroid(pts))

    # assign each point to the closest centroid
    previous_assignments = copy.deepcopy(assignments)
    assignments = assign(points, centroids)

    # yield first iteration
    yield centroids, assignments


    # do the algorithm until nothing new happens
    while previous_assignments != assignments:
        centroids = []
        for pts in assignments:
            centroids.append(get_centroid(pts))

        previous_assignments = copy.deepcopy(assignments)
        assignments = assign(points, centroids)

        yield centroids, assignments
