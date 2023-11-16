from collections import defaultdict

from sklearn.cluster import DBSCAN


class ClusterCreator:
    def __init__(self, distance=10, minimum_samples_per_cluster=12):
        self.distance = distance
        self.minimum_samples_per_cluster = minimum_samples_per_cluster

    def calculate(self, points):
        return self._create_dictionary(DBSCAN(eps=self.distance, min_samples=self.minimum_samples_per_cluster)
                                       .fit(points), points)

    def _create_dictionary(self, clustering, points):
        clusters = defaultdict(lambda: [])
        for label, point in zip(clustering.labels_, points):
            if label != -1: clusters[label].append(point)
        return clusters
