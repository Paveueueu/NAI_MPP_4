import random

class Point:
    def __init__(self, coords: list[float]):
        self.coords = coords


class Centroid(Point):
    def __init__(self, coords: list[float]):
        super().__init__(coords)
        self.assigned = []

    def distance_to(self, point: Point):
        return sum([(a - b)**2 for a, b in zip(self.coords, point.coords)])

    def sum_of_distances(self):
        return sum([self.distance_to(p) for p in self.assigned])

def k_means_gen(points: list[Point], k: int):

    # random initialization of centroids
    centroids = [Centroid(point.coords) for point in random.sample(points, k)]

    while True:
        # remove all points assigned to centroid
        for centroid in centroids:
            centroid.assigned = []

        # assign each point to the closest centroid
        for point in points:
            cen = min(centroids, key=lambda c: c.distance_to(point))
            cen.assigned.append(point)

        yield centroids

        # calculate new centroids
        new_centroids = []
        for centroid in centroids:
            if centroid.assigned:
                new_coords = [
                    sum(point.coords[i] for point in centroid.assigned) / len(centroid.assigned)
                    for i in range(len(centroid.coords))
                ]
                new_centroids.append(Centroid(new_coords))
            else:
                new_centroids.append(centroid)

        # if nothing changed then break
        if all(new.distance_to(old) == 0 for new, old in zip(new_centroids, centroids)):
            break

        centroids = new_centroids

    yield centroids
