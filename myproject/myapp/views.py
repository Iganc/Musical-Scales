from os.path import split

from django.shortcuts import render

from .identify_scales import harmonic_minor_scale
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
    letter_to_num,
    num_to_letter,
)


from django.shortcuts import render
from .DICTIONARIES import letter_to_num, num_to_letter
from .EXPLORE_SCALES import major_scale, natural_minor_scale, harmonic_minor_scale, melodic_minor_scale, dorian_mode, lydian_mode, mixolydian_mode, ionian_mode, phrygian_mode, aeolian_mode, locrian_mode
from .explore_chord_progressions import chord_prog, scale
from .identify_chords import chord_identifier

def explore_scales_view(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        scale = request.POST.get('scale')

        if note is None or scale is None:
            return render(request, 'myapp/explore-scales.html', {
                'error': "Please select both a note and a scale.",
            })

        note = note.upper()
        note_num = letter_to_num.get(note, None)

        if note_num is None:
            return render(request, 'myapp/explore-scales.html', {
                'error': f"Invalid note: {note}. Please enter a valid note.",
            })


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
            result = []

        return render(request, 'myapp/explore-scales.html', {
            'note': note,
            'scale': scale,
            'result': result,
        })

    return render(request, 'myapp/explore-scales.html')




def home(request):
    return render(request, 'myapp/home.html')

def process_note(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        note_num = letter_to_num.get(note.upper(), None)


        if note_num:
            scale = major_scale(note_num)
            return render(request, 'myapp/result.html', {'scale': scale})
        else:
            return render(request, 'myapp/result.html', {'error': 'Invalid note'})

    return render(request, 'myapp/home.html')

from django.shortcuts import render




def explore_chords(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        scale = request.POST.get('scale')

        if note is None or scale is None:
            return render(request, 'myapp/explore-chord-progressions.html', {
                'error': "Please select both a note and a scale.",
            })

        note = note.upper()
        note_num = letter_to_num.get(note, None)

        if note_num is None:
            return render(request, 'myapp/explore-chord-progressions.html', {
                'error': f"Invalid note: {note}. Please enter a valid note.",
            })


        result = chord_prog(note_num, scale)


        result = [chord.strip() for chord in result.split(',')]

        return render(request, 'myapp/explore-chord-progressions.html', {
            'note': note,
            'scale': scale,
            'result': result,
        })

    return render(request, 'myapp/explore-chord-progressions.html')



def identify_chords(request):
    selected_notes = []

    if request.method == 'POST':
        notes = request.POST.get('notes')

        if notes is None or notes.strip() == '':
            return render(request, 'myapp/identify-chords.html', {
                'error': "Please select at least one note.",
            })

        notes = notes.upper().split()
        selected_notes = notes
        notes_num = [letter_to_num.get(note, None) for note in notes]

        if None in notes_num:
            invalid_notes = [note for note in notes if letter_to_num.get(note) is None]
            return render(request, 'myapp/identify-chords.html', {
                'error': f"Invalid notes: {', '.join(invalid_notes)}. Please enter valid notes.",
                'selected_notes': selected_notes,
            })

        result = chord_identifier(notes)

        return render(request, 'myapp/identify-chords.html', {
            'result': result,
            'selected_notes': selected_notes,
        })

    return render(request, 'myapp/identify-chords.html', {
        'selected_notes': selected_notes,
    })

from myapp.identify_scales import key_identifier


def identify_scales(request):
    selected_scale = None
    matching_scales = []
    error_message = None
    root_note = None
    notes = []
    selected_scale_notes = None

    if request.method == 'POST':

        if 'notes' in request.POST:

            notes = request.POST.get('notes', '').split()
            print(f"Received notes: {notes}")

            if notes:
                matching_scales = key_identifier(notes)
                print(f"Matching scales: {matching_scales}")


        if 'scale_choice' in request.POST:
            selected_scale = request.POST.get('scale_choice')
            print(f"Selected scale: {selected_scale}")

            if selected_scale:
                split_scale = selected_scale.split()
                if len(split_scale) == 2:
                    root_note, scale_type = split_scale
                elif len(split_scale) == 3:
                    root_note = split_scale[0]
                    scale_type = ' '.join(split_scale[1:])
                else:
                    error_message = "Invalid scale input format. Expected format: 'Root ScaleType'"
                    return render(request, 'myapp/identify-scales.html', {'error': error_message})


                root_num = letter_to_num.get(root_note)
                scales = generate_scales(root_num)


                if scale_type in scales:
                    selected_scale_notes = scales[scale_type]
                    print(f"The notes of the selected {scale_type} scale are: {selected_scale_notes}")
                else:
                    error_message = f"Scale {scale_type} not found."
                    return render(request, 'myapp/identify-scales.html', {'error': error_message})


        if selected_scale is None:
            selected_scale_notes = None

        return render(request, 'myapp/identify-scales.html', {
            'matching_scales': matching_scales,
            'selected_scale': selected_scale,
            'root_note': root_note,
            'selected_scale_notes': selected_scale_notes,
            'error': error_message
        })


    return render(request, 'myapp/identify-scales.html')


def generate_scales(root_num):
    return {
        'major': major_scale(root_num),
        'natural minor': natural_minor_scale(root_num),
        'harmonic minor': harmonic_minor_scale(root_num),
        'melodic minor': melodic_minor_scale(root_num),
        'dorian': dorian_mode(root_num),
        'phrygian': phrygian_mode(root_num),
        'lydian': lydian_mode(root_num),
        'mixolydian': mixolydian_mode(root_num),
        'locrian': locrian_mode(root_num),
    }

def test_template(request):
    return render(request, 'myapp/explore-scales.html')