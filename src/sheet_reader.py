import argparse
import cv2
from utils import open_file, load_imgs, draw_boxes
from detector import Detector

class SheetReader:
    def __init__(self, input: str) -> None:
        self._sheet_img_path = input
        self._notes = []
        self._start_size = 0.5  # TODO: DRY
        self._stop_size = 0.9   # TODO: DRY
        self._threshold_staff = 0.87  # TODO: DRY
        self._threshold_sharp_sign = 0.75  # TODO: DRY
        self._threshold_flat_sign = 0.75  # TODO: DRY
        self._threshold_natural_sign = 0.75  # TODO: DRY
        self._threshold_quarter_note = 0.75  # TODO: DRY
        self._threshold_half_note = 0.75  # TODO: DRY
        self._threshold_whole_note = 0.75  # TODO: DRY
        self._threshold_half_rest = 0.9  # TODO: DRY
        self._width_resized = 2048
        self._search_step = 0.02

        # Read data
        self._img = cv2.imread(self._sheet_img_path, 0)  # grey scale
        self._img_height, self._img_width = self._img.shape

        # Preprocess
        self._preprocess()

    def _preprocess(self) -> None:
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
        open_file('sheet_proprocessed.png')

    @property
    def img_height(self) -> float:
        return self._img_height
    
    @property
    def img_width(self) -> float:
        return self._img_width

    def detect_staff(self, staff_dir: str) -> None:
        staff_imgs = load_imgs(staff_dir)
        detector = Detector(self, staff_imgs, self._threshold_staff, is_staff=True)
        self._staff_boxes = detector.detect()
        draw_boxes('staff_boxes_img.png', self._img_rgb, self._staff_boxes)

    def detect_sharp_sign(self, sharp_sign_dir: str) -> None:
        sharp_sign_imgs = load_imgs(sharp_sign_dir)
        detector = Detector(self, sharp_sign_imgs, self._threshold_sharp_sign)
        self._sharp_sign_boxes = detector.detect()
        draw_boxes('sharp_sign_boxes_img.png', self._img_rgb, self._sharp_sign_boxes)

    def detect_flat_sign(self, flat_sign_dir: str) -> None:
        flat_sign_imgs = load_imgs(flat_sign_dir)
        detector = Detector(self, flat_sign_imgs, self._threshold_flat_sign)
        self._flat_sign_boxes = detector.detect()
        draw_boxes('flat_sign_boxes_img.png', self._img_rgb, self._flat_sign_boxes)

    def detect_natural_sign(self, natural_sign_dir: str) -> None:
        natural_sign_imgs = load_imgs(natural_sign_dir)
        detector = Detector(self, natural_sign_imgs, self._threshold_natural_sign)
        self._natural_sign_boxes = detector.detect()
        draw_boxes('natural_sign_boxes_img.png', self._img_rgb, self._natural_sign_boxes)

    def detect_quarter_note(self, quarter_note_dir: str) -> None:
        quarter_note_imgs = load_imgs(quarter_note_dir)
        detector = Detector(self, quarter_note_imgs, self._threshold_quarter_note)
        self._quarter_note_boxes = detector.detect()
        draw_boxes('quarter_note_boxes_img.png', self._img_rgb, self._quarter_note_boxes)

    def detect_half_note(self, half_note_dir: str) -> None:
        half_note_imgs = load_imgs(half_note_dir)
        detector = Detector(self, half_note_imgs, self._threshold_half_note)
        self._half_note_boxes = detector.detect()
        draw_boxes('half_note_boxes_img.png', self._img_rgb, self._half_note_boxes)

    def detect_whole_note(self, whole_note_dir: str) -> None:
        whole_note_imgs = load_imgs(whole_note_dir)
        detector = Detector(self, whole_note_imgs, self._threshold_whole_note)
        self._whole_note_boxes = detector.detect()
        draw_boxes('whole_note_boxes_img.png', self._img_rgb, self._whole_note_boxes)

    def detect_half_rest(self, half_rest_dir: str) -> None:
        half_rest_imgs = load_imgs(half_rest_dir)
        detector = Detector(self, half_rest_imgs, self._threshold_half_rest)
        self._half_rest_boxes = detector.detect()
        draw_boxes('half_rest_boxes_img.png', self._img_rgb, self._half_rest_boxes)

    def decode(self):
        for staff_box in self._staff_boxes:
            pass





