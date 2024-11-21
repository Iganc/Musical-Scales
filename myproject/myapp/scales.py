letter_to_num = {
    'C': 1,
    'C#': 2,
    'D': 3,
    'D#': 4,
    'E': 5,
    'F': 6,
    'F#': 7,
    'G': 8,
    'G#': 9,
    'A': 10,
    'A#': 11,
    'B': 12,
}
num_to_letter = {
    1: 'C', 13: 'C',
    2: 'C#', 14: 'C#',
    3: 'D', 15: 'D',
    4: 'D#', 16: 'D#',
    5: 'E', 17: 'E',
    6: 'F', 18: 'F',
    7: 'F#', 19: 'F#',
    8: 'G', 20: 'G',
    9: 'G#', 21: 'G#',
    10: 'A', 22: 'A',
    11: 'A#', 23: 'A#',
    12: 'B', 24: 'B',
}
flats_to_sharps = {
    'C#': 'Db',
    'D#': 'Eb',
    'F#': 'Gb',
    'G#': 'Ab',
    'A#': 'Bb',
    'Db': 'C#',
    'Eb': 'D#',
    'Gb': 'F#',
    'Ab': 'G#',
    'Bb': 'A#'
}



def major_scale(note):
    notes = [note, note + 2, note + 4, note + 5, note + 7, note + 9, note + 11]
    notes = [num_to_letter.get(note, None) for note in notes]
    return notes


def natural_minor_scale(note):
    notes = [note, note + 2, note + 3, note + 5, note + 7, note + 8, note + 10]
    notes = [num_to_letter.get(note, None) for note in notes]
    return notes


def harmonic_minor_scale(note):
    notes = [note, note + 2, note + 3, note + 5, note + 7, note + 8, note + 11]
    notes = [num_to_letter.get(note, None) for note in notes]
    return notes


def melodic_minor_scale(note):
    notes = [note, note + 2, note + 3, note + 5, note + 7, note + 9, note + 11]
    notes = [num_to_letter.get(note, None) for note in notes]
    return notes


def ionian_mode(note):
    notes = major_scale(note)
    return notes


def dorian_mode(note):
    note = note - 2
    if note == -1:
        note = note + 12
    if note == 0:
        note = note + 11
    notes = major_scale(note)
    return notes


def phrygian_mode(note):
    note = note + 5
    if note > 12:
        note = note - 12
    notes = natural_minor_scale(note)
    return notes


def lydian_mode(note):
    note = note + 4
    if note > 12:
        note = note - 12
    notes = natural_minor_scale(note)
    return notes

def mixolydian_mode(note):
    note = note + 2
    if note > 12:
        note = note - 12
    notes = natural_minor_scale(note)
    return notes

def aeolian_mode(note):
    notes = natural_minor_scale(note)
    return notes

def locrian_mode(note):
    note = note + 1
    if note > 12:
        note = note - 12
    notes = major_scale(note)
    return notes

