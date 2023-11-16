import numpy as np


class DistanceCalculator:
    def _normalize(self, coords):
        min_x = min([coord[0] for coord in coords])
        max_x = max([coord[0] for coord in coords])
        min_y = min([coord[1] for coord in coords])
        max_y = max([coord[1] for coord in coords])
        return np.array([
            np.array([(x - min_x) / (max_x - min_x) if max_x != min_x else 0,
                      (y - min_y) / (max_y - min_y) if max_y != min_y else 0]) for x, y in coords])

    def calculate_distances(self, one_d_points):
        result = []
        for i in range(len([one_d_points[-1]])):
            for j in range(i + 1, len(one_d_points)):
                result.append(abs(one_d_points[i] - one_d_points[j]))
        return result

    def calculate_distance_intra_cluster(self, coords):
        coords = self._normalize(coords)
        max_coord = np.max(coords, axis=0)
        min_coord = np.min(coords, axis=0)
        quartile_x = np.percentile([coord[0] for coord in coords], [10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 100])
        quartile_y = np.percentile([coord[1] for coord in coords], [10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 100])
        centroid = np.mean(coords, axis=0)
        return np.mean(self.calculate_distances(
            list(quartile_x) + list(quartile_y) + list(max_coord) + list(min_coord) + list(centroid)))

    def _calculate_distance_inter_cluster(self, coords_cluster1, coords_cluster2):
        return abs(self.calculate_distance_intra_cluster(coords_cluster1) - self.calculate_distance_intra_cluster(
            coords_cluster2))

    def distance_for(self, finger_print_1, finger_print_2):
        distances = []
        for cluster_key_i in finger_print_1.clusters.keys():
            for cluster_key_j in finger_print_2.clusters.keys():
                distances.append(self._calculate_distance_inter_cluster(finger_print_1.clusters[cluster_key_i],
                                                                        finger_print_2.clusters[cluster_key_j]))
        return abs(len(finger_print_1.clusters) - len(finger_print_2.clusters)) / np.min(distances) if distances else 100
