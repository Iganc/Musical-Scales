##major
## natural minor, harmonic minor, melodic minor
##modes
##adapt it to 12 keys
##chords:
##minor 7th, major 7th, maj7
##sus2, sus4


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

note = input("Give me a note: ").upper()
note = letter_to_num.get(note, None)


# print(note)
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


def ionan_mode(note):
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

def chord_prog(note):
    scale = input("What scale are you using? ").lower()
    if scale == "major":
        major_scale_notes = major_scale(note)
        first = major_scale_notes[0] + "maj"
        second = major_scale_notes[1] + "min"
        third = major_scale_notes[2] + "min"
        fourth = major_scale_notes[3] + "maj"
        fifth = major_scale_notes[4] + "maj"
        sixth = major_scale_notes[5] + "min"
        seventh = major_scale_notes[6] + "dim"
    if scale == "natural minor" or scale =="minor":
        natural_minor_notes = natural_minor_scale(note)
        first = natural_minor_notes[0] + "min"
        second = natural_minor_notes[1] + "dim"
        third = natural_minor_notes[2] + "maj"
        fourth = natural_minor_notes[3] + "min"
        fifth = natural_minor_notes[4] + "min"
        sixth = natural_minor_notes[5] + "maj"
        seventh = natural_minor_notes[6] + "maj"
    print(f"I={first}, II={second}, III={third}, IV={fourth}, V={fifth}, VI={sixth}, VII={seventh}")


def chord_identifier(note):
    notes = input("Insert the notes (separated by spaces): ").split()
    numbers = sorted(letter_to_num[note] for note in notes)
    print("Notes:", notes)
    print("numbers", numbers)

    if len(numbers) == 3:

        intervals = [
            (numbers[1] - numbers[0]) % 12,
            (numbers[2] - numbers[1]) % 12,
            (numbers[2] - numbers[0]) % 12
        ]
        # Sort intervals to match with known patterns
        intervals = sorted(set(intervals))
        print("Intervals:", intervals)

        # Define chord patterns
        major = [0, 4, 7]  # Major chord intervals
        minor = [0, 3, 7]  # Minor chord intervals
        diminished = [0, 3, 6]  # Diminished chord intervals
        augmented = [0, 4, 8]  # Augmented chord intervals

        # Determine the chord type
        if intervals == major:
            print(f"The chord is a {num_to_letter[root]} major chord.")
        elif intervals == minor:
            print(f"The chord is a {num_to_letter[root]} minor chord.")
        elif intervals == diminished:
            print(f"The chord is a {num_to_letter[root]} diminished chord.")
        elif intervals == augmented:
            print(f"The chord is a {num_to_letter[root]} augmented chord.")
        else:
            print("The chord is neither major, minor, diminished, nor augmented.")
    else:
        print("Please enter exactly three notes.")
    if len(numbers) == 4:
        intervals = {
            "maj_7": [1, 5, 8, 10],
            "min_7": [1, 4, 8, 10],
            "sus2": [1, 3, 5, 8],
            "sus4": [1, 5, 6, 8]
        }








# print("The major (ionan) scale of your note is:", major_scale(note))
# print(dorian_mode(note))
# print(phrygian_mode(note))
# print(lydian_mode(note))
# print(mixolydian_mode(note))
# print(locrian_mode(note))
# chord_prog(note)
print(chord_identifier(note))