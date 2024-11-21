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

# from myapp.DICTIONARIES import letter_to_num, num_to_letter
# from myapp.EXPLORE_SCALES import major_scale, natural_minor_scale, harmonic_minor_scale, melodic_minor_scale, dorian_mode, lydian_mode, mixolydian_mode, ionian_mode, phrygian_mode, aeolian_mode, locrian_mode
notes = input("Insert the notes (separated by spaces), the first one being the root: ").split()


def key_identifier(notes):
    # Convert notes to uppercase and filter valid notes
    notes = [n.upper() for n in notes if n.upper() in letter_to_num]
    if not notes:
        raise ValueError("No valid notes found.")

    # Convert notes to numeric representation
    numbers = [letter_to_num[n] for n in notes]
    matching_scales = []

    # Loop through each note as a potential root and check scales
    for root in numbers:
        print(f"Checking scales starting from root: {num_to_letter[root]}")

        # Define scales based on the root using modular arithmetic within your 1-12 range
        scales_and_modes = {
            'major': major_scale(root),
            'natural minor': natural_minor_scale(root),
            'harmonic minor': harmonic_minor_scale(root),
            'melodic minor': melodic_minor_scale(root),
            'dorian': dorian_mode(root),
            'phrygian': phrygian_mode(root),
            'lydian': lydian_mode(root),
            'mixolydian': mixolydian_mode(root),
            'locrian': locrian_mode(root),
        }

        # Check each scale for a match with the notes
        for scale_name, scale_notes in scales_and_modes.items():
            # Convert numeric scale notes back to names
            scale_notes_nums = [letter_to_num[n.upper()] for n in scale_notes]

            # Then, adjust the scale notes numerically and convert them back to note names
            scale_notes_names = [num_to_letter[(n - 1) % 12 + 1] for n in scale_notes_nums]
            if all(note in scale_notes_names for note in notes):
                matching_scales.append(f"{num_to_letter[root]} {scale_name}")

    # Return matching scales or a default message
    return matching_scales if matching_scales else ["No matching scale found."]

print(key_identifier(notes))

