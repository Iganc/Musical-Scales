# ##major
# ## natural minor, harmonic minor, melodic minor
# ##modes
# ##adapt it to 12 keys
# ##chords:
# ##minor 7th, major 7th, maj7
# ##sus2, sus4
#
#
# letter_to_num = {
#     'C': 1,
#     'C#': 2,
#     'D': 3,
#     'D#': 4,
#     'E': 5,
#     'F': 6,
#     'F#': 7,
#     'G': 8,
#     'G#': 9,
#     'A': 10,
#     'A#': 11,
#     'B': 12,
# }
# num_to_letter = {
#     1: 'C', 13: 'C',
#     2: 'C#', 14: 'C#',
#     3: 'D', 15: 'D',
#     4: 'D#', 16: 'D#',
#     5: 'E', 17: 'E',
#     6: 'F', 18: 'F',
#     7: 'F#', 19: 'F#',
#     8: 'G', 20: 'G',
#     9: 'G#', 21: 'G#',
#     10: 'A', 22: 'A',
#     11: 'A#', 23: 'A#',
#     12: 'B', 24: 'B',
# }
# flats_to_sharps = {
#     'C#': 'Db',
#     'D#': 'Eb',
#     'F#': 'Gb',
#     'G#': 'Ab',
#     'A#': 'Bb',
#     'Db': 'C#',
#     'Eb': 'D#',
#     'Gb': 'F#',
#     'Ab': 'G#',
#     'Bb': 'A#'
# }
#
#
# note = input("Give me a note: ").upper()
# note = letter_to_num.get(note, None)
#
#
# # print(note)
# def major_scale(note):
#     notes = [note, note + 2, note + 4, note + 5, note + 7, note + 9, note + 11]
#     notes = [num_to_letter.get(note, None) for note in notes]
#     return notes
#
#
# def natural_minor_scale(note):
#     notes = [note, note + 2, note + 3, note + 5, note + 7, note + 8, note + 10]
#     notes = [num_to_letter.get(note, None) for note in notes]
#     return notes
#
#
# def harmonic_minor_scale(note):
#     notes = [note, note + 2, note + 3, note + 5, note + 7, note + 8, note + 11]
#     notes = [num_to_letter.get(note, None) for note in notes]
#     return notes
#
#
# def melodic_minor_scale(note):
#     notes = [note, note + 2, note + 3, note + 5, note + 7, note + 9, note + 11]
#     notes = [num_to_letter.get(note, None) for note in notes]
#     return notes
#
#
# def ionan_mode(note):
#     notes = major_scale(note)
#     return notes
#
#
# def dorian_mode(note):
#     note = note - 2
#     if note == -1:
#         note = note + 12
#     if note == 0:
#         note = note + 11
#     notes = major_scale(note)
#     return notes
#
#
# def phrygian_mode(note):
#     note = note + 5
#     if note > 12:
#         note = note - 12
#     notes = natural_minor_scale(note)
#     return notes
#
#
# def lydian_mode(note):
#     note = note + 4
#     if note > 12:
#         note = note - 12
#     notes = natural_minor_scale(note)
#     return notes
#
# def mixolydian_mode(note):
#     note = note + 2
#     if note > 12:
#         note = note - 12
#     notes = natural_minor_scale(note)
#     return notes
#
# def aeolian_mode(note):
#     notes = natural_minor_scale(note)
#     return notes
#
# def locrian_mode(note):
#     note = note + 1
#     if note > 12:
#         note = note - 12
#     notes = major_scale(note)
#     return notes
#
# def chord_prog(note):
#     scale = input("What scale are you using? ").lower()
#     if scale == "major":
#         major_scale_notes = major_scale(note)
#         first = major_scale_notes[0] + "maj"
#         second = major_scale_notes[1] + "min"
#         third = major_scale_notes[2] + "min"
#         fourth = major_scale_notes[3] + "maj"
#         fifth = major_scale_notes[4] + "maj"
#         sixth = major_scale_notes[5] + "min"
#         seventh = major_scale_notes[6] + "dim"
#     if scale == "natural minor" or scale =="minor":
#         natural_minor_notes = natural_minor_scale(note)
#         first = natural_minor_notes[0] + "min"
#         second = natural_minor_notes[1] + "dim"
#         third = natural_minor_notes[2] + "maj"
#         fourth = natural_minor_notes[3] + "min"
#         fifth = natural_minor_notes[4] + "min"
#         sixth = natural_minor_notes[5] + "maj"
#         seventh = natural_minor_notes[6] + "maj"
#     print(f"I={first}, II={second}, III={third}, IV={fourth}, V={fifth}, VI={sixth}, VII={seventh}")
#
#
# def chord_identifier(note):
#
#     notes = input("Insert the notes (separated by spaces): ").split()
#     notes = [n.upper() for n in notes]
#     # print("Converted notes to uppercase:", notes)
#     # print(notes)
#
#     numbers = [letter_to_num.get(note) for note in notes] ##IF SORTED THEN SOME CHORDS DONT WORK, IF NOT SORTED THEN NOTES HAVE TO BE ENTERED IN THE RIGHT ORDER
#     root = numbers[0]
#     # print("Notes:", notes)
#     # print("numbers", numbers)
#     # print("ROOT:", root)
#     if len(numbers) == 3:
#         intervals = [
#             (numbers[0] - numbers[0]) % 12,
#             (numbers[2] - numbers[1]) % 12,
#             (numbers[2] - numbers[0]) % 12
#         ]
#         # Sort intervals to match with known patterns
#         intervals = sorted(set(intervals))
#         # print("Intervals:", intervals)
#
#         major = [0, 3, 7]
#         minor = [0, 4, 7]
#         diminished = [0, 5, 8]
#         augmented = [0, 4, 8]
#         sus2 = [0, 5, 7]
#         sus4 = [0, 2, 7]
#
#         if intervals == major:
#             print(f"The chord is a {num_to_letter[root]} major chord.")
#         elif intervals == minor:
#             print(f"The chord is a {num_to_letter[root]} minor chord.")
#         elif intervals == diminished:
#             print(f"The chord is a {num_to_letter[root]} diminished chord.")
#         elif intervals == augmented:
#             print(f"The chord is a {num_to_letter[root]} augmented chord.")
#         elif intervals == sus2:
#             print(f"The chord is a {num_to_letter[root]} sus2 chord.")
#         elif intervals == sus4:
#             print(f"The chord is a {num_to_letter[root]} sus4 chord.")
#         else:
#             print("No chord found.")
#
#     if len(numbers) == 4:
#
#         intervals = [
#             (numbers[0] - numbers[0]) % 12,
#             (numbers[1] - numbers[0]) % 12,
#             (numbers[2] - numbers[0]) % 12,
#             (numbers[3] - numbers[0]) % 12
#         ]
#
#         intervals = sorted(set(intervals))
#         # print("Intervals:", intervals)
#
#         maj7 = [0, 4, 7, 11]
#         min7 = [0, 3, 7, 10]
#         add9 = [0, 2, 4, 7]
#         dim7 = [0, 3, 6, 9]
#         sus47= [0, 2, 5, 7] ##NOT WORKING
#
#         if intervals == maj7:
#             print(f"The chord is a {num_to_letter[root]} major 7 chord.")
#         elif intervals == min7:
#             print(f"The chord is a {num_to_letter[root]} minor 7 chord.")
#         elif intervals == add9:
#             print(f"The chord is a {num_to_letter[root]}add9 chord.")
#         elif intervals == dim7:
#             print(f"The chord is a {num_to_letter[root]} diminished 7 chord.")
#         elif intervals == sus47:
#             print(f"The chord is a {num_to_letter[root]} 7sus4 chord.")
#         else:
#             print("No chord found.")
#
# def key_identifier(note):
#     notes = input("Insert the notes (separated by spaces), the first one being the root: ").split()
#     notes = [n.upper() for n in notes]
#     numbers = sorted(letter_to_num.get(n) for n in notes)
#     print("Notes:", notes)
#     print("Numbers:", numbers)
#
#     root = numbers[0]
#     print("Root:", root)
#
#     # Generate scales and modes
#     scales_and_modes = {
#         'major': major_scale(root),
#         'natural_minor': natural_minor_scale(root),
#         'harmonic_minor': harmonic_minor_scale(root),
#         'melodic_minor': melodic_minor_scale(root),
#         'dorian': dorian_mode(root),
#         'phrygian': phrygian_mode(root),
#         'lydian': lydian_mode(root),
#         'mixolydian': mixolydian_mode(root),
#         'locrian': locrian_mode(root),
#     }
#
#     matching_scales = []
#
#     # Check for matches
#     for scale_name, scale_notes in scales_and_modes.items():
#         if len(scale_notes) >= len(notes) and all(note in scale_notes for note in notes):
#             matching_scales.append(scale_name)
#
#     if matching_scales:
#         print(f"The scales that match: {', '.join(matching_scales)}.")
#         choice = input("Please choose one: ")
#         if choice in matching_scales:
#             return choice
#         else:
#             print("Invalid choice.")
#     else:
#         print("No matching scales found.")
#
#
#
#
#
# # print("The major (ionan) scale of your note is:", major_scale(note))
# # print(dorian_mode(note))
# # print(phrygian_mode(note))
# # print(lydian_mode(note))
# # print(mixolydian_mode(note))
# # print(locrian_mode(note))
# # chord_prog(note)
# # print(chord_identifier(note))
# print(key_identifier(note))