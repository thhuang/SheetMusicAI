import argparse
from sheet_reader import SheetReader


if __name__ == '__main__':
    # Argument parser
    parser = argparse.ArgumentParser(description='sum the integers at the command line') 
    parser.add_argument('--input', type=str, help='path to the sheet music image file')
    args = parser.parse_args()

    reader = SheetReader(args.input)

    staff_dir = 'data/template/staff'
    reader.detect_staff(staff_dir)

    sharp_dir = 'data/template/sharp'
    reader.detect_sharp(sharp_dir)

    flat_dir = 'data/template/flat'
    reader.detect_flat(flat_dir)

    quarter_dir = 'data/template/quarter'
    reader.detect_quarter(quarter_dir)

    half_dir = 'data/template/half'
    reader.detect_half(half_dir)

    whole_dir = 'data/template/whole'
    reader.detect_whole(whole_dir)

    half_rest_dir = 'data/template/half_rest'
    reader.detect_half_rest(half_rest_dir)