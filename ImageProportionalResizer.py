import cv2 as cv


class ImageProportionalResizer:
    def resize(self, image, proportion=1/3):
        return cv.resize(image, (int(image.shape[1] * proportion), int(image.shape[0] * proportion)))
