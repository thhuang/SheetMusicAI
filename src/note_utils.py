from enum import Enum


class Pitch(Enum):
    # http://newt.phys.unsw.edu.au/jw/notes.html
    A0 = 21
    B0 = 23
    C1 = 24
    D1 = 26
    E1 = 28
    F1 = 29
    G1 = 31
    A1 = 33
    B1 = 35
    C2 = 36
    D2 = 38
    E2 = 40
    F2 = 41
    G2 = 43
    A2 = 45
    B2 = 47
    C3 = 48
    D3 = 50
    E3 = 52
    F3 = 53
    G3 = 55
    A3 = 57
    B3 = 59
    C4 = 60
    D4 = 62
    E4 = 64
    F4 = 65
    G4 = 67
    A4 = 69
    B4 = 71
    C5 = 72
    D5 = 74
    E5 = 76
    F5 = 77
    G5 = 79
    A5 = 81
    B5 = 83
    C6 = 84
    D6 = 86
    E6 = 88
    F6 = 89
    G6 = 91
    A6 = 93
    B6 = 95
    C7 = 96
    D7 = 98
    E7 = 100
    F7 = 101
    G7 = 103
    A7 = 105
    B7 = 107
    C8 = 108

class NoteLength(Enum):
    # http://neilhawes.com/sstheory/theory12.htm
    WHOLE = 1
    HALF = 1/2
    QUARTER = 1/4
    EIGHT = 1/8
    SIXTEENTH = 1/16
    THIRTYSECOND = 1/32
    SIXTYFOURTH = 1/64

NOTE_DIC = {
     22: Pitch.C8,
     21: Pitch.B7,
     20: Pitch.A7,
     19: Pitch.G7,
     18: Pitch.F7,
     17: Pitch.E7,
     16: Pitch.D7,
     15: Pitch.C7,
     14: Pitch.B6,
     13: Pitch.A6,
     12: Pitch.G6,
     11: Pitch.F6,
     10: Pitch.E6,
      9: Pitch.D6,
      8: Pitch.C6,
      7: Pitch.B5,
      6: Pitch.A5,
      5: Pitch.G5,
      4: Pitch.F5,
      3: Pitch.E5,
      2: Pitch.D5,
      1: Pitch.C5,
      0: Pitch.B4,
     -1: Pitch.A4,
     -2: Pitch.G4,
     -3: Pitch.F4,
     -4: Pitch.E4,
     -5: Pitch.D4,
     -6: Pitch.C4,
     -7: Pitch.B3,
     -8: Pitch.A3,
     -9: Pitch.G3,
    -10: Pitch.F3,
    -11: Pitch.E3,
    -12: Pitch.D3,
    -13: Pitch.C3,
    -14: Pitch.B2,
    -15: Pitch.A2,
    -16: Pitch.G2,
    -17: Pitch.F2,
    -18: Pitch.E2,
    -19: Pitch.D2,
    -20: Pitch.C2,
}