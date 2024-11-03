from .DICTIONARIES import letter_to_num, num_to_letter
note = input("Give me a note: ").upper()
note = letter_to_num.get(note, None)



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


def choice():
    scale = input("What scale or scales would you like to see? ").lower()
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
        'aeolian': aeolian_mode(note)
    }
    if scale in scales_and_modes:
        chosen_scale = scales_and_modes[scale]

        print(f"the {scale} scale is:", chosen_scale)


choice()