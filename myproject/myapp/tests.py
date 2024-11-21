from django.test import TestCase
from django.urls import reverse

from myproject.myapp.views import generate_scales


class ExploreScalesViewTests(TestCase):

    def test_get_view(self):
        response = self.client.get(reverse('explore_scales_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/explore-scales.html')

    def test_post_valid_data(self):
        data = {'note': 'C', 'scale': 'major'}
        response = self.client.post(reverse('explore_scales_view'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'C major scale')

    def test_post_invalid_note(self):
        data = {'note': 'X', 'scale': 'major'}
        response = self.client.post(reverse('explore_scales_view'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid note: X')

    def test_post_missing_note_or_scale(self):
        data = {'note': 'C'}
        response = self.client.post(reverse('explore_scales_view'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please select both a note and a scale.')

class HomeViewTests(TestCase):

    def test_get_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/home.html')

class ProcessNoteViewTests(TestCase):

    def test_valid_note(self):
        data = {'note': 'C'}
        response = self.client.post(reverse('process_note'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'C major scale')

    def test_invalid_note(self):
        data = {'note': 'X'}
        response = self.client.post(reverse('process_note'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid note')

class ExploreChordsViewTests(TestCase):

    def test_post_valid_data(self):
        data = {'note': 'C', 'scale': 'major'}
        response = self.client.post(reverse('explore_chords'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'C major chord progression')

    def test_post_invalid_note(self):
        data = {'note': 'X', 'scale': 'major'}
        response = self.client.post(reverse('explore_chords'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid note: X')

    def test_post_missing_note_or_scale(self):
        data = {'note': 'C'}
        response = self.client.post(reverse('explore_chords'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please select both a note and a scale.')

class IdentifyScalesViewTests(TestCase):

    def test_valid_notes(self):
        data = {'notes': 'C E G'}
        response = self.client.post(reverse('identify_scales'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Matching scales')

    def test_invalid_notes(self):
        data = {'notes': 'X Y Z'}
        response = self.client.post(reverse('identify_scales'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid notes')

    def test_select_scale_choice(self):
        data = {'scale_choice': 'C major'}
        response = self.client.post(reverse('identify_scales'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'C major scale notes')

    def test_invalid_scale_choice_format(self):
        data = {'scale_choice': 'C major scale'}
        response = self.client.post(reverse('identify_scales'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid scale input format.')

class GenerateScalesTests(TestCase):

    def test_generate_scales(self):
        root_num = 1  # C
        scales = generate_scales(root_num)
        self.assertIn('major', scales)
        self.assertIn('natural minor', scales)
        self.assertIn('harmonic minor', scales)
        # Add more checks for specific scale results
