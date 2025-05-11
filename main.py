import argparse
import csv
import sys
import plot

import k_means


def load_points(path: str) -> list[list[float]]:
    points = []
    with open(path) as file:
        for row in csv.reader(file):
            points.append([float(x) for x in row])
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

    km_gen = k_means.k_means(points, k)
    result_centroids = []
    result_points = []

    try:
        for i in range(sys.maxsize):
            cen, pts = next(km_gen)

            print(f"\nIteration {i}")
            result_centroids.append(cen)
            result_points.append(pts)

            for c, p in zip(cen, pts):
                print(f"Centroid {c} ----- Points {p}")

    except StopIteration:
        print("Finished")

    plot.show(result_centroids[-1], result_points[-1])


if __name__ == '__main__':
    main()
