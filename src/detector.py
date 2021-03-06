import cv2
import numpy as np
from bounding_box import BoundingBox
from utils import open_file
from tqdm import tqdm
from typing import List, TypeVar

SheetReader = TypeVar('SheetReader')

class Detector:
    def __init__(self, 
            reader: SheetReader, 
            templates: List[np.ndarray], 
            detection_threshold: float,
            is_staff: bool=False) -> None:

        self._reader = reader
        self._is_staff = is_staff
        self._templates = templates
        self._best_location_count = -1
        self._best_locations = []
        self._best_scale = 0
        self._boxes = []
        self._detection_threshold = detection_threshold
        self._iou_threshold = 0.3

    # Locate target position
    def _locate(self) -> None:
        for scale in np.arange(self._reader._start_size, 
                               self._reader._stop_size + 0.01, 
                               self._reader._search_step):
            locations = []
            location_count = 0
            for template in self._templates:
                if template is None:
                    continue
                template = cv2.resize(template, None, 
                                      fx=scale, fy=scale, 
                                      interpolation=cv2.INTER_CUBIC)
                result = cv2.matchTemplate(self._reader._img, template, cv2.TM_CCOEFF_NORMED)
                result = np.where(result >= self._detection_threshold)
                location_count += len(result[0])
                locations += [result]
            print('scale: {:1.2f}, matches: {:d}'.format(scale, location_count))

            if (location_count > self._best_location_count):
                self._best_location_count = location_count
                self._best_locations = locations
                self._best_scale = scale

    # Generate bounding boxes
    def _generate_boxes(self) -> None:
        for i in tqdm(range(len(self._templates))):
            h, w = np.array(self._templates[i].shape) * self._best_scale
            if self._is_staff:
                self._boxes.append([BoundingBox(0, pt[0], self._reader.img_width, h) 
                                    for pt in zip(*self._best_locations[i])])
            else:
                self._boxes.append([BoundingBox(pt[1], pt[0], w, h) 
                                    for pt in zip(*self._best_locations[i])])
        self._boxes = [j for i in self._boxes for j in i]

    # Merge bounding boxes
    def _merge(self) -> None:
        self._filtered_boxes = []
        while len(self._boxes) > 0:
            box = self._boxes.pop(0)
            # TODO: KD-Tree
            self._boxes.sort(key=lambda bounding_box: bounding_box.distance(box))
            merged = False
            while(not merged):
                merged = True
                i = 0
                for _ in range(len(self._boxes)):
                    if box.iou(self._boxes[i]) > self._iou_threshold or self._boxes[i].iou(box) > self._iou_threshold:
                        box = box.merge(self._boxes.pop(i))
                        merged = False
                    elif box.distance(self._boxes[i]) > box.w / 2 + self._boxes[i].w / 2:
                        break
                    else:
                        i += 1
            self._filtered_boxes.append(box)

    def detect(self) -> List[BoundingBox]:
        print('Locating...')
        self._locate()
        print('Generating bounding boxes...')
        self._generate_boxes()
        print('Merging bounding boxes...')
        self._merge()
        print('Total number of boxes: {}'.format(len(self._filtered_boxes)))
        return self._filtered_boxes