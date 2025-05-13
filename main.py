import argparse
import csv
import sys
import plot
from point import Point

import k_means


def load_points(path: str) -> list[Point]:
    points = []
    with open(path) as file:
        for row in csv.reader(file):
            points.append(Point([float(x) for x in row]))
    return points


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True, type=str, help="Input .csv file path")
    parser.add_argument("-k", required=True, type=int, help="Number of clusters")

    args = parser.parse_args()

    file_path = args.f
    k = args.k

    print("Loading points...")
    points = load_points(file_path)
    print("Loaded points")

    if len(points) < k:
        raise ValueError("Number of points must be greater than 'k'.")

    km_gen = k_means.k_means(points, k)
    result_centroids = []

    try:
        for i in range(sys.maxsize):
            res = next(km_gen)

            print(f"\nIteration {i}")
            result_centroids.append(res)

            for c in res:
                print(f"Centroid {c.centroid.coordinates} ----- Points {[p.coordinates for p in c.assigned]}")

    except StopIteration:
        print("Finished")

    plot.show(result_centroids[-1])


if __name__ == '__main__':
    main()
