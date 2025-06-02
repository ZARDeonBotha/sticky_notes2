from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm


def note_list(request):
    """
    Displays a list of all notes stored in the database.

    This view queries all available notes from the database
    and renders them in the 'note_list.html' template, passing the
    retrieved notes to the context.

    :param request: HttpRequest object representing metadata
    about the request.
    :type request: HttpRequest
    :return: HttpResponse containing the rendered template with
    the list of notes.
    :rtype: HttpResponse
    """
    notes = Note.objects.all()
    return render(request,
                  'notes/note_list.html',
                  {'notes': notes}
                  )


def note_detail(request, pk):
    """
    Retrieve and render the details of a specific note.

    This view fetches a note object identified by its primary key (`pk`)
    from the database. If the note with the given `pk` does not exist,
    an HTTP 404 error is automatically raised and handled.
    Upon successfully retrieving the note, it is passed to the specified
    template for rendering.

    :param request: The HTTP request object associated with the current
        client request.
    :type request: HttpRequest
    :param pk: The primary key of the note to be retrieved.
    :type pk: int
    :return: An HTTP response object containing the rendered template
        with the specified note's details.
    :rtype: HttpResponse
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request,
                  'notes/note_detail.html',
                  {'note': note}
                  )


def note_create(request):
    """
    Handles the creation of a new note. If the HTTP request method
    is POST, it processes the submitted form, validates it, and saves the
    note. Otherwise, it initializes an
    empty form for creating a new note. Renders the note creation
    page with a form for user input.

    :param request: The HTTP request object provided by Django.
    It contains meta information about the request and any data submitted
    through the form.
    :type request: django.http.HttpRequest

    :return: Depending on the HTTP request method:
             - If the form submission is successful, it redirects
              the user to the note list page.
             - If the form submission is invalid, or if the
             request method is not
               POST, it returns an HTTP response rendering
               the note creation page with the corresponding form.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request,
                  'notes/note_form.html',
                  {'form': form}
                  )


def note_update(request, pk):
    """
    Handles the update of an existing note by processing the
    form submission or rendering the form for the user to edit the note.
    If the form is successfully submitted and valid,
    the changes are saved, and the user is redirected to the
    note list view.

    :param request: The HTTP request object containing metadata about
    the request and user input.
    :type request: HttpRequest
    :param pk: The primary key of the note to be updated.
    :type pk: int
    :return: An HTTP response redirecting to the note list view
    upon successful form submission or rendering the note form
    template for editing.
    :rtype: HttpResponse
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request,
                  'notes/note_form.html',
                  {'form': form}
                  )


def note_delete(request, pk):
    """
    Handles the deletion of a specific note instance.
    Retrieves the note with the specified primary key (`pk`)
    and checks if a POST request has been made to delete the note.
    If confirmed, the note is deleted, and the user is redirected
    to the note list. For non-POST requests,
    renders a confirmation template prompting the user to
    confirm the deletion.

    :param request: The HTTP request instance representing
    the current incoming request made by the user.
    :param pk: The primary key of the note instance to be retrieved
    and potentially deleted.
    :return: For POST requests, redirects to the note list after
    successful deletion of the note. For non-POST requests, renders a
    confirmation page to confirm the deletion of the note instance.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request,
                  'notes/note_confirm_delete.html',
                  {'note': note}
                  )
