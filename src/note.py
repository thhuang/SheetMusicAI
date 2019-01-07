from note_utils import NOTE_DIC, NoteLength, Pitch
from typing import TypeVar
BoundingBox = TypeVar('BoundingBox')

# TODO: DRY
STAFF_SCALE = 0.0625

class Note:
    def __init__(self, length: NoteLength, box: BoundingBox, staff_box: BoundingBox) -> None:
        self._box = box
        self._length = length
        self._x, self._y = self._box.center  # TODO: check all types of note
        self._pitch_height = staff_box.h / 16  # TODO: confirm
        self._pitch = NOTE_DIC[int(round((staff_box.center[1] - self._y) / self._pitch_height))]
        
    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def length(self) -> NoteLength:
        return self._length
    
    @property
    def pitch(self) -> Pitch:
        return self._pitch