from django.db import models


class Note(models.Model):
    """
    Represents a note with a title, content, and a timestamp
    for when it was created.

    This class is used to store information about individual notes,
    including their title, the full content of the note, and the
    creation timestamp. It is commonly used in applications where
    organizing or storing text-based notes is required.

    :ivar title: The title of the note.
    :type title: str
    :ivar content: The main body or content of the note.
    :type content: str
    :ivar created_at: The timestamp indicating when the note was
    created.
    :type created_at: datetime.datetime
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
