#! /usr/local/bin/python3

if __name__ == '__main__':
    classes_file = open('classes.txt', 'w')

    END_LINE = '\n'
    
    # Note and rest
    for i in ['whole', 'half', 'quarter', 'eighth', 'sixteenth', 'thirtysecond', 'sixtyfourth']:
        for d in ['', '_dotted']:
            classes_file.write('rest_{}{}{}'.format(i, d, END_LINE))
            for j in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
                for k in range(8):
                    classes_file.write('note_{}{}_{}{}{}'.format(i, d, j, k, END_LINE))

    # Sign
    classes_file.write('sign_flat{}'.format(END_LINE))
    classes_file.write('sign_natural{}'.format(END_LINE))
    classes_file.write('sign_sharp{}'.format(END_LINE))

    classes_file.close()