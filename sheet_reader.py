import argparse
import cv2
from utils import open_file, load_imgs, draw_boxes
from detector import Detector

class SheetReader:
    def __init__(self, input):
        self._sheet_img_path = input
        self._start_size = 0.5  # TODO: DRY
        self._stop_size = 1.2   # TODO: DRY
        self._threshold_staff = 0.87  # TODO: DRY
        self._threshold_sharp = 0.75  # TODO: DRY
        self._threshold_flat = 0.75  # TODO: DRY
        self._threshold_quarter = 0.75  # TODO: DRY
        self._threshold_half = 0.75  # TODO: DRY
        self._threshold_whole = 0.75  # TODO: DRY
        self._threshold_half_rest = 0.9  # TODO: DRY
        self._width_resized = 2048
        self._search_step = 0.02

        # Read data
        self._img = cv2.imread(self._sheet_img_path, 0)  # grey scale
        self._img_height, self._img_width = self._img.shape

        # Preprocess
        self._preprocess()

    def _preprocess(self):
        # Color filter
        _, self._img = cv2.threshold(self._img, 127, 255, cv2.THRESH_BINARY)

        # Resize
        scale = self._width_resized / self._img_width
        self._img = cv2.resize(self._img, None, fx = scale, fy = scale, interpolation = cv2.INTER_CUBIC)
        self._img_height, self._img_width = self._img.shape  # update the size of the image
        
        # RGB image
        self._img_rgb = cv2.cvtColor(self._img, cv2.COLOR_GRAY2RGB)

        # Save image
        cv2.imwrite('sheet_proprocessed.png', self._img)
        #open_file('sheet_proprocessed_resized.png')

    def detect_staff(self, staff_dir):
        staff_imgs = load_imgs(staff_dir)
        detector = Detector(self, staff_imgs, self._threshold_staff)
        self._staff_boxes = detector.detect()
        draw_boxes('staff_boxes_img.png', self._img_rgb, self._staff_boxes)

    def detect_sharp(self, sharp_dir):
        sharp_imgs = load_imgs(sharp_dir)
        detector = Detector(self, sharp_imgs, self._threshold_sharp)
        self._sharp_boxes = detector.detect()
        draw_boxes('sharp_boxes_img.png', self._img_rgb, self._sharp_boxes)

    def detect_flat(self, flat_dir):
        flat_imgs = load_imgs(flat_dir)
        detector = Detector(self, flat_imgs, self._threshold_flat)
        self._flat_boxes = detector.detect()
        draw_boxes('flat_boxes_img.png', self._img_rgb, self._flat_boxes)

    def detect_quarter(self, quarter_dir):
        quarter_imgs = load_imgs(quarter_dir)
        detector = Detector(self, quarter_imgs, self._threshold_quarter)
        self._quarter_boxes = detector.detect()
        draw_boxes('quarter_boxes_img.png', self._img_rgb, self._quarter_boxes)

    def detect_half(self, half_dir):
        half_imgs = load_imgs(half_dir)
        detector = Detector(self, half_imgs, self._threshold_half)
        self._half_boxes = detector.detect()
        draw_boxes('half_boxes_img.png', self._img_rgb, self._half_boxes)

    def detect_whole(self, whole_dir):
        whole_imgs = load_imgs(whole_dir)
        detector = Detector(self, whole_imgs, self._threshold_whole)
        self._whole_boxes = detector.detect()
        draw_boxes('whole_boxes_img.png', self._img_rgb, self._whole_boxes)

    def detect_half_rest(self, half_rest_dir):
        half_rest_imgs = load_imgs(half_rest_dir)
        detector = Detector(self, half_rest_imgs, self._threshold_half_rest)
        self._half_rest_boxes = detector.detect()
        draw_boxes('half_rest_boxes_img.png', self._img_rgb, self._half_rest_boxes)







