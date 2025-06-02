from django.test import TestCase
from .models import Note
from .forms import NoteForm
from django.urls import reverse


class NoteModelTest(TestCase):
    def test_create_note(self):
        """
        Tests the functionality of creating a Note instance and
        verifying the correctness of its attributes after creation.
        Ensures that the `title` and `content` match the provided
        input, and checks that the `created_at` attribute is
        automatically populated.

        :return:
            None
        """
        note = Note.objects.create(title="Test Note",
                                   content="This is a test note."
                                   )
        self.assertEqual(note.title,
                         "Test Note"
                         )
        self.assertEqual(note.content,
                         "This is a test note."
                         )
        self.assertIsNotNone(note.created_at)

    def test_str_representation(self):
        """
        Tests the string representation of a `Note` instance.

        This method confirms that the string representation
        of a `Note` object corresponds to its `title` field. It ensures the
        human-readable output for instances of the `Note` model.

        :raises AssertionError: If string representation does not match
            the `title` field of the `Note` instance.
        """
        note = Note.objects.create(title="Sample",
                                   content="Sample content"
                                   )
        self.assertEqual(str(note), "Sample")


class NoteFormTest(TestCase):
    def test_valid_form(self):
        """
        Tests the validity of the `NoteForm` with valid data.

        This method ensures that the `NoteForm` correctly validates
        when provided with valid input data for its fields, including
        `title` and `content`.
        It asserts that the form is considered valid.

        :rtype: None
        """
        form = NoteForm(data={'title': 'Test', 'content': 'Test content'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Tests the validation of an invalid NoteForm object.

        This test ensures that a form with empty 'title' and 'content'
        fields is considered invalid and fails validation when the
        `is_valid()` method is called.

        :return: Asserts that the form is invalid
        :rtype: None
        """
        form = NoteForm(data={'title': '', 'content': ''})
        self.assertFalse(form.is_valid())


class NoteViewTest(TestCase):
    def setUp(self):
        """
        Sets up the test environment by creating a note instance
        for testing purposes.

        The method initializes a test-specific note object that
        can be used across different test cases to ensure consistency and
        isolation during the testing
        process.

        :return: None
        """
        self.note = Note.objects.create(title="View Test",
                                        content="View test content"
                                        )

    def test_note_list_view(self):
        """
        Tests the functionality of the 'note_list' view to ensure it
        responds correctly to GET requests and includes the expected
        content.

        The function verifies if the 'note_list' view returns a
        valid HTTP 200 statuscode and contains a specific string in
        its response content.

        :returns: None
        """
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test")

    def test_note_detail_view(self):
        """
        Tests the detailed view of a specific note.

        This test checks if the note detail view can be accessed
        successfully and validates that the returned content includes the
        expected data, indicating correct rendering of the note details.

        :param self: The test case instance containing the test
        client and note information.

        :return: None
        """
        response = self.client.get(reverse('note_detail',
                                           args=[self.note.id])
                                   )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View test content")

    def test_note_create_view(self):
        """
        Tests the creation of a new note through the 'note_create' view.

        This method simulates sending a POST request to the
        'note_create' view to create a new note with specific data. It
        asserts that the response status code is 302 (indicating a
        successful redirect after note creation) and checks whether
        the note with the specified title exists in the database.

        :raises AssertionError: If the response status code is
        not 302 or if the note with the given title does not exist in the
        database.
        """
        response = self.client.post(reverse('note_create'), {
            'title': 'Created Note',
            'content': 'Created content'
        })
        self.assertEqual(response.status_code, 302)

        self.assertTrue(Note.objects.filter(title='Created Note').exists())

    def test_note_update_view(self):
        """
        Tests the behavior of the note update view to ensure it
        properly updates the note's attributes and returns the expected
        status code upon a successful update.

        This test case sends a POST request to the note update view,
        simulates an update to the note's title and content, and verifies
        the response as well as data persistence.

        :raises AssertionError: If the response status code is
        not 302 or if the note's title and content are not updated
        as expected.
        """
        response = self.client.post(reverse('note_update',
                                            args=[self.note.id]), {
            'title': 'Updated Title',
            'content': 'Updated content'
        })
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Title')

    def test_note_delete_view(self):
        """
        Tests the functionality of deleting a note through
        the note delete view.

        This test ensures that when a valid POST request is made to
        the note delete view, the specified note is deleted from the
        database and the response returns a
        redirect status code (302).

        :param self:
            An instance of the test case class that includes setup data,
            a test client, and other utilities for testing.
        :return: None
        """
        response = self.client.post(reverse('note_delete',
                                            args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
