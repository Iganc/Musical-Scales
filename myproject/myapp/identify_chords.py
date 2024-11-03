from DICTIONARIES import letter_to_num, num_to_letter



def chord_identifier():

    notes = input("Insert the notes (separated by spaces): ").split()
    notes = [n.upper() for n in notes]
    # print("Converted notes to uppercase:", notes)
    # print(notes)

    numbers = [letter_to_num.get(note) for note in notes] ##IF SORTED THEN SOME CHORDS DONT WORK, IF NOT SORTED THEN NOTES HAVE TO BE ENTERED IN THE RIGHT ORDER
    root = numbers[0]
    # print("Notes:", notes)
    # print("numbers", numbers)
    # print("ROOT:", root)
    if len(numbers) == 3:
        intervals = [
            (numbers[0] - numbers[0]) % 12,
            (numbers[2] - numbers[1]) % 12,
            (numbers[2] - numbers[0]) % 12
        ]
        # Sort intervals to match with known patterns
        intervals = sorted(set(intervals))
        # print("Intervals:", intervals)

        major = [0, 3, 7]
        minor = [0, 4, 7]
        diminished = [0, 5, 8]
        augmented = [0, 4, 8]
        sus2 = [0, 5, 7]
        sus4 = [0, 2, 7]

        if intervals == major:
            print(f"The chord is a {num_to_letter[root]} major chord.")
        elif intervals == minor:
            print(f"The chord is a {num_to_letter[root]} minor chord.")
        elif intervals == diminished:
            print(f"The chord is a {num_to_letter[root]} diminished chord.")
        elif intervals == augmented:
            print(f"The chord is a {num_to_letter[root]} augmented chord.")
        elif intervals == sus2:
            print(f"The chord is a {num_to_letter[root]} sus2 chord.")
        elif intervals == sus4:
            print(f"The chord is a {num_to_letter[root]} sus4 chord.")
        else:
            print("No chord found.")

    if len(numbers) == 4:

        intervals = [
            (numbers[0] - numbers[0]) % 12,
            (numbers[1] - numbers[0]) % 12,
            (numbers[2] - numbers[0]) % 12,
            (numbers[3] - numbers[0]) % 12
        ]

        intervals = sorted(set(intervals))
        # print("Intervals:", intervals)

        maj7 = [0, 4, 7, 11]
        min7 = [0, 3, 7, 10]
        add9 = [0, 2, 4, 7]
        dim7 = [0, 3, 6, 9]
        sus47= [0, 2, 5, 7] ##NOT WORKING

        if intervals == maj7:
            print(f"The chord is a {num_to_letter[root]} major 7 chord.")
        elif intervals == min7:
            print(f"The chord is a {num_to_letter[root]} minor 7 chord.")
        elif intervals == add9:
            print(f"The chord is a {num_to_letter[root]}add9 chord.")
        elif intervals == dim7:
            print(f"The chord is a {num_to_letter[root]} diminished 7 chord.")
        elif intervals == sus47:
            print(f"The chord is a {num_to_letter[root]} 7sus4 chord.")
        else:
            print("No chord found.")

chord_identifier()