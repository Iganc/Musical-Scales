# from EXPLORE_SCALES import major_scale, natural_minor_scale, harmonic_minor_scale, melodic_minor_scale, dorian_mode, lydian_mode, mixolydian_mode, ionian_mode, phrygian_mode, aeolian_mode, locrian_mode
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


# Helper function to rotate the scale to start from the root note
# Helper function to rotate the scale to start from the root note
def rotate_scale(scale, root_note):
    while scale[0] != root_note:
        scale.append(scale.pop(0))  # Move the first element to the end
    return scale

# Ensure note values wrap around correctly (within 1 to 12 range)
def adjust_note_value(note):
    return (note - 1) % 12 + 1  # Ensures the note stays between 1 and 12

# Modes with scale rotation
def ionian_mode(note):
    notes = [note, note + 2, note + 4, note + 5, note + 7, note + 9, note + 11]
    notes = [num_to_letter.get(note, None) for note in notes]
    return notes

def dorian_mode(note):
    notes = [adjust_note_value(note + i) for i in [0, 2, 3, 5, 7, 9, 10]]
    notes = [num_to_letter.get(note, None) for note in notes]
    return rotate_scale(notes, num_to_letter[adjust_note_value(note)])

def phrygian_mode(note):
    notes = [adjust_note_value(note + i) for i in [0, 1, 3, 5, 7, 8, 10]]
    notes = [num_to_letter.get(note, None) for note in notes]
    return rotate_scale(notes, num_to_letter[adjust_note_value(note)])

def lydian_mode(note):
    notes = [adjust_note_value(note + i) for i in [0, 2, 4, 6, 7, 9, 11]]
    notes = [num_to_letter.get(note, None) for note in notes]
    return rotate_scale(notes, num_to_letter[adjust_note_value(note)])

def mixolydian_mode(note):
    notes = [adjust_note_value(note + i) for i in [0, 2, 4, 5, 7, 9, 10]]
    notes = [num_to_letter.get(note, None) for note in notes]
    return rotate_scale(notes, num_to_letter[adjust_note_value(note)])

def aeolian_mode(note):
    notes = [adjust_note_value(note + i) for i in [0, 2, 3, 5, 7, 8, 10]]
    notes = [num_to_letter.get(note, None) for note in notes]
    return rotate_scale(notes, num_to_letter[adjust_note_value(note)])

def locrian_mode(note):
    notes = [adjust_note_value(note + i) for i in [0, 1, 3, 5, 6, 8, 10]]
    notes = [num_to_letter.get(note, None) for note in notes]
    return rotate_scale(notes, num_to_letter[adjust_note_value(note)])

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


note = input("Give me a note: ").upper()
note = letter_to_num.get(note, None)
print(note)
scale = input("What scale are you using? ").lower()
def chord_prog(note, scale):
    scales_and_modes = {
        'major': major_scale(note),
        'natural minor': natural_minor_scale(note),
        'minor': natural_minor_scale(note),
        'harmonic minor': harmonic_minor_scale(note),
        'melodic minor': melodic_minor_scale(note),
        'dorian': dorian_mode(note),
        'phrygian': phrygian_mode(note),
        'lydian': lydian_mode(note),
        'mixolydian': mixolydian_mode(note),
        'locrian': locrian_mode(note),
        'ionian': major_scale(note),
        'aeolian': natural_minor_scale(note)
    }

    # Mapping of chord qualities for different modes
    chord_qualities = {
        'major': ['maj', 'min', 'min', 'maj', 'maj', 'min', 'dim'],
        'natural minor': ['min', 'dim', 'maj', 'min', 'min', 'maj', 'maj'],
        'harmonic minor': ['min', 'dim', 'aug', 'min', 'maj', 'maj', 'dim'],
        'melodic minor': ['min', 'min', 'aug', 'maj', 'maj', 'dim', 'dim'],
        'dorian': ['min', 'min', 'maj', 'maj', 'min', 'dim', 'maj'],
        'phrygian': ['min', 'maj', 'maj', 'min', 'dim', 'maj', 'min'],
        'lydian': ['maj', 'maj', 'min', 'dim', 'maj', 'min', 'min'],
        'mixolydian': ['maj', 'min', 'dim', 'maj', 'min', 'min', 'maj'],
        'locrian': ['dim', 'maj', 'min', 'min', 'maj', 'maj', 'min'],
        'ionian': ['maj', 'min', 'min', 'maj', 'maj', 'min', 'dim'],
        'aeolian': ['min', 'dim', 'maj', 'min', 'min', 'maj', 'maj']
    }

    if scale in scales_and_modes:
        scale_notes = scales_and_modes[scale]  # Get the notes of the chosen scale/mode
        chord_types = chord_qualities[scale]  # Get the chord types for that scale/mode

        # Assign the chords to the scale degrees
        first = scale_notes[0] + chord_types[0]
        second = scale_notes[1] + chord_types[1]
        third = scale_notes[2] + chord_types[2]
        fourth = scale_notes[3] + chord_types[3]
        fifth = scale_notes[4] + chord_types[4]
        sixth = scale_notes[5] + chord_types[5]
        seventh = scale_notes[6] + chord_types[6]

        # Output the chord progression
        return(f"I={first}, II={second}, III={third}, IV={fourth}, V={fifth}, VI={sixth}, VII={seventh}")
    else:
        return(f"Scale '{scale}' is not recognized. Please choose a valid scale or mode.")

print(chord_prog(note, scale))
print(chord_prog(note=1, scale='major'))