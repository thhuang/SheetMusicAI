import os
import sys
import subprocess
import cv2

def open_file(path):
    cmd = {'linux': 'eog', 'win32': 'explorer', 'darwin': 'open'}[sys.platform]
    subprocess.run([cmd, path])

def load_imgs(img_dir):
    filenames = os.listdir(img_dir)
    paths = [os.path.join(img_dir, name) for name in filenames]
    return [cv2.imread(img_path, 0) for img_path in paths]

def draw_boxes(filename, img, boxes, ):
    boxes_img = img.copy()
    for box in boxes:
        box.draw(boxes_img, (0, 0, 255), 4)
    cv2.imwrite(filename, boxes_img)
    open_file(filename)