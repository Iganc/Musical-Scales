from myapp.DICTIONARIES import letter_to_num, num_to_letter

def chord_identifier(notes):
    notes = notes.split() if isinstance(notes, str) else notes
    notes = [n.upper() for n in notes]  # Convert all notes to uppercase

    numbers = [letter_to_num.get(note) for note in notes]

    identified_chords = []

    chord_patterns = {
        'major': [0, 4, 7],
        'minor': [0, 3, 7],
        'diminished': [0, 3, 6],
        'augmented': [0, 4, 8],
        'sus2': [0, 2, 7],
        'sus4': [0, 5, 7],
        'maj7': [0, 4, 7, 11],
        'min7': [0, 3, 7, 10],
        'add9': [0, 2, 4, 7],
        'dim7': [0, 3, 6, 9],
        'sus47': [0, 5, 7, 10],
        'dom9': [0, 4, 7, 10, 14],
        'maj9': [0, 4, 7, 11, 14],
        'min9': [0, 3, 7, 10, 14],
        'dom11': [0, 4, 7, 10, 14, 17],
        'min11': [0, 3, 7, 10, 14, 17],
        'maj13': [0, 4, 7, 11, 14, 17, 21],
        'min13': [0, 3, 7, 10, 14, 17, 21],
        'dom13': [0, 4, 7, 10, 14, 17, 21],
        'seven_sharp5': [0, 4, 8, 10],
        'seven_flat5': [0, 4, 6, 10],
        'seven_sharp9': [0, 4, 7, 10, 15],
        'seven_flat9': [0, 4, 7, 10, 13],
        'add4': [0, 4, 5, 7],
        'min_add9': [0, 3, 7, 14],
        'six_nine': [0, 4, 7, 9, 14],
        'seven_sharp5_sharp9': [0, 4, 8, 10, 15],
        'seven_flat5_flat9': [0, 4, 6, 10, 13],
        'thirteen_flat9': [0, 4, 7, 10, 13, 21],
    }

    for i, root in enumerate(numbers):
        intervals = sorted([(note - root) % 12 for note in numbers])

        for chord_name, pattern in chord_patterns.items():
            if intervals == pattern:
                identified_chords.append(f"The chord is a {num_to_letter[root]} {chord_name.replace('_',  ' ')} chord.")
                break

    return ' '.join(identified_chords) if identified_chords else "No chord found."

