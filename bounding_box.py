import cv2
import numpy as np

class BoundingBox:
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._center = np.array((x + w / 2, y + h / 2))
        self._area = w * h
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    @property
    def w(self):
        return self._w

    @property
    def h(self):
        return self._h
    
    @property
    def center(self):
        return self._center

    def iou(self, other):
        dx = max(0, min(self.x + self.w, other.x + other.w) - max(self.x, other.x))
        dy = max(0, min(self.y + self.h, other.y + other.h) - max(self.y, other.y))
        return dx * dy / self._area

    def distance(self, other):
        return np.linalg.norm(self.center - other.center)

    def merge(self, other):
        x = min(self.x, other.x)
        y = min(self.y, other.y)
        w = max(self.x + self.w, other.x + other.w) - x
        h = max(self.y + self.h, other.y + other.h) - y
        return BoundingBox(x, y, w, h)

    def draw(self, img, color, thickness):
        pos = (int(self.x), int(self.y))
        size = (int(self.x + self.w), int(self.y + self.h))
        cv2.rectangle(img, pos, size, color, thickness)