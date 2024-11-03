from django.shortcuts import render


from .scales import (
    major_scale,
    natural_minor_scale,
    harmonic_minor_scale,
    melodic_minor_scale,
    ionian_mode,
    dorian_mode,
    phrygian_mode,
    lydian_mode,
    mixolydian_mode,
    aeolian_mode,
    locrian_mode,
    chord_prog,
    chord_identifier,
    key_identifier,
    letter_to_num,
    num_to_letter,
)


from django.shortcuts import render
from .DICTIONARIES import letter_to_num, num_to_letter  # Import your dictionaries
from .EXPLORE_SCALES import major_scale, natural_minor_scale, harmonic_minor_scale, melodic_minor_scale, dorian_mode, lydian_mode, mixolydian_mode, ionian_mode, phrygian_mode, aeolian_mode, locrian_mode
from .explore_chord_progressions import chord_prog

def explore_scales_view(request):
    if request.method == 'POST':
        note = request.POST.get('note')  # Get the note
        scale = request.POST.get('scale')  # Get the selected scale

        if note is None or scale is None:
            # If no note or scale is selected, return the form with an error
            return render(request, 'myapp/explore-scales.html', {
                'error': "Please select both a note and a scale.",
            })

        note = note.upper()  # Convert note to uppercase
        note_num = letter_to_num.get(note, None)  # Convert letter note to number

        if note_num is None:
            return render(request, 'myapp/explore-scales.html', {
                'error': f"Invalid note: {note}. Please enter a valid note.",
            })

        # Determine the scale to display based on the user's selection
        if scale == 'major':
            result = major_scale(note_num)
        elif scale == 'natural minor':
            result = natural_minor_scale(note_num)
        elif scale == 'harmonic minor':
            result = harmonic_minor_scale(note_num)
        elif scale == 'melodic minor':
            result = melodic_minor_scale(note_num)
        elif scale == 'dorian':
            result = dorian_mode(note_num)
        elif scale == 'lydian':
            result = lydian_mode(note_num)
        elif scale == 'mixolydian':
            result = mixolydian_mode(note_num)
        elif scale == 'ionian':
            result = ionian_mode(note_num)
        elif scale == 'phrygian':
            result = phrygian_mode(note_num)
        elif scale == 'aeolian':
            result = aeolian_mode(note_num)
        elif scale == 'locrian':
            result = locrian_mode(note_num)
        else:
            result = []  # Default case if the scale is not recognized

        return render(request, 'myapp/explore-scales.html', {
            'note': note,
            'scale': scale,
            'result': result,  # Pass the resulting notes to the template
        })

    return render(request, 'myapp/explore-scales.html')




def home(request):
    return render(request, 'myapp/home.html')  # Ensure this path is correct

def process_note(request):
    if request.method == 'POST':
        note = request.POST.get('note')  # Get the note input from your form
        note_num = letter_to_num.get(note.upper(), None)

        # Use your Python logic (e.g., `major_scale`) here
        if note_num:
            scale = major_scale(note_num)  # Replace with the function you want to use
            return render(request, 'myapp/result.html', {'scale': scale})
        else:
            return render(request, 'myapp/result.html', {'error': 'Invalid note'})

    return render(request, 'myapp/home.html')

from django.shortcuts import render



# View for exploring chords
def explore_chords(request):
    if request.method == 'POST':
        note = request.POST.get('note')  # Get the note
        scale = request.POST.get('scale')  # Get the selected scale

        if note is None or scale is None:
            return render(request, 'myapp/explore-chord-progressions.html', {
                'error': "Please select both a note and a scale.",
            })

        note = note.upper()  # Convert note to uppercase
        note_num = letter_to_num.get(note, None)  # Convert letter note to number

        if note_num is None:
            return render(request, 'myapp/explore-chord-progressions.html', {
                'error': f"Invalid note: {note}. Please enter a valid note.",
            })

        # Call chord_prog with the correct note_num
        result = chord_prog(note_num, scale)

        # Assuming result is a string, split it into a list
        result = [chord.strip() for chord in result.split(',')]

        return render(request, 'myapp/explore-chord-progressions.html', {
            'note': note,
            'scale': scale,
            'result': result,  # Pass the resulting notes to the template
        })

    return render(request, 'myapp/explore-chord-progressions.html')


# View for identifying chords or scales
def identify_chords(request):
    # Add your logic for identifying chords and scales here
    return render(request, 'myapp/identify-chords.html')

def identify_scales(request):
    # Add your logic for identifying chords and scales here
    return render(request, 'myapp/identify-scales.html')

def test_template(request):
    return render(request, 'myapp/explore-scales.html')