#! /usr/local/bin/python3
 
import os
import argparse
import cv2

WIDTH_RESIZED = 2048

if __name__ == "__main__":

    # Argument parser
    parser = argparse.ArgumentParser() 
    parser.add_argument('--dir', type=str, help='path to the sheet music image directory', required=True)
    args = parser.parse_args()

    filenames = os.listdir(args.dir)
    paths = [os.path.join(args.dir, name) for name in filenames]

    for path in paths:
        img = cv2.imread(path, 0)  # grey scale

        # Color filter
        _, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

        # Resize
        scale = WIDTH_RESIZED / img.shape[1]
        img = cv2.resize(img, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)

        # Save image
        print(os.path.join(args.dir, 'preprocessed_{}'.format(path.split('/')[1])))
        cv2.imwrite(os.path.join(args.dir, 'preprocessed_{}'.format(path.split('/')[-1])), img)

