import numpy as np
import cv2 as cv


class HighContrastPointDetector:
    def __init__(self, std):
        self.std = std

    def calculate_for(self, image):
        total_gradient_change = self._calculate_gradient(image)
        return np.argwhere(total_gradient_change > self._contrast_threshold(total_gradient_change))

    def _contrast_threshold(self, total_gradient_change):
        return np.mean(total_gradient_change) + self.std * np.std(total_gradient_change)

    def _calculate_gradient(self, image):
        sobel_x_abs = np.abs(cv.Sobel(image, cv.CV_64F, 1, 0, ksize=11))
        sobel_y_abs = np.abs(cv.Sobel(image, cv.CV_64F, 0, 1, ksize=11))
        return sobel_x_abs + sobel_y_abs
