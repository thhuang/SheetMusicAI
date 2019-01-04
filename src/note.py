from typing import TypeVar
BoundingBox = TypeVar('BoundingBox')

# TODO: DRY
note_step = 0.0625

# TODO: ENUM
# TODO: 0 to c4
note_pitch = {
     -4 : ('g5', 79),
     -3 : ('f5', 77),
     -2 : ('e5', 76),
     -1 : ('d5', 74),
      0 : ('c5', 72),
      1 : ('b4', 71),
      2 : ('a4', 69),
      3 : ('g4', 67),
      4 : ('f4', 65),
      5 : ('e4', 64),
      6 : ('d4', 62),
      7 : ('c4', 60),
      8 : ('b3', 59),
      9 : ('a3', 57),
     10 : ('g3', 55),
     11 : ('f3', 53),
     12 : ('e3', 52),
     13 : ('d3', 50),
     14 : ('c3', 48),
     15 : ('b2', 47),
     16 : ('a2', 45),
     17 : ('f2', 53),
}

class Note:
    def __init__(self, box: BoundingBox, staff_box: BoundingBox):
        self._box = box
        
        # TODO: check all types of note
        center_y = self._box.center[1]
        
