from ClusterCreator import ClusterCreator
from HighContrastPointDetector import HighContrastPointDetector
from ImageProportionalResizer import ImageProportionalResizer
from OrientationFieldCreator import OrientationFieldCreator

resizer = ImageProportionalResizer()
orientation_field_creator = OrientationFieldCreator(16)
hc_detector = HighContrastPointDetector(3.5)
cluster_creator = ClusterCreator(distance=5, minimum_samples_per_cluster=20)


class Fingerprint:
    def __init__(self, name, fingerprint_image):
        self.name = name
        self.resized_image = resizer.resize(fingerprint_image, proportion=1/3) if fingerprint_image.shape[0] > 200 else fingerprint_image
        self.orientation_field = orientation_field_creator.create_field_for(self.resized_image)
        self.hc_points = hc_detector.calculate_for(self.orientation_field)
        self.clusters = cluster_creator.calculate(self.hc_points)
