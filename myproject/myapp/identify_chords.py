from DICTIONARIES import letter_to_num, num_to_letter


def chord_identifier():
    notes = input("Insert the notes (separated by spaces): ").split()
    notes = [n.upper() for n in notes]

    # Convert notes to their numeric representation
    numbers = [letter_to_num.get(note) for note in notes]

    # Define chord interval patterns
    major = [0, 4, 7]
    minor = [0, 3, 7]
    diminished = [0, 3, 6]
    augmented = [0, 4, 8]
    sus2 = [0, 2, 7]
    sus4 = [0, 5, 7]
    maj7 = [0, 4, 7, 11]
    min7 = [0, 3, 7, 10]
    add9 = [0, 2, 4, 7]
    dim7 = [0, 3, 6, 9]
    sus47 = [0, 5, 7, 10]
    dom9 = [0, 4, 7, 10, 14]
    maj9 = [0, 4, 7, 11, 14]
    min9 = [0, 3, 7, 10, 14]
    dom11 = [0, 4, 7, 10, 14, 17]
    min11 = [0, 3, 7, 10, 14, 17]
    maj13 = [0, 4, 7, 11, 14, 17, 21]
    min13 = [0, 3, 7, 10, 14, 17, 21]
    dom13 = [0, 4, 7, 10, 14, 17, 21]
    seven_sharp5 = [0, 4, 8, 10]
    seven_flat5 = [0, 4, 6, 10]
    seven_sharp9 = [0, 4, 7, 10, 15]
    seven_flat9 = [0, 4, 7, 10, 13]
    add4 = [0, 4, 5, 7]
    min_add9 = [0, 3, 7, 14]
    six_nine = [0, 4, 7, 9, 14]
    seven_sharp5_sharp9 = [0, 4, 8, 10, 15]
    seven_flat5_flat9 = [0, 4, 6, 10, 13]
    thirteen_flat9 = [0, 4, 7, 10, 13, 21]

    for i, root in enumerate(numbers):

        intervals = sorted([(note - root) % 12 for note in numbers])

        # Check for a match with known chord patterns
        if intervals == major:
            print(f"The chord is a {num_to_letter[root]} major chord.")
            return
        elif intervals == minor:
            print(f"The chord is a {num_to_letter[root]} minor chord.")
            return
        elif intervals == diminished:
            print(f"The chord is a {num_to_letter[root]} diminished chord.")
            return
        elif intervals == augmented:
            print(f"The chord is a {num_to_letter[root]} augmented chord.")
            return
        elif intervals == sus2:
            print(f"The chord is a {num_to_letter[root]} sus2 chord.")
            return
        elif intervals == sus4:
            print(f"The chord is a {num_to_letter[root]} sus4 chord.")
            return
        elif intervals == maj7:
            print(f"The chord is a {num_to_letter[root]} major 7 chord.")
            return
        elif intervals == min7:
            print(f"The chord is a {num_to_letter[root]} minor 7 chord.")
            return
        elif intervals == add9:
            print(f"The chord is a {num_to_letter[root]} add9 chord.")
            return
        elif intervals == dim7:
            print(f"The chord is a {num_to_letter[root]} diminished 7 chord.")
            return
        elif intervals == sus47:
            print(f"The chord is a {num_to_letter[root]} 7sus4 chord.")
            return
        elif intervals == dom9:
            print(f"The chord is a {num_to_letter[root]} dominant 9 chord.")
            return
        elif intervals == maj9:
            print(f"The chord is a {num_to_letter[root]} major 9 chord.")
            return
        elif intervals == min9:
            print(f"The chord is a {num_to_letter[root]} minor 9 chord.")
            return
        elif intervals == dom11:
            print(f"The chord is a {num_to_letter[root]} dominant 11 chord.")
            return
        elif intervals == min11:
            print(f"The chord is a {num_to_letter[root]} minor 11 chord.")
            return
        elif intervals == maj13:
            print(f"The chord is a {num_to_letter[root]} major 13 chord.")
            return
        elif intervals == min13:
            print(f"The chord is a {num_to_letter[root]} minor 13 chord.")
            return
        elif intervals == dom13:
            print(f"The chord is a {num_to_letter[root]} dominant 13 chord.")
            return
        elif intervals == seven_sharp5:
            print(f"The chord is a {num_to_letter[root]} 7♯5 chord.")
            return
        elif intervals == seven_flat5:
            print(f"The chord is a {num_to_letter[root]} 7♭5 chord.")
            return
        elif intervals == seven_sharp9:
            print(f"The chord is a {num_to_letter[root]} 7♯9 chord.")
            return
        elif intervals == seven_flat9:
            print(f"The chord is a {num_to_letter[root]} 7♭9 chord.")
            return
        elif intervals == add4:
            print(f"The chord is a {num_to_letter[root]} add4 chord.")
            return
        elif intervals == min_add9:
            print(f"The chord is a {num_to_letter[root]} minor add9 chord.")
            return
        elif intervals == six_nine:
            print(f"The chord is a {num_to_letter[root]} 6/9 chord.")
            return
        elif intervals == seven_sharp5_sharp9:
            print(f"The chord is a {num_to_letter[root]} 7♯5♯9 chord.")
            return
        elif intervals == seven_flat5_flat9:
            print(f"The chord is a {num_to_letter[root]} 7♭5♭9 chord.")
            return
        elif intervals == thirteen_flat9:
            print(f"The chord is a {num_to_letter[root]} 13♭9 chord.")
            return


    print("No chord found.")


chord_identifier()
