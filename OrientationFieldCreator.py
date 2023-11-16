import cv2 as cv
import numpy as np


class OrientationFieldCreator:
    def __init__(self, block_size):
        self.block_size = block_size

    def _calculate_gradients(self, image, block_size):
        b = block_size // 2
        gradient_x, gradient_y = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3), cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)
        g_xx = np.zeros_like(image, dtype=float)
        g_yy = np.zeros_like(image, dtype=float)
        g_xy = np.zeros_like(image, dtype=float)
        for i in range(b, gradient_x.shape[0] - b):
            for j in range(b, gradient_x.shape[1] - b):
                window_x = gradient_x[i-b:i+b+1, j-b:j+b+1]
                window_y = gradient_y[i-b:i+b+1, j-b:j+b+1]
                g_xx[i, j] = np.sum(window_x ** 2)
                g_yy[i, j] = np.sum(window_y ** 2)
                g_xy[i, j] = np.sum(window_x * window_y)
        return g_xx, g_yy, g_xy

    def create_field_for(self, image):
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) if len(image.shape) == 3 else image
        g_xx, g_yy, g_xy = self._calculate_gradients(gray_image, self.block_size)
        return np.rad2deg(0.5 * np.pi + 0.5 * np.arctan2(2 * g_xy, g_xx - g_yy)) % 180