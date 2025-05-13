import argparse
import csv
import sys

from plot import *
from kmeans import *


def load_points(path: str) -> list[Point]:
    points = []
    with open(path) as file:
        for row in csv.reader(file):
            points.append(Point([float(x) for x in row]))
    return points


def k_means(file_path, k) -> None:
    print("Loading points...")
    points = load_points(file_path)
    print(f"Loaded {len(points)} points")

    if len(points) < k:
        raise ValueError("Number of points must be greater than 'k'.")

    gen = k_means_gen(points, k)
    result_centroids = []

    try:
        for i in range(sys.maxsize):
            result = next(gen)

            print(f"\nIteration {i}")
            result_centroids = result

            total_dist = 0
            for c in result:
                print(f"Centroid {c.coords} ----- Points {[p.coords for p in c.assigned]}")
                print(f"\tdist={c.sum_of_distances()}")
                total_dist += c.sum_of_distances()
            print(f"{total_dist=}")

    except StopIteration:
        print("Finished")

    if len(result_centroids[0].coords) >= 2:
        show(result_centroids)
    if len(result_centroids[0].coords) >= 3:
        show3d(result_centroids)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True, type=str, help="Input .csv file path")
    parser.add_argument("-k", required=True, type=int, help="Number of clusters")

    arg = parser.parse_args()
    k_means(arg.f, arg.k)
