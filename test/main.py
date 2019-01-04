#! /usr/local/bin/python3

import sys
sys.path.insert(0, '../src')

import argparse
from sheet_reader import SheetReader


if __name__ == '__main__':
    # Argument parser
    parser = argparse.ArgumentParser(description='sum the integers at the command line') 
    parser.add_argument('--input', type=str, help='path to the sheet music image file', required=True)
    args = parser.parse_args()

    reader = SheetReader(args.input)

    # https://www.alt-codes.net/music_note_alt_codes.php
    
    staff_dir = '../data/template/staff'
    reader.detect_staff(staff_dir)

    sharp_sign_dir = '../data/template/sharp_sign'
    reader.detect_sharp_sign(sharp_sign_dir)

    flat_sign_dir = '../data/template/flat_sign'
    reader.detect_flat_sign(flat_sign_dir)

    natural_sign_dir = '../data/template/natural_sign'
    reader.detect_natural_sign(natural_sign_dir)

    quarter_note_dir = '../data/template/quarter_note'
    reader.detect_quarter_note(quarter_note_dir)

    half_note_dir = '../data/template/half_note'
    reader.detect_half_note(half_note_dir)

    whole_note_dir = '../data/template/whole_note'
    reader.detect_whole_note(whole_note_dir)

    half_rest_dir = '../data/template/half_rest'
    reader.detect_half_rest(half_rest_dir)
